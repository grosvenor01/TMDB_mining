from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import requests
from social_django.utils import psa
from django.http import HttpResponse,JsonResponse
from requests.exceptions import HTTPError


@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def register_by_access_token(request, backend):
    token = request.data.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=status.HTTP_200_OK,)
    else:
        return Response({'errors': {'token': 'Invalid token'}},status=status.HTTP_400_BAD_REQUEST,)

def trend(request):
    response = requests.get("https://api.themoviedb.org/3/trending/all/week?api_key=1d027e174057ab9860ac7b1fb566fc11").json()
    return JsonResponse(response, status=200 , safe=False)
def discover(request):
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=1d027e174057ab9860ac7b1fb566fc11&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate").json()
    return JsonResponse(response, status=200 , safe=False)
def providers(request):
    response = requests.get(" https://api.themoviedb.org/3/watch/providers/regions?api_key=1d027e174057ab9860ac7b1fb566fc11&language=en-US").json()
    return JsonResponse(response, status=200 , safe=False)
