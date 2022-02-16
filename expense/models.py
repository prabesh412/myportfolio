from django.db import models

# Create your models here.
class expenses(models.Model):
    reason = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.reason)

    def amounts(self):
        return int(self.amount)