from django.urls import path
from studyapp import views as studyapp_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', studyapp_views.index, name='index'),

    #Register and Login
    path('register/', studyapp_views.register, name='register'),
    path('login/', studyapp_views.login_view, name='login'),

    #Home
    path('meeting/', studyapp_views.videocall, name='meeting'),
    path('join/', studyapp_views.join_room, name='join'),
    path('home/', studyapp_views.home, name='home'),

    #StudyTools
    path('solospace/', studyapp_views.solospace, name='solospace'),
    path('logout/', studyapp_views.logout_view, name='logout'),

    #Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
