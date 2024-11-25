import jwt
from django.urls import reverse
from django.conf import settings
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import ContractUser
from ..serializers import ContractUserSerializer
from ..utils import send_activation_email


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ContractUserSerializer

    def create(self, request, *args, **kwargs):
        # create user & send email to verify account
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = ContractUser.objects.get(username=serializer.data["username"])
        send_activation_email(user, request.build_absolute_uri)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # user verification
        token = request.GET.get("token")
        if token is not None:
            try:
                data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
                user = ContractUser.objects.get(id=data["user_id"])
                user.is_active = True
                user.save()
                return Response(
                    {"detail": "Account activated"}, status=status.HTTP_200_OK
                )
            except jwt.ExpiredSignatureError:
                return Response(
                    {"error": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST
                )
            except jwt.PyJWTError:
                return Response(
                    {"error": "Unknown error"}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response({"error": "No token"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="resend-email")
    def resend_email(self, request):
        # api/user/resend-email/ to resend activation email
        username = request.data["username"]
        if username is not None:
            user = ContractUser.objects.filter(username=username).first()
            if user is not None:
                send_activation_email(user, request.build_absolute_uri)
                return Response({"detail": "Email sent"}, status=status.HTTP_200_OK)
            return Response(
                {"error": "No user with the username"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
