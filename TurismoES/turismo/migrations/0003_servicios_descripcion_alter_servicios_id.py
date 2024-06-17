# Generated by Django 5.0.6 on 2024-06-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0002_servicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
