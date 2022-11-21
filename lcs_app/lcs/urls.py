from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.update_stage_view, name='update_stage'),
]