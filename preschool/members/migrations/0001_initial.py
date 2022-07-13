# Generated by Django 4.0.5 on 2022-06-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('address', models.CharField(blank=True, default='Your Address', max_length=300, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, default='Your Phone Number', max_length=40, null=True, verbose_name='Phone')),
                ('mobile_phone', models.CharField(blank=True, default='Your Mobile Phone Number', max_length=40, null=True, verbose_name='Mobile Number')),
                ('member_pic', models.ImageField(default='images/default_pic.jpg', upload_to='images/', verbose_name='Profile Picture')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
