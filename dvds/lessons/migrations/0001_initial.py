# Generated by Django 4.2.9 on 2024-02-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FranchiseFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Franchise Fee',
            },
        ),
        migrations.CreateModel(
            name='LessonPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_hourly', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('manual_block', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('manual_refresher', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('automatic_hourly', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('automatic_block', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('automatic_refresher', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_ten', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_fifteen', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_twenty', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_twentyfive', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_thirty', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_thirtyfive', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_fourty', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('intensive_fourtyfive', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Lesson Pricing',
                'verbose_name_plural': 'Lesson Pricing',
            },
        ),
    ]
