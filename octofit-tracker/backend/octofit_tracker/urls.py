"""octofit_tracker URL Configuration"""
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octofit_tracker.views import (
    api_root, UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')


@api_view(['GET'])
def codespace_api_root(request, format=None):
    """Return API root with Codespace-aware absolute URLs."""
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api"
    else:
        base_url = f"{request.scheme}://{request.get_host()}/api"
    return Response({
        'users': f"{base_url}/users/",
        'teams': f"{base_url}/teams/",
        'activities': f"{base_url}/activities/",
        'leaderboard': f"{base_url}/leaderboard/",
        'workouts': f"{base_url}/workouts/",
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', codespace_api_root, name='api-root'),
    path('api/', codespace_api_root, name='api-root-api'),
    path('api/', include(router.urls)),
]
