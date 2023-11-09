from django.urls import path

from storeapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student_form/', views.student_form, name='student_form'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.success, name='success'),
]