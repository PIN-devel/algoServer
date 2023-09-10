from django.urls import path, include
from rest_framework import routers

from .views import ProblemViewSet

router = routers.DefaultRouter()
router.register(r'', ProblemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
