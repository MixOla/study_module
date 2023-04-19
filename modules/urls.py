from django.urls import path

from modules import views

urlpatterns = [
    path('create', views.ModuleCreateView.as_view(), name='module_create'),
    path('list', views.ModuleListView.as_view(), name='module_list'),
    path('<pk>', views.ModuleView.as_view(), name='module_pk'),

]