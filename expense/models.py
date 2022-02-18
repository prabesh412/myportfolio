from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expenses(models.Model):
    reason = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return str(self.reason)

    def amounts(self):
        return int(self.amount)