from django.http.response import JsonResponse
from products_api.models import Product
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins
#generic views

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin , mixins.CreateModelMixin,mixins.UpdateModelMixin , mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class= ProductSerializer
    queryset=Product.objects.all()

    lookup_field='id'

    def get(self,request,id=None):
        if id:
            return self.retrive(request)
        else:
            return self.list(request)
        return self.list(request) 
    
    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id):
        return self.destroy(request,id)



#class based views

class ProdcutAPIView(APIView):

    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#function based views
# Create your views here.
@api_view(['GET','POST'])
def product_list(request):

    if request.method == 'GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer= ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        product=Product.objects.get(pk=pk)
    
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)