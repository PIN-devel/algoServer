from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, create_round, get_or_patch_round

router = routers.DefaultRouter()
router.register('', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:group_id>/rounds/', create_round),
    path('rounds/<int:round_id>/', get_or_patch_round)
]
