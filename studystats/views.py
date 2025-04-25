# views.py in your 'studyapp' or appropriate app
import json
from flashcard.models import Deck
from .models import StudySession
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('login')
    return render(request, 'studystats/profile.html', {'profile':profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)  
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False
      
    return render(request, 'studystats/profile_edit.html', { 'form':form, 'onboarding':onboarding })


@login_required
def profile_settings_view(request):
    return render(request, 'studystats/profile_settings.html')


@login_required
def profile_emailchange(request):
    
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            
            # Check if the email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            
            form.save() 
            
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile-settings')
        
    return redirect('chathome')


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('index')
    
    return render(request, 'studystats/profile_delete.html')


@login_required
@csrf_exempt
def save_study_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_time = parse_datetime(data['start_time'])
        end_time = parse_datetime(data['end_time'])
        StudySession.objects.create(user=request.user, start_time=start_time, end_time=end_time)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)


@login_required
def study_stats(request):
    # Aggregate study hours per day for the past 7 days
    user = request.user
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    sessions = StudySession.objects.filter(user=user, start_time__gte=week_ago, end_time__lte=today)

    data = {}
    for session in sessions:
        day = session.start_time.strftime('%Y-%m-%d')
        data[day] = data.get(day, 0) + session.duration()

    # Ensure all days in the past week are present in the data
    for i in range(7):
        day = (week_ago + timedelta(days=i)).strftime('%Y-%m-%d')
        if day not in data:
            data[day] = 0

    sorted_data = sorted(data.items())

    context = {
        'data': json.dumps(sorted_data),  # Pass the data as JSON to the template
    }
    return render(request, 'studystats/studystats.html', context)
