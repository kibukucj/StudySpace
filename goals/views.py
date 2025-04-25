from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from .models import Goal
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Imports for Reordering Feature
from django.views import View
from django.db import transaction
from .forms import PositionForm

class TaskList(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = 'tasks'
    template_name = 'goals/goal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks'].filter(user=self.request.user)
        today = timezone.now().date()
        goals_due_today = tasks.filter(deadline=today, complete=False)
        missed_goals = tasks.filter(deadline__lt=today, complete=False)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            tasks = tasks.filter(title__startswith=search_input)
        
        context.update({
            'tasks': tasks,
            'goals_due_today': goals_due_today,
            'missed_goals': missed_goals,
            'count': tasks.filter(complete=False).count(),
            'search_input': search_input,
        })
        
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Goal
    context_object_name = 'task'
    template_name = 'goals/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ['title', 'description', 'deadline','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['title', 'description', 'deadline', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))
    
def task_toggle_complete(request, id):
    task = get_object_or_404(Goal, id=id)
    if request.method == 'POST':
        task.complete = not task.complete
        task.save()
    return redirect('tasks')


