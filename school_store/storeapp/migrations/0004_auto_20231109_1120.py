# Generated by Django 3.1.7 on 2023-11-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_auto_20231109_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='materials_provide',
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('BBA', 'BBA'), ('BCom', 'BCom')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts'), ('History', 'History')], max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='materials_provided',
            field=models.ManyToManyField(blank=True, to='storeapp.Material'),
        ),
    ]
