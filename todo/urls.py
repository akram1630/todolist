from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    ##############################################################""
    path('api/todoList/', views.todoList, name='todoList'),
         #<str:pk> or <int:myPk> both work and name myPk
         #should be the same with parameter of views function :     
    path('api/todoId/<int:myPk>/', views.todoById, name='todoId'),
    path('api/newTask/', views.newTask, name='newTask'),
    path('api/delete/<int:pkD>/', views.deleteApi, name='deleteApi'),

]
