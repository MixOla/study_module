from django.urls import path

from modules import views

urlpatterns = [
    path('module/', views.ModuleCreateView.as_view(), name='module'),
    path('<pk>/', views.ModuleView.as_view(), name='module_pk'),

]