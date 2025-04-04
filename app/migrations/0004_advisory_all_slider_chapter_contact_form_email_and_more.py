# Generated by Django 5.1.7 on 2025-04-02 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisory_name', models.CharField(max_length=100)),
                ('advisory', models.ImageField(upload_to='media/advisory/pic')),
                ('occupation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='All_Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider1_image', models.ImageField(upload_to='media/slider/images')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapters_name', models.CharField(max_length=100)),
                ('chapters_cover', models.ImageField(upload_to='media/chapters/cover')),
                ('chairman_name', models.CharField(max_length=100)),
                ('chairman_pic', models.ImageField(upload_to='media/chapters/chairman')),
                ('co_chairman_name', models.CharField(max_length=100)),
                ('co_chairman_pic', models.ImageField(upload_to='media/chapters/co_chairman')),
                ('secretary_name', models.CharField(max_length=100)),
                ('secretary_pic', models.ImageField(upload_to='media/chapters/secretary')),
                ('financial_secretary_name', models.CharField(max_length=100)),
                ('financial_secretary_pic', models.ImageField(upload_to='media/chapters/financial_secretary')),
                ('treasurer_name', models.CharField(max_length=100)),
                ('treasurer_pic', models.ImageField(upload_to='media/chapters/treasurer')),
                ('chaplain_name', models.CharField(max_length=100)),
                ('chaplain_pic', models.ImageField(upload_to='media/chapters/chaplain')),
                ('training_director_name', models.CharField(max_length=100)),
                ('training_director_pic', models.ImageField(upload_to='media/chapters/training_director')),
                ('program_director_name', models.CharField(max_length=100)),
                ('program_director_pic', models.ImageField(upload_to='media/chapters/program_director')),
                ('parliamentarian_name', models.CharField(max_length=100)),
                ('parliamentarian_pic', models.ImageField(upload_to='media/chapters/parliamentarian')),
                ('reporter_name', models.CharField(max_length=100)),
                ('reporter_pic', models.ImageField(upload_to='media/chapters/reporter')),
                ('girl_in_ict_name', models.CharField(max_length=100)),
                ('girl_in_ict_pic', models.ImageField(upload_to='media/chapters/girl_in_ict')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president', models.CharField(blank=True, max_length=100, null=True)),
                ('president_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('vic_president', models.CharField(blank=True, max_length=100, null=True)),
                ('vic_president_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('financial_secretary', models.CharField(blank=True, max_length=100, null=True)),
                ('financial_secretary_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('secretary_general', models.CharField(blank=True, max_length=100, null=True)),
                ('secretary_general_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('aLL_chapters_chairman', models.CharField(blank=True, max_length=100, null=True)),
                ('aLL_chapters_chairma_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('program_director', models.CharField(blank=True, max_length=100, null=True)),
                ('program_director_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('training_director', models.CharField(blank=True, max_length=100, null=True)),
                ('training_director_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('sa', models.CharField(blank=True, max_length=100, null=True)),
                ('sa_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('girls_in_ICTs_chairlady', models.CharField(blank=True, max_length=100, null=True)),
                ('girls_in_ICTs_chairlady_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('national_reporter', models.CharField(blank=True, max_length=100, null=True)),
                ('national_reporter_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('systems_administrator', models.CharField(blank=True, max_length=100, null=True)),
                ('systems_administrator_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('p_r_o', models.CharField(blank=True, max_length=100, null=True)),
                ('p_r_o_cover', models.ImageField(blank=True, null=True, upload_to='media/leadership/cover')),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership_From',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='media/membership/profile_pic')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('home_address', models.TextField()),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('county_of_residence', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('extra_skill', models.CharField(max_length=100)),
                ('level_of_education', models.CharField(max_length=100)),
                ('chapter_name', models.CharField(blank=True, max_length=100)),
                ('living_with', models.CharField(max_length=10)),
                ('working_or_not', models.CharField(blank=True, max_length=3)),
                ('if_yes_place_of_work', models.CharField(blank=True, max_length=100)),
                ('hear_about_us', models.CharField(max_length=100)),
                ('why_be_member', models.TextField()),
                ('emergency_first_name', models.CharField(max_length=100)),
                ('emergency_last_name', models.CharField(max_length=100)),
                ('emergency_email', models.EmailField(max_length=254)),
                ('emergency_address', models.TextField()),
                ('emergency_relationship', models.CharField(max_length=100)),
                ('accepted_membership_rules', models.BooleanField(default=False)),
                ('accepted_privacy_policy', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Presidential_info', models.CharField(max_length=100)),
                ('Presidential_image', models.ImageField(upload_to='media/Presidential/pic')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter_Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_chairman_name', models.CharField(max_length=200)),
                ('chapter_chairman_cover', models.ImageField(upload_to='media/leadership/cover')),
                ('leadership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.leaderships')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='post_images/')),
                ('category', models.CharField(blank=True, choices=[('News', 'News'), ('Announcements', 'Announcements')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
