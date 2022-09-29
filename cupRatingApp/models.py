from django.db import models

rating_choices = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]


class Cup(models.Model):
    uId = models.UUIDField(primary_key=True, unique=True ,editable=False)
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(choices=rating_choices, blank=True, null=True)

    def __str__(self):
        return f"{self.name}:\n\t{self.description}\n\t{self.price}"
