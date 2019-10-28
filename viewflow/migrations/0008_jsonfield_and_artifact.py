# Generated by Django 3.0b1 on 2019-10-25 09:11

from django.db import migrations, models
from jsonfield_schema import JSONField
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('viewflow', '0007_task_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='artifact_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='process',
            name='artifact_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='data',
            field=JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='artifact_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='task',
            name='artifact_object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='data',
            field=JSONField(blank=True, null=True),
        ),
    ]
