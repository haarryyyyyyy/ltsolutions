from django.db import models

# Create your models here.
class db(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    describe = models.TextField(null=True)
    qualification = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.first_name