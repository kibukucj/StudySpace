from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'studyapp/login.html', {'success': 'Registration successful. Please login'})
        else:
            error_message = form.errors.as_text()
            return render(request, 'studyapp/register.html', {'error': error_message})
    return render (request, 'studyapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return render (request, 'studyapp/login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'studyapp/login.html')

@login_required
def videocall(request):
    return render(request, 'studyapp/videocall.html', {'name': request.user.username})    

def index(request):
    return render(request, 'studyapp/index.html')

@login_required
def home(request):
    return render(request, 'studyapp/home.html', {'name': request.user.username})

@login_required
def solospace(request):
    return render(request, 'studyapp/solospace.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'studyapp/joinroom.html')


