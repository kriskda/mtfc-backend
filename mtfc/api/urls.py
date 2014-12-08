from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'matches', views.MatchViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]