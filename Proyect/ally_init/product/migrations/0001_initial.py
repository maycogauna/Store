# Generated by Django 3.1.7 on 2021-07-13 02:39

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'db_table': 'categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='producto/')),
                ('excerpt', models.TextField(max_length=200, verbose_name='Extracto')),
                ('detail', models.TextField(max_length=1000, verbose_name='informacion del producto')),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'producto',
                'ordering': ['id'],
            },
        ),
    ]
