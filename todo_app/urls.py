from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('complete/<int:pk>/', views.complete_view, name='complete'),
]