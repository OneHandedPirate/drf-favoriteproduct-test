from rest_framework import permissions, request, response, status, views


class CheckStatusAPIView(views.APIView):
    """App healthcheck endpoint"""

    permission_classes = (permissions.AllowAny,)

    def get(
        self,
        request: request.Request,
        *args: tuple,
        **kwargs: dict,
    ) -> response.Response:
        return response.Response({"status": "OK"}, status=status.HTTP_200_OK)
