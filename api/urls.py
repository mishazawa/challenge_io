from django.urls import include, path
from rest_framework import routers


from .views.user import UserViewSet
from .views.challenge import ChallengeViewSet
from .views.submission import SubmissionViewSet

router = routers.DefaultRouter()
router.register(r"challenge", ChallengeViewSet, basename="challenge")
router.register(r"user", UserViewSet, basename="user")
router.register(r"submission", SubmissionViewSet, basename="submission")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + router.urls
