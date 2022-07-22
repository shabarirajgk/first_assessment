
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseView, ModuleView, ModuleUpdate, CourseUpdate, create_module

router = DefaultRouter()
router.register('course', CourseView)
router.register('module',ModuleView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('module-update/',ModuleUpdate.as_view()),
    path('module-update/<id>',ModuleUpdate.as_view()),
    path('course-update', CourseUpdate.as_view()),
    path('course-update/<id>',CourseUpdate.as_view()),
    path('api/create_module', create_module),

]

