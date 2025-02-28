from django.urls import include, path
from rest_framework import routers


from .views.user import UserViewSet
from .views.challenge import ChallengeViewSet

router = routers.DefaultRouter()
router.register(r"challenges", ChallengeViewSet, basename="challenge")
router.register(r"user", UserViewSet, basename="user")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + router.urls
