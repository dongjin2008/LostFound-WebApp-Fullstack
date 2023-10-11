from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  homeroom = models.CharField(max_length=255)

  def __str__(self):
    return self.user.first_name

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name
  

class LostItem(models.Model):
  name = models.CharField(max_legth=255)
  description = models.TextField()
  tags = models.ManyToManyField(Tag, related_name='lost_items')
  location = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='lost_item_images', blank=True)
  is_found = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class Claim(models.Model):
  lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
  claimant = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Claim for {self.lost_item.name} at 0 floor"
  