# Generated by Django 4.2.1 on 2023-10-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_food_type_food_non_veg'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='a_img',
            field=models.CharField(default='https://images.pexels.com/photos/1860208/pexels-photo-1860208.jpeg?cs=srgb&dl=cooked-food-1860208.jpg&fm=jpg', max_length=1000),
        ),
        migrations.AddField(
            model_name='food',
            name='b_img',
            field=models.CharField(default='https://images.pexels.com/photos/1860208/pexels-photo-1860208.jpeg?cs=srgb&dl=cooked-food-1860208.jpg&fm=jpg', max_length=1000),
        ),
        migrations.AddField(
            model_name='food',
            name='c_img',
            field=models.CharField(default='https://images.pexels.com/photos/1860208/pexels-photo-1860208.jpeg?cs=srgb&dl=cooked-food-1860208.jpg&fm=jpg', max_length=1000),
        ),
    ]
