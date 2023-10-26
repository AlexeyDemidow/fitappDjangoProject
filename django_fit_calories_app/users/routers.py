from rest_framework import routers

from .API_views import AllProfileAPIViewSet, ProfileAPIViewSet, WeighingAPIViewSet

admin_profiles_edit_router = routers.SimpleRouter()
admin_profiles_edit_router.register(r'admin_profiles_edit', AllProfileAPIViewSet)

profile_router = routers.SimpleRouter()
profile_router.register(r'profile', ProfileAPIViewSet, basename='profile')

weighing_router = routers.SimpleRouter()
weighing_router.register(r'weighing', WeighingAPIViewSet, basename='weighing')