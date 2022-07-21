from rest_framework.serializers import ModelSerializer

from .models import Course, Module


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'slug', 'description', 'image', 'status', 'created_at']
        # dynamically modifying fields


class ModuleSerializer(ModelSerializer):
    create_course = CourseSerializer(read_only=True, many=True)

    def to_representation(self, instance):
        children = ModuleSerializer(instance.child, many=True, read_only=True).data
        # print()
        response = super().to_representation(instance)
        # super() returns an obj that represents parent class
        response['children'] = children
        return response

    class Meta:
        model = Module
        fields = ['id', 'name', 'course_id', 'parent_id', 'create_course']
        # dynamically modifying fields
