from django.shortcuts import render
from django.http import JsonResponse
from . import models
from .serializers import LostItemSerializer

def list_lost_items(request):
  lost_item = models.LostItem.objects.all()
  LostItemSerializer(lost_item, many=True)
  return JsonResponse({'lost_items': lost_item})

def list_found_items(request):
  found_items = models.FoundItem.objects.all()
  return render(request, {'found_items': found_items})

def list_claims(request):
  claims = models.Claim.objects.all()
  return render(request, 'claims.html', {'claims': claims})

def list_users(request):
  users = models.User.objects.all()
  return render(request, 'users.html', {'users': users})

def create_lost_item(request):
  if request.method == 'POST':
    name = request.POST['name']
    description = request.POST['description']
    date_lost = request.POST['date_lost']
    owner = request.POST['owner']
    lost_item = models.LostItem(name=name, description=description, date_lost=date_lost, owner=owner)
    lost_item.save()
    return HttpResponse('Lost item created!')
  else:
    return render(request, 'create_lost_item.html')
