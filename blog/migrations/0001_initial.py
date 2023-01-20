# Generated by Django 4.1.5 on 2023-01-20 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyBlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='static/blog')),
                ('thumbnail_description', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('content_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.content')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/blog')),
                ('image_description', models.CharField(max_length=200)),
                ('content_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.content')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.weeklyblogpost'),
        ),
        migrations.CreateModel(
            name='Code_S',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4000)),
                ('content_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.content')),
            ],
        ),
        migrations.CreateModel(
            name='Code_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20000)),
                ('content_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.content')),
            ],
        ),
        migrations.CreateModel(
            name='Code_L',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100000)),
                ('content_container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.content')),
            ],
        ),
    ]