
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseView, ModuleView, ModuleUpdate

router = DefaultRouter()
router.register('course', CourseView)
router.register('module',ModuleView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('module-update/<id>',ModuleUpdate.as_view()),

]

