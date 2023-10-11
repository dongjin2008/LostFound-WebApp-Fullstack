from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  homeroom = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class LostItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  date_lost = models.DateField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name

class FoundItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  date_found = models.DateField()
  finder = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.name

class Claim(models.Model):
  lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
  found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE)
  date_claimed = models.DateField(auto_now_add=True)

  def __str__(self) -> str:
    return self.lost_item.name + " claimed by " + self.found_item.finder.first_name + " " + self.found_item.finder.last_name

