from django.urls import include, path
from rest_framework import routers


from .views.user import UserDetailAPIView
from .views.challenge import ChallengeViewSet

router = routers.DefaultRouter()
router.register(r"challenges", ChallengeViewSet, basename="challenge")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path(r"api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + router.urls
