from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer


class ProfileCreateUpdateView(APIView):
    permission_classes = [IsAuthenticated]  #allow only authenticated user
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():  # validate data
            serializer.save(user = request.user)  # save data with current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            profile = Profile.objects.get(user=request.user)  # fetch profile
        except Profile.DoesNotExist:
            return Response("Profile does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)  # partially validate 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

