from django.urls import include, path
from rest_framework import routers

from .views import ChallengesListAPIView,    \
                    ChallengesDetailAPIView, \
                    ParticipantsListAPIView, \
                    SubmissionsListAPIView,  \
                    UserDetailAPIView

router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"challenges/<int:pk>/participants", ParticipantsListAPIView.as_view(), name='challenge-participants'),
    path(r"challenges/<int:pk>/submissions", SubmissionsListAPIView.as_view(), name='challenge-submissions'),
    path(r"challenges/<int:pk>/", ChallengesDetailAPIView.as_view(), name='challenge-detail'),
    path(r"challenges/", ChallengesListAPIView.as_view(), name='challenge'),
    path(r"users/<int:pk>/", UserDetailAPIView.as_view(), name='user-detail'),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]