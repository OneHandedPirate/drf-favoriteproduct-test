from drf_spectacular.utils import OpenApiExample, OpenApiTypes, extend_schema
from rest_framework import permissions, request, response, status, views


@extend_schema(
    responses=OpenApiTypes.OBJECT,
    examples=[
        OpenApiExample(name="Success", value={"status": "OK"}, response_only=True)
    ],
)
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
