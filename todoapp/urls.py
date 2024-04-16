from django.urls import path

from todoapp import views



urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
]
