from django.shortcuts import render

# Create your views here.

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from fardaapp.serializers import UserInfoSerializer


class UserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=UserInfoSerializer, tags=["User Order"])
    def post(self, request):
        serializer = UserInfoSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(
            {"message": serializer.errors["message"][0], "status": False},
            status=status.HTTP_400_BAD_REQUEST,
        )
