from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.views import APIView
from authSec.serializers import *
from .models import *
from datetime import timezone
import os

class deleteProfileImage(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request):
        try:
            data = request.data
            pk = data['user']
            user = get_object_or_404(User, pk=pk)
            if user.profile.image:
                os.remove(user.profile.image.path)
            
            user.profile.image = None
            return Response({'message': 'Profile image deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteCompetitionFile(APIView):
    permission_classes = (permissions.AllowAny, )
    def delete(self, request):
        try:
            data = request.data
            pk = data['competition']
            competition = get_object_or_404(Competitions, pk=pk)

            if competition.file:
                os.remove(competition.file.path)
            
            competition.file = None

            return Response({'message': 'Attached file deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
