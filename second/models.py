from django.db import models

# Create your models here.
class Post(models.Model): #장고모델상속받는 호스트클래스
    title = models.CharField(max_length=30) #30자짜리 문자열 저장
    content = models.TextField() #문자열길이 지정 안하고 저장

    created_at = models.DateTimeField(auto_now_add=True) #글 올릴 때 자동으로 현재시간 기록
    updated_at = models.DateTimeField(auto_now=True) #수정될 때 수정시간 기록
