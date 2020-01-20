from django.db import models

CATEGORIES = (
    ('starters', 'STARTERS'),
    ('mains', 'MAINS'),
    ('desserts', 'DESSERTS'),
    ('drinks', 'DRINKS')
)

class Product(models.Model):
    "Define a product"

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=15, choices=CATEGORIES, default='starters')
    name = models.CharField(max_length=500, default='', unique=True)
    price = models.FloatField()
    short_description = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name