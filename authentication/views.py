from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInfoSerializer
from firebase_admin import db
import json

db_ref = db.reference()

class Signup(APIView):
    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            try:
              new=db_ref.child('users').push({
                  'fname': 'John Doe',
                  'email': 'johndoe@example.com',
                  'password':'12345678'
})
              print(new.key)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"message": "Data saved successfully", "data": serializer.data,"id":new.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

