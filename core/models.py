from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class SanPham(models.Model):
    ten_loai= models.CharField(max_length=255)
    ten_sanpham= models.CharField(max_length=255)
    anh= models.CharField(max_length=255)
    gia = models.IntegerField()
    def __str__(self):
        return self.ten_sanpham


