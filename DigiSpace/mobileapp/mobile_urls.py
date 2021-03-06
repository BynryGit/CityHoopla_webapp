from django.conf.urls import patterns, include, url
from django.contrib import admin
from digispaceapp import views
from django.conf.urls.static import static
from DigiSpace import settings

#from django.views.generic import direct_to_template
from django.views.generic import TemplateView
mobileapp_urlpattern = patterns('',
    # Examples:
    # url(r'^$', 'DigiSpace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'mobileapp.views.consumer_signup',name='signup'),
    url(r'^social-signup/', 'mobileapp.views.social_signup',name='social_signup'),
    url(r'^consumer-login/', 'mobileapp.views.consumer_login',name='login'),
    url(r'^forget-password/', 'mobileapp.views.forgot_password',name='forget-password'),
    url(r'^get-city-list/', 'mobileapp.views.get_city_list',name='get_city_list'),
    url(r'^get-category-list/', 'mobileapp.views.get_category_list',name='get_category_list'),
    url(r'^get-advert-details/', 'mobileapp.views.get_advert_details',name='get_advert_details'),
    url(r'^get-advert-list/', 'mobileapp.views.get_advert_list',name='get_advert_list'),
    url(r'^get-coupon-code/', 'mobileapp.views.get_coupon_code',name='get_coupon_code'),
    url(r'^get-discount-details/', 'mobileapp.views.get_discount_details',name='get_discount_details'),
    url(r'^get-active-discount-details/', 'mobileapp.views.get_active_discount_details',name='get_active_discount_details'),
    url(r'^edit-customer-profile/', 'mobileapp.views.edit_customer_profile',name='edit_customer_profile'),
    url(r'^send-feedback/', 'mobileapp.views.consumer_feedback',name='send_feedback'),
    url(r'^update-device-token/', 'mobileapp.views.update_device_token',name='update_device_token'),
    url(r'^update-profile-photo/', 'mobileapp.views.update_profile_photo',name='update-profile-photo'),
    url(r'^like-advert/', 'mobileapp.views.like_advert',name='like_advert'),
    url(r'^search-advert/', 'mobileapp.views.search_advert',name='search_advert'),
    url(r'^get-category/', 'mobileapp.views.get_category',name='get_category'),
    url(r'^user-logout/', 'mobileapp.views.user_logout',name='user_logout'),
   

) + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
