# Generated by Django 2.2.24 on 2021-09-17 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0049_sponsoremailnotificationtemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTargetable',
            fields=[
                ('benefitfeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sponsors.BenefitFeature')),
            ],
            options={
                'verbose_name': 'Email Targetable Benefit',
                'verbose_name_plural': 'Email Targetable Benefits',
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('sponsors.benefitfeature', models.Model),
        ),
        migrations.CreateModel(
            name='EmailTargetableConfiguration',
            fields=[
                ('benefitfeatureconfiguration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sponsors.BenefitFeatureConfiguration')),
            ],
            options={
                'verbose_name': 'Email Targetable Configuration',
                'verbose_name_plural': 'Email Targetable Configurations',
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('sponsors.benefitfeatureconfiguration', models.Model),
        ),
    ]
