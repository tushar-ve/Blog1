# Generated by Django 4.2.1 on 2023-05-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lekh', '0012_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
