from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from drftest.models import Coordination
from drftest.serializers import CoordinateSerializer

from rest_framework.response import Response
from rest_framework import status
from .models import Client,Coordination

# Create your views here.

class CoordinateCreateAPIView(APIView):
    
    def get(self,request):
        #active=true : 유효한 객체만 불러온다
        coordinations=Coordination.objects.filter(active=True)
        serializer =CoordinateSerializer(coordinations,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CoordinateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CoordinateDetatilAPIView(APIView):
    def get_object(self,pk):
        coordination=get_object_or_404(Coordination,pk=pk)
        return coordination
    
    def get(self,request,pk):
        coordination=self.get_object(pk)
        serializer=CoordinateSerializer(coordination)
        return Response(serializer.data)

    def put(self,request,pk):
        coordination=self.get_object(pk)
        serializer=CoordinateSerializer(coordination,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        coordination = self.get_object(pk)
        coordination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



    
