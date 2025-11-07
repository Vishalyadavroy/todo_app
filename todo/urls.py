from django.urls import path
from todo import views

urlpatterns = [
    path('frontend/', views.todo_frontend, name='todo_frontend'),
    path('todos/', views.read_todo, name='list_todos'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<int:pk>/', views.get_todo, name='get_todo'),
    path('todos/<int:pk>/update/', views.update_todo, name='update_todo'),
    path('todos/<int:pk>/delete/', views.delete_todo, name='delete_todo'),
]
