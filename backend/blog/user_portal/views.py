from rest_framework import status
from rest_framework import response
from rest_framework import views
from rest_framework import generics


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

        auth_response = serializer.get_token(serializer.data)

        return response.Response(
            auth_response,
            status=status.HTTP_200_OK,
        )
