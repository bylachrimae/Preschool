# Generated by Django 4.0.5 on 2022-06-28 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_schoolclass_attending_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.CharField(max_length=2)),
                ('attending_students', models.ManyToManyField(through='main.SchoolClass', to='main.student')),
            ],
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='stu_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.studentclass'),
        ),
    ]