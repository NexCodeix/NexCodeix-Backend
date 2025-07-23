from django.db import models


class Domain(models.Model):
    name = models.CharField(
        max_length=100,
    )
    price = models.FloatField()
    link = models.URLField(
        max_length=2040,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    data = models.JSONField(
        default=dict,
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name