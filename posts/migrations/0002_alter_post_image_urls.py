
# Generated by Django 3.2.18 on 2023-06-12 08:32


from django.db import migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_urls',
            field=posts.models.ListField(blank=True, null=True),
        ),
    ]
