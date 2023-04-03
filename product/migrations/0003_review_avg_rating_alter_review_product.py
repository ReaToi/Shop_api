# Generated by Django 4.1.7 on 2023-04-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review_stars_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_rating',
            field=models.IntegerField(default=models.IntegerField(choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=5)),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='review_list', to='product.product'),
        ),
    ]