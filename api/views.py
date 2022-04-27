from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response  
from .serializers import RegistrationSerializer,BookSerializer
from rest_framework import permissions
from .models import Account,Book
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
  
# Create your views here. 

@api_view(['GET'])   
def get_books(request):
    """
    This is a function based view which only allowed GET method

    """

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

 

class  BookDetails(APIView):

    """
    Class based view for all CRUD operations
    permissions allowed to only authenticated admin
    """
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self,id):
        try:
            return Book.objects.get(id = id)
        except Book.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
            

    def get(self,request,id):
            book  = self.get_object(id)
            serializer = BookSerializer(book)
            return Response(serializer.data) 


    def put(self,request,id):
        book = self.get_object(id)
        serializer = BookSerializer(book ,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def delete(self,request,id):
        book = self.get_object(id)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





class AdminViewSet(APIView):
    """
    Class based view for listing and save the new admins
    permissions allowed to only authenticated admin
    
    """
    permission_classes=[permissions.AllowAny]  


    def list(self,request):
        admins  = Account.objects.all()
        serializer = BookSerializer(admins)
        return Response(serializer.data) 


    def post(self,request):
       reg_serializer=RegistrationSerializer(data=request.data)
       if reg_serializer.is_valid():

            new_user=reg_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
       return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)