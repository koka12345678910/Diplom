import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, OTPRequest
from .serializersOTP import OTPRequestSerializer


class RequestOTPView(APIView):
    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        telegram_id = serializer.validated_data['telegram_id']

        user, _ = User.objects.get_or_create(telegram_id=telegram_id, defaults={
            'username': f"user_{telegram_id}",
            'email': f"{telegram_id}@mangalib.fake"
        })

        code = str(random.randint(100000, 999999))
        OTPRequest.objects.update_or_create(
            user=user,
            defaults={'code': code, 'created_at': timezone.now(), 'verified': False}
        )

        return Response({"detail": "Код отправлен в Telegram"}, status=200)

class VerifyOTPView(APIView):
    def post(self, request):
        telegram_id = request.data.get('telegram_id')
        code = request.data.get('code')

        try:
            user = User.objects.get(telegram_id=telegram_id)
            otp = OTPRequest.objects.get(user=user)

            if otp.code != code:
                return Response({'detail': 'Неверный код'}, status=400)

            if otp.verified:
                return Response({'detail': 'Код уже подтвержден'}, status=400)

            otp.verified = True
            otp.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=404)
        except OTPRequest.DoesNotExist:
            return Response({'detail': 'Код не запрашивался'}, status=404)