# Generated by Django 4.1.2 on 2022-10-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_post_unlisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='unlisted',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
