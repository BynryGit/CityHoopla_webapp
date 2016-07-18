# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 10:01
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalAmenities',
            fields=[
                ('extra_amenity_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('extra_amenity', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('advert_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=150, null=True)),
                ('advert_name', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('short_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('product_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('discount_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('product_price', models.CharField(blank=True, max_length=50, null=True)),
                ('display_image', models.FileField(blank=True, max_length=500, null=True, upload_to=b'images/user_images/')),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('landmark', models.CharField(blank=True, max_length=50, null=True)),
                ('email_primary', models.CharField(blank=True, max_length=50, null=True)),
                ('email_secondary', models.CharField(blank=True, max_length=50, null=True)),
                ('property_market_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('possesion_status', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_delivery', models.CharField(blank=True, max_length=50, null=True)),
                ('any_other_details', models.CharField(blank=True, max_length=5000, null=True)),
                ('distance_frm_railway_station', models.CharField(blank=True, max_length=50, null=True)),
                ('distance_frm_railway_airport', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advert_Category_Map',
            fields=[
                ('adv_cat_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('category_level', models.CharField(blank=True, max_length=30, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='Advert_Video',
            fields=[
                ('advert_video_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('advert_video_name', models.FileField(blank=True, max_length=500, null=True, upload_to=b'images/user_images/')),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advert_videos', to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('advert_image_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('advert_image', models.FileField(blank=True, max_length=500, null=True, upload_to=b'images/user_images/')),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertLike',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertRateCard',
            fields=[
                ('advert_rate_card_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('advert_service_name', models.CharField(max_length=30)),
                ('duration', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.CharField(blank=True, max_length=30, null=True)),
                ('advert_rate_card_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('advert_rate_card_created_date', models.DateTimeField(blank=True, null=True)),
                ('advert_rate_card_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('advert_rate_card_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('advert_rate_card_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertSubscriptionMap',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('amenity_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('amenity', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('duration', models.CharField(max_length=30)),
                ('transaction_code', models.CharField(blank=True, max_length=30, null=True)),
                ('start_date', models.CharField(blank=True, max_length=30, null=True)),
                ('end_date', models.CharField(blank=True, max_length=30, null=True)),
                ('business_created_date', models.DateTimeField(blank=True, null=True)),
                ('business_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('business_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('business_updated_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
                ('category_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('category_created_date', models.DateTimeField(blank=True, null=True)),
                ('category_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('category_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('category_updated_date', models.DateTimeField(blank=True, null=True)),
                ('level', models.CharField(blank=True, max_length=30, null=True)),
                ('has_category', models.ForeignKey(blank=b'True', null=b'True', on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCityMap',
            fields=[
                ('map_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('sequence', models.CharField(blank=True, max_length=500, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('city_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City_Place',
            fields=[
                ('city_place_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('about_city', models.CharField(blank=True, max_length=1000, null=True)),
                ('city_image', models.FileField(blank=True, max_length=500, null=True, upload_to=b'images/user_images/')),
                ('climate', models.CharField(blank=True, max_length=500, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('population', models.CharField(blank=True, max_length=100, null=True)),
                ('time_zone', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('city_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=10, null=True)),
                ('city_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='Consumer_Feedback',
            fields=[
                ('feedback_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('consumer_feedback', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('consumer_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('consumer_full_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('consumer_contact_no', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('consumer_email_id', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('consumer_status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=100, null=True)),
                ('consumer_created_date', models.DateTimeField(blank=True, null=True)),
                ('consumer_created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('consumer_updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('consumer_updated_date', models.DateTimeField(blank=True, null=True)),
                ('sign_up_source', models.CharField(blank=True, max_length=20, null=True)),
                ('consumer_profile_pic', models.ImageField(default=None, max_length=500, upload_to=b'images/user_images/', verbose_name=b'Image')),
                ('device_token', models.CharField(blank=True, max_length=20, null=True)),
                ('online', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=100, null=True)),
                ('last_time_login', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('coupon_code', models.CharField(blank=True, max_length=20, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.ConsumerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('currency', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=None, max_length=150, null=True)),
                ('Currency_created_by', models.CharField(max_length=150, null=True)),
                ('Currency_created_date', models.DateTimeField(null=True)),
                ('Currency_updated_by', models.CharField(max_length=150, null=True)),
                ('Currency_updated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NearByAttraction',
            fields=[
                ('attraction_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('attraction', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='NearestHospital',
            fields=[
                ('hospital_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(blank=True, max_length=50, null=True)),
                ('distance_frm_property', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='NearestSchool',
            fields=[
                ('school_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=50, null=True)),
                ('distance_frm_property', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='NearestShopping',
            fields=[
                ('shopping_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('shop_name', models.CharField(blank=True, max_length=50, null=True)),
                ('distance_frm_property', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('payment_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('payment_code', models.CharField(max_length=30)),
                ('payment_mode', models.CharField(max_length=30)),
                ('paid_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('payable_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('payment_created_date', models.DateTimeField(blank=True, null=True)),
                ('payment_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('payment_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('payment_updated_date', models.DateTimeField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=30, null=True)),
                ('business_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Business')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCategory',
            fields=[
                ('phone_category_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('phone_category_name', models.CharField(max_length=15)),
                ('phone_category_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('phone_category_created_date', models.DateTimeField(blank=True, null=True)),
                ('phone_category_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_category_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_category_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNo',
            fields=[
                ('phone_no_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
                ('phone_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.PhoneCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('pincode_id', models.AutoField(primary_key=True, serialize=False)),
                ('pincode', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('created_by', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('updated_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_by', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('pincode_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=10, null=True)),
                ('city_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('place_name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('place_image', models.FileField(blank=True, max_length=500, null=True, upload_to=b'images/user_images/')),
                ('place_type', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('created_by', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('updated_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_by', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('city_place_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City_Place')),
            ],
        ),
        migrations.CreateModel(
            name='PremiumService',
            fields=[
                ('premium_service_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('premium_service_name', models.CharField(max_length=30)),
                ('no_of_days', models.CharField(max_length=30)),
                ('start_date', models.CharField(blank=True, max_length=30, null=True)),
                ('end_date', models.CharField(blank=True, max_length=30, null=True)),
                ('premium_service_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('premium_service_created_date', models.DateTimeField(blank=True, null=True)),
                ('premium_service_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('premium_service_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('premium_service_updated_date', models.DateTimeField(blank=True, null=True)),
                ('business_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Business')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRateCard',
            fields=[
                ('service_rate_card_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=30)),
                ('duration', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.CharField(blank=True, max_length=30, null=True)),
                ('service_rate_card_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('service_rate_card_created_date', models.DateTimeField(blank=True, null=True)),
                ('service_rate_card_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('service_rate_card_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('service_rate_card_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=500, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('state_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('supplier_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('business_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('phone_no', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('secondary_phone_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('supplier_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('secondary_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, default=None, null=True, upload_to=b'images/user_images/')),
                ('address1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('business_details', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('contact_person', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contact_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('supplier_status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=100, null=True)),
                ('supplier_created_date', models.DateTimeField(blank=True, null=True)),
                ('supplier_created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('supplier_updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('supplier_updated_date', models.DateTimeField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City')),
                ('pincode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Pincode')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.State')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('tax_type', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('tax_rate', models.IntegerField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user_contact_no', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('usre_email_id', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user_status', models.CharField(choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=100, null=True)),
                ('user_created_date', models.DateTimeField(blank=True, null=True)),
                ('user_created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('role_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=25)),
                ('role_status', models.CharField(blank=True, choices=[(b'1', b'1'), (b'0', b'0')], default=b'1', max_length=15, null=True)),
                ('role_created_date', models.DateTimeField(blank=True, null=True)),
                ('role_created_by', models.CharField(blank=True, max_length=30, null=True)),
                ('role_updated_by', models.CharField(blank=True, max_length=30, null=True)),
                ('role_updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('working_hr_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('day', models.CharField(blank=True, max_length=50, null=True)),
                ('start_time', models.CharField(blank=True, max_length=50, null=True)),
                ('end_time', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=500, null=True)),
                ('updation_date', models.DateTimeField(blank=True, null=True)),
                ('advert_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Advert')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.UserRole'),
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='tax_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Tax'),
        ),
        migrations.AddField(
            model_name='consumer_feedback',
            name='consumer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.ConsumerProfile'),
        ),
        migrations.AddField(
            model_name='city_place',
            name='state_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.State'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.State'),
        ),
        migrations.AddField(
            model_name='categorycitymap',
            name='city_place_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City_Place'),
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Category'),
        ),
        migrations.AddField(
            model_name='business',
            name='service_rate_card_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.ServiceRateCard'),
        ),
        migrations.AddField(
            model_name='business',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Supplier'),
        ),
        migrations.AddField(
            model_name='advertsubscriptionmap',
            name='business_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Business'),
        ),
        migrations.AddField(
            model_name='advertlike',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.ConsumerProfile'),
        ),
        migrations.AddField(
            model_name='advert_category_map',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Category'),
        ),
        migrations.AddField(
            model_name='advert',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Category'),
        ),
        migrations.AddField(
            model_name='advert',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.City'),
        ),
        migrations.AddField(
            model_name='advert',
            name='currency_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Currency'),
        ),
        migrations.AddField(
            model_name='advert',
            name='pincode_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Pincode'),
        ),
        migrations.AddField(
            model_name='advert',
            name='state_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.State'),
        ),
        migrations.AddField(
            model_name='advert',
            name='supplier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digispaceapp.Supplier'),
        ),
        migrations.AddField(
            model_name='additionalamenities',
            name='advert_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add_ame', to='digispaceapp.Advert'),
        ),
    ]
