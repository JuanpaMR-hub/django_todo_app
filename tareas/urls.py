from django.urls import path
from rest_framework import routers
from .views import TareaViewSet



router = routers.DefaultRouter()
router.register("tareas",TareaViewSet)

urlpatterns = router.urls
