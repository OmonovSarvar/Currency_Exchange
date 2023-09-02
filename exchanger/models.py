from django.db import models
from django.utils import timezone


# Create your models here.
class Exchanger(models.Model):
    CHOICES = (
        ('UZS', "O'zbekiston So'mi"),
        ('USD', 'Amerika Dollari'),
        ('RUB', 'Rossiya Rubli'),
        ('KZT', 'Qozoqiston Tengesi'),
        ('TRY', 'Turikya Lirasi'),
        ('EUR', 'Yevro'),
    )
    value1 = models.CharField(max_length=10, choices=CHOICES, default='USD')
    value2 = models.CharField(max_length=10, choices=CHOICES, default='UZS')
    value = models.BigIntegerField()
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return f"{self.date}da {self.value1}dan {self.value2}ga exchange qilindi"