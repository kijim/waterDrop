# Generated by Django 2.1.1 on 2018-09-17 03:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': '社員情報',
                'verbose_name': '社員情報',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BuTable',
            fields=[
                ('buCode', models.AutoField(help_text='部コードを入力してください(0001など)', primary_key=True, serialize=False, verbose_name='部コード')),
                ('name', models.CharField(help_text='部名を入力してください', max_length=32, verbose_name='部名')),
            ],
            options={
                'verbose_name_plural': '部門情報',
                'verbose_name': '部門情報',
            },
        ),
        migrations.CreateModel(
            name='CalendarTable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KaTable',
            fields=[
                ('kaCode', models.AutoField(help_text='課コードを入力してください(0001など)', primary_key=True, serialize=False, verbose_name='課コード')),
                ('name', models.CharField(help_text='課名を入力してくっださい', max_length=32, verbose_name='課名')),
                ('buCode', models.ForeignKey(help_text='課が所属する部コードを選択してください', on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.BuTable', verbose_name='所属部門')),
            ],
            options={
                'verbose_name_plural': '課情報',
                'verbose_name': '課情報',
            },
        ),
        migrations.CreateModel(
            name='KubunTable',
            fields=[
                ('kubunid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('div', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MeisaiTable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('calendar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.CalendarTable')),
                ('employ_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('tanka_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('tanka', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeCardTable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('employ_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkCodeTable',
            fields=[
                ('work_code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDetailCodeTable',
            fields=[
                ('work_detail_code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('work_time', models.FloatField()),
                ('time_card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.TimeCardTable')),
                ('work_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.WorkCodeTable')),
                ('work_detail_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.WorkDetailCodeTable')),
            ],
        ),
        migrations.AddField(
            model_name='meisaitable',
            name='tana_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.PriceTable'),
        ),
        migrations.AddField(
            model_name='calendartable',
            name='kubunid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.KubunTable'),
        ),
        migrations.AddField(
            model_name='user',
            name='kaCode',
            field=models.ForeignKey(help_text='所属課を選択してください', null=True, on_delete=django.db.models.deletion.CASCADE, to='waterDropApp.KaTable', verbose_name='課コード'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]