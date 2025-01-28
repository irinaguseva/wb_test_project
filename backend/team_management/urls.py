from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import CreatorViewSet, TeamViewSet, MemberViewSet, TeamApplicationViewSet


router = DefaultRouter()
router.register(r'creators', CreatorViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'members', MemberViewSet)
router.register(r'applications', TeamApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
