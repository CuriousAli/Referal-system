from django.db import models
from phone.models import User
from phone.utils import generate_code


class Sms_Code(models.Model):
    auto_code = models.CharField(max_length=4, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auto_code)

    def save(self, *args, **kwargs):
        self.auto_code = generate_code(4)
        super().save(*args, **kwargs)
