from django.urls import path
from . import views


app_name = 'brainstorm'


urlpatterns = [
    path('', views.BrainstormHome.as_view(), name='home'),
    path('questions/', views.BSCreateView.as_view(), name='questions'),  # todo add View
    path('result/', views.BSListView, name='result'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.BSUpdateView.as_view(), name='update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.BSDeleteView.as_view(), name='delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
]
