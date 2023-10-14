from rest_framework import serializers
from .models import LostItem, Tag,  User, FoundItem, Claim

class LostItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = LostItem
    fields = ['name', 'description', 'owner', 'date_lost', 'date_created', 'tags']

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['name']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email', 'homeroom']

class FoundItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoundItem
    fields = ['name', 'description', 'finder', 'date_found']

class ClaimSerializer(serializers.ModelSerializer):
  class Meta:
    model = Claim
    fields = ['lost_item', 'found_item', 'date_claimed']
