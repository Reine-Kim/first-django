from django.urls import path

from . import views

urlpatterns = [
    path('second/list/', views.list, name="list"),
    path('second/create/', views.create, name='create'),
    path('second/confirm/', views.confirm, name="confirm"),
]

