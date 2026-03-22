from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('candidate/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidate/<int:pk>/rename/', views.rename_candidate, name='rename_candidate'),
    path('candidate/<int:pk>/delete/', views.delete_candidate, name='delete_candidate'),
]
