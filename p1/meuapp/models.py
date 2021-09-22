from django.db import models


class Pessoas(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'Name: {self.name} | Last Name: {self.last_name}'
