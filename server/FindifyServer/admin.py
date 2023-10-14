from django.contrib import admin
from .models import LostItem, FoundItem, Claim, User, Tag

admin.site.register(LostItem)
admin.site.register(User)
admin.site.register(Tag)