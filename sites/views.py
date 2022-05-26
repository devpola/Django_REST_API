from django.shortcuts import render
from rest_framework.response import Response
from .models import Site
from rest_framework.views import APIView, status
from .serializers import SiteSerializer


class SiteAPI(APIView):
    def get(self, request, mode):
        sites = Site.objects.filter(mode=mode)
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)