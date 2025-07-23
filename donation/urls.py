from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_donor, name='register'),
    path('donors/', views.donor_list, name='donors'),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospital/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('hospital/<int:pk>/<str:form_type>/', views.hospital_form, name='hospital_form'),
]
