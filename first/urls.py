from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('product/', views.product, name='product'),
    path('notice/', views.notice, name="notice"),
    path('qna/', views.qna, name='qna')
]

