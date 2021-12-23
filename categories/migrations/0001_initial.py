# Generated by Django 4.0 on 2021-12-23 11:08

import categories.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', categories.models.LCharField(max_length=50)),
                ('color', models.CharField(default='#000000', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='accounts.user')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), django.db.models.expressions.F('owner'), name='unique_category_name_owner'),
        ),
    ]
