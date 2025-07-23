from django.contrib import admin
from .models import Portfolio, PortfolioContent, PortfolioImage

admin.site.register(Portfolio)
admin.site.register(PortfolioContent)
admin.site.register(PortfolioImage)

