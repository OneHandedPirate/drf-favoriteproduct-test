from collections.abc import Mapping
from typing import Any

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def base_exception_handler(
    exc: Exception,
    context: Mapping[str, Any],
) -> Response | None:
    response = exception_handler(exc, context)

    if response is not None:
        match response.status_code:
            case status.HTTP_403_FORBIDDEN:
                response.data = {
                    "detail": "You don't have permission to perform this action",
                }
            case status.HTTP_401_UNAUTHORIZED:
                response.data = {
                    "detail": "This action is forbidden for unauthorized users",
                }
            case _:
                pass

    return response
