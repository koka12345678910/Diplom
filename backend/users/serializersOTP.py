from rest_framework import serializers

class OTPRequestSerializer(serializers.Serializer):
    telegram_id = serializers.CharField(max_length=64)
