from django.contrib import admin
from .models import LostItem, FoundItem, Claim, User

admin.site.register(LostItem)
admin.site.register(User)