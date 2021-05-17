from rest_framework import status
from rest_framework.response import Response
from datetime import datetime


def set_cookie_response(tokens):
    response = Response({"access": tokens["access"]}, status=status.HTTP_200_OK)
    response.set_cookie('refresh', tokens["refresh"], httponly=True)
    return response
