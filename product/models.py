from django.db import models
import uuid
# Create your models here.


class products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=255, unique=True)



