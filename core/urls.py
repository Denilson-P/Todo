from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TaskViewSet

router = SimpleRouter()
router.register("user", UserViewSet, basename="user")
router.register("task", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls))
]