# Generated by Django 3.2.5 on 2022-10-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_reviews_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
