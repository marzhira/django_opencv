from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):

    description = models.CharField(max_length=255, blank=True)
    #빈칸 제출을 허용
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #업로드 기준
