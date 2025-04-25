# urls.py in your 'studyapp' or appropriate app
from django.urls import path
from studystats import views

urlpatterns = [
    path('stats/', views.study_stats, name='stats'),
    #path('create_study_session/', views.create_study_session, name='create_study_session'),
    path('save_study_session/', views.save_study_session, name='save_study_session'),

    path('profile/', views.profile_view, name="profile"),
    path('edit/', views.profile_edit_view, name="profile-edit"),
    path('onboarding/', views.profile_edit_view, name="profile-onboarding"),
    path('settings/', views.profile_settings_view, name="profile-settings"),
    path('emailchange/', views.profile_emailchange, name="profile-emailchange"),
    path('emailverify/', views.profile_emailverify, name="profile-emailverify"),
    path('delete/', views.profile_delete_view, name="profile-delete"),
]
