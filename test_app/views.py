from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .utlis import COURSE_SOFT_DELETED
from .models import Course, Module
from .serializers import CourseSerializer, ModuleSerializer


class CourseView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # describe all the objects in the db


class CourseUpdate(APIView):
    # soft delete course
    def get(self, request, id=None):
        if id:
            item = Course.objects.get(id=id)
            serializer = CourseSerializer(item)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

        items = Course.objects.exclude(status=COURSE_SOFT_DELETED)
        serializer = CourseSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        try:
            create_course = Course.objects.get(id=id)
            create_course.status = COURSE_SOFT_DELETED
            create_course.save()
            return Response({"detail": " Deleted Successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ModuleView(ModelViewSet):
    serializer_class = ModuleSerializer
    # get super parent  modules - ie. course  which having parent_id None
    queryset = Module.objects.filter(parent_id=None).all()
    # parent_id which is none - it will take it as super parent


@api_view(['GET', 'POST'])
def create_module(request, self=None):
    serializer = ModuleSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        last_position = Module.objects.order_by('-position').first()
        if last_position:
            new_position = last_position.position + 1
        else:
            new_position = 1

        name = request.data.get('name')
        description = request.data.get('description')
        position = new_position

        module_instance = Module.objects.create(
            name=name,
            description=description,
            position=position,
        )

        response = {
            "id": module_instance.id,
            "name": module_instance.name,
            "description": module_instance.description,

        }

        return Response(response, status.HTTP_200_OK)


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
