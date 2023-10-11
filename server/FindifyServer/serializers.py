from rest_framework import serializers
from .models import LostItem

class LostItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = LostItem
    fields = ['name', 'description', 'date_lost', 'owner', 'date_created']