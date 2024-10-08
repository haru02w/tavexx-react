# Generated by Django 5.1.1 on 2024-09-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=256)),
                ('tag', models.CharField(max_length=64)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo', models.CharField(choices=[('deposito', 'Deposit'), ('saque', 'Withdrawal')], max_length=10)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['data'],
            },
        ),
    ]
