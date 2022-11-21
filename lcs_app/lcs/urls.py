from django.urls import path

from . import views

app_name = "lcs"
urlpatterns = [
    path('add_stage/', views.add_stage_view, name='add_stage'),
    path('<int:pk>/', views.update_stage_view, name='update_stage'),
]