from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import EmailSerializer
from django.conf import settings

class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            recipient = serializer.validated_data['recipient']

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )

            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)