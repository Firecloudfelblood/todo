from django.contrib import admin
from django.urls import path
from .views import edittaskview, todoview, addtask, deletetask, edittask

urlpatterns = [
    path('', todoview),
    path('addtask/', addtask ),
    path('deletetask/<int:taskpk>/', deletetask),
    path('edittask/<int:taskpk>/', edittaskview)
]
