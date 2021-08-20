from django.db import models


class Recipe(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=True)
    Category = models.CharField(max_length=40, null=False, blank=True)
    Image = models.CharField(max_length=200, null=False, blank=True)
    Ingredients = models.CharField(max_length=50, null=False, blank=True)
    Instructions = models.TextField(null=False, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name', 'id')
