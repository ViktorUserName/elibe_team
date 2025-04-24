from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import serializers

from author import serializers
from .serializers import CustomUserSerializer, UserReadSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #
    #     refresh = RefreshToken.for_user(user)
    #     access = refresh.access_token
    #
    #     return Response({
    #         "user": {
    #             "id": user.id,
    #             "username": user.username,
    #             "email": user.email,
    #             "role": user.role,
    #         },
    #         "tokens": {
    #             "refresh": str(refresh),
    #             "access": str(access),
    #         }
    #     }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UserReadSerializer(request.user)
            # serializer = CustomUserSerializer(request.user)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)