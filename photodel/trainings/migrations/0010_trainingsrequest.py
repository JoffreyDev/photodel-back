# Generated by Django 3.2.7 on 2023-01-29 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20230118_0220'),
        ('trainings', '0009_trainings_training_orgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.trainings')),
            ],
        ),
    ]