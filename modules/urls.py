from django.urls import path

from modules import views

urlpatterns = [
    path('module/create', views.ModuleCreateView.as_view(), name='module_create'),
    path('module/list', views.ModuleListView.as_view(), name='module_list'),
    path('module/<pk>', views.ModuleView.as_view(), name='module_pk'),

]