from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient = serializers.EmailField()