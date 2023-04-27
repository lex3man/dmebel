# Generated by Django 4.2 on 2023-04-14 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500, verbose_name='Наименование')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('tg_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телеграм ID')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500, verbose_name='Наименование')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.human', verbose_name='Субъект')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.employeerole', verbose_name='Должность')),
                ('tag', models.ManyToManyField(null=True, to='data.tag', verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500, verbose_name='Наименование')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.human', verbose_name='Субъект')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.clientstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500, verbose_name='Наименование')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.human', verbose_name='Субъект')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.adminrole', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Администратор',
                'verbose_name_plural': 'Администраторы',
            },
        ),
    ]
