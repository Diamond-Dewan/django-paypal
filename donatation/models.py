from django.db import models


# Create your models here.
class Donate(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    is_donated = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_donation_info(self):
        return self.name + ' - ' + str(self.amount)

