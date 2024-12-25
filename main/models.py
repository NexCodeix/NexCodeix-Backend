from django.db import models


class Portfolio(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    profile_image = models.ImageField(
        upload_to="portfolio/profile_image/"
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class PortfolioContent(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.SET_NULL,
        null=True,
        related_name="contents"
    )
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.SET_NULL,
        null=True,
        related_name="images"
    )
    title = models.CharField(
        max_length=200,
    )
    profile_image = models.ImageField(
        upload_to="portfolio/images/"
    )

    def __str__(self):
        return self.title
