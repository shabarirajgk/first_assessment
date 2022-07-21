# Generated by Django 4.0.6 on 2022-07-21 10:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('course_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_course', to='test_app.course')),
                ('parent_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='test_app.module')),
            ],
        ),
    ]