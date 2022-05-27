# Generated by Django 4.0.4 on 2022-05-11 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ContryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('peragraph', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Extractdata.category')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Extractdata.contrydetails')),
            ],
        ),
    ]