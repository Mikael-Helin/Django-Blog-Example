from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Homepage URL
    path('<int:pk>/', views.post_detail, name='post_detail'),  # Detail page URL
]