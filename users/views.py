from rest_framework import permissions, request, response, status, views
from rest_framework_simplejwt import authentication

from users.models import CustomUser
from users.serializers import UserProfileSerializer


class UserProfileAPIView(views.APIView):
    """Get users profile"""

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    authentication_classes = (authentication.JWTAuthentication,)

    def get(
        self, request: request.Request, *args: tuple, **kwargs: dict
    ) -> response.Response:
        user: CustomUser = request.user
        serializer = self.serializer_class(user)

        return response.Response(serializer.data, status=status.HTTP_200_OK)
