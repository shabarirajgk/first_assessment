import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from django.db.models.functions import datetime


# Create your models here.
# create course

class Course(models.Model):
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid.uuid4)
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    image = models.ImageField(blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=["png", "jpg"])])
    # allowed extensions only allows selected files
    status = models.BooleanField(default=False)
    # position = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # shows created date
    updated_at = models.DateTimeField(auto_now=True)  # shows updated date


# create module
class Module(models.Model):
    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid.uuid4)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    course_id = models.ForeignKey(Course, related_name='create_course', on_delete=models.SET_NULL, null=True,
                                  default=None)
    # foreign key - link b/w  tables, it refers primary key to another table
    parent_id = models.ForeignKey('self', related_name='child', on_delete=models.CASCADE, null=True,
                                  default=None)
