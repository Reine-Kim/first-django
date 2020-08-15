#모델 하나가 테이블 하나
#한 테이블과 다른 테이블을 연결하기 위한 식별자를 ForeignKey임!
#모델 바꾸면 무조건 migrations 해줘야함
#makemigrations로 migration 파일 생성하고 migrate시켜서 DB에 업로드
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # ▼ 리뷰 데이터가 어떤 식당을 가리키는지 나타내는 속성
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) #아이디가 3인 곳에 리뷰 쓰면 이값은 3?
    #on_delete: 레스토랑이 삭제되었을 때 리뷰는 어떻게 할거냐! CASCADE=리뷰도 같이 삭제 / SENT_NULL은 레스토랑을 NULL처리 하겠다
