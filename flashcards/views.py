from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import FlashcardsSerializer
from .models import Flashcards

# Create your views here.
@api_view(['GET'])
def cards(request):
    api_urls = {
        'List': '/flashcards-list/',
        'Detail View': '/flashcards-detail/<str:pk>/',
        'Create': '/flashcards-create/',
        'Update': '/flashcards-update/<str:pk>/',
        'Delete': '/flashcards-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def cardList(request):
    cards = Flashcards.objects.all()
    serializer = FlashcardsSerializer(cards , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cardDetail(request, pk):
    try:
        card = Flashcards.objects.get(id=pk)
    except Flashcards.DoesNotExist:
        return Response({'error': 'Card does not exist'}, status=404)
    
    serializer = FlashcardsSerializer(card, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def cardCreate(request):
    serializer = FlashcardsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def cardUpdate(request, pk):
    task =  Flashcards.objects.get(id=pk)
    serializer = FlashcardsSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def cardDelete(request, pk):
    task =  Flashcards.objects.get(id=pk)
    task.delete()
    return Response('Item successfully deleted!')