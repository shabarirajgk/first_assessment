from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Course, Module
from .serializers import CourseSerializer, ModuleSerializer


class CourseView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # describe all the objects in the db

# class CourseUpdate(APIView):
#     def delete(self, request, id=None):
#         try:
#             create_course = Course.objects.get(id=id)
#             if create_course.type ==
#                 create_course.status =
#                 create_course.save()
#                 return Response({"detail": "Case Deleted Successfully"}, status=status.HTTP_200_OK)


class ModuleView(ModelViewSet):
    serializer_class = ModuleSerializer
    # get super parent  modules - ie. course  which having parent_id None
    queryset = Module.objects.filter(parent_id=None).all()
    # parent_id which is none - it will take it as super parent


class ModuleUpdate(APIView):
    # to update and delete the module
    def patch(self, request, id=None):
        item = Module.objects.get(id=id)
        serializer = ModuleSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            # if the serializer is valid it will save
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Module, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})