from django.urls import path, re_path

from . import views

urlpatterns = [
    path('first/', views.index, name='index'),
    path('first/about/', views.about, name="about"),
    path('first/product/', views.product, name='product'),
    path('first/notice/', views.notice, name="notice"),
    path('first/qna/', views.qna, name='qna')
]

