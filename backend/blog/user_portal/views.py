from rest_framework import status
from rest_framework import response
from rest_framework import views
from rest_framework import generics
from rest_framework import exceptions
from rest_framework_simplejwt import tokens
from rest_framework_simplejwt import exceptions as jwt_exceptions


from user_portal import serializers


class RegistrationView(views.APIView):
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)

        if serializer.is_valid() is False:
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return response.Response(
            {"message": "Success"},
            status=status.HTTP_201_CREATED,
        )


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid() is False:
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            auth_response = serializer.get_token(serializer.data)
        except exceptions.ValidationError as e:
            return response.Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(
            auth_response,
            status=status.HTTP_200_OK,
        )

class ValidateTokenView(views.APIView):
    def post(self, request):
        token = request.data.get("token")

        print("here comes the token :", token)
        if token is None:
            return response.Response(
                {"valid": False, "error": "No token provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token_obj = tokens.AccessToken(token)
            user = token_obj.payload.get("user_id")

            return response.Response(
                {
                    "valid": True,
                    "user_id": user,
                    "status_code": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK
            )
        except jwt_exceptions.TokenError:
            return response.Response(
                {"valid": False, "error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )