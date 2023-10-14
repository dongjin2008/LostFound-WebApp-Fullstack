from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from . import models
from .serializers import LostItemSerializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def lost_items(request):
  if request.method == 'GET':
    lost_items = models.LostItem.objects.all()
    serializer = LostItemSerializer(lost_items, many=True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == 'POST':
    serializer = LostItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def lost_item(request, id):

  try:
    lost_item = models.LostItem.objects.get(pk=id)
  except models.LostItem.DoesNotExist:
    return JsonResponse({'error': 'Lost item not found'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = LostItemSerializer(lost_item)
    return JsonResponse(serializer.data)
  elif request.method == 'DELETE':
    lost_item.delete()
    return JsonResponse({'message': 'Lost item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
  elif request.method == 'PUT':
    serializer = LostItemSerializer(lost_item, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)