# Generated by Django 4.2.1 on 2023-10-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_food_a_img_food_b_img_food_c_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='a_img',
            field=models.CharField(default='Image 1 link', max_length=1000),
        ),
        migrations.AlterField(
            model_name='food',
            name='b_img',
            field=models.CharField(default='Image 2 link', max_length=1000),
        ),
        migrations.AlterField(
            model_name='food',
            name='c_img',
            field=models.CharField(default='Image 3 link', max_length=1000),
        ),
    ]