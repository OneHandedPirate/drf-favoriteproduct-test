from django.urls import path

from base.views import CheckStatusAPIView

urlpatterns = [path("healthcheck/", CheckStatusAPIView.as_view(), name="healthcheck")]
