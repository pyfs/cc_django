# Generated by Django 2.2.14 on 2021-03-05 01:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='KvTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新')),
                ('key', models.CharField(max_length=100, verbose_name='键')),
                ('value', models.CharField(blank=True, max_length=100, null=True, verbose_name='值')),
            ],
            options={
                'verbose_name': '- 键值标签',
                'verbose_name_plural': '- 键值标签',
                'unique_together': {('key', 'value')},
            },
        ),
        migrations.CreateModel(
            name='UUIDTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField(db_index=True, verbose_name='对象')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='模型')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kvtags.KvTag', verbose_name='标签')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
