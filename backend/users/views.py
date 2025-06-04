from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()


class RegisterView(APIView):
    @extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя на основе email, username и пароля.",
        request=UserRegistrationSerializer,
        responses={
            201: OpenApiResponse(description="Пользователь успешно зарегистрирован"),
            400: OpenApiResponse(description="Ошибка валидации")
        }
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь успешно зарегистрирован"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @extend_schema(
        summary="Вход в систему",
        description="Аутентификация пользователя по email и паролю. Возвращает JWT токены.",
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(description="Успешный вход"),
            401: OpenApiResponse(description="Неверные учетные данные")
        }
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Профиль пользователя",
        description="Возвращает информацию об аутентифицированном пользователе.",
        responses={
            200: OpenApiResponse(description="Данные профиля"),
            403: OpenApiResponse(description="Неавторизованный доступ")
        }
    )
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })
