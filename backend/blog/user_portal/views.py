from rest_framework import status
from rest_framework import response
from rest_framework import views


from user_portal import serializers


class RegistrationView(views.APIView):
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)

        if serializer.is_valid() is True:
            user = serializer.save()
            return response.Response(
                {"message": "User registered successfully", "user_id": user.id},
                status=status.HTTP_201_CREATED,
            )

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
