# Generated by Django 4.1.7 on 2023-04-02 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review_avg_rating_alter_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='avg_rating',
        ),
    ]
