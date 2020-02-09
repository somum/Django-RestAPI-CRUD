from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
import requests
from .models import flight
from .serializers import flightSerializer

@api_view(['GET', 'POST'])
def flightList(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flight_list.html'

    if request.method == 'GET':
        snippets = flight.objects.all()
        serializer = flightSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #converting json format into dictionary
        serializer = flightSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flightList_details(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = flight.objects.get(pk=pk)
    except flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = flightSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = flightSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















