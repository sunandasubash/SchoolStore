# Generated by Django 3.1.7 on 2023-11-09 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[], default='BCA', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts'), ('History', 'History')], default='Science', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='materials_provide',
            field=models.CharField(default='Science', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='purpose',
            field=models.CharField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')], default='BCA', max_length=20),
            preserve_default=False,
        ),
    ]