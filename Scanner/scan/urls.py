from django.contrib import admin
# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import hotel_image_view,success,HomePageView,CreatePostView,create_image_set_view,image_set_detail_view

# urlpatterns = [
    # path('', hotel_image_view, name='image_upload'),
    # path('success', success, name='success'),
    # path("hotel/", HomePageView.as_view(), name="hotel"),
    # path("post/", CreatePostView.as_view(), name="add_post") ,

    #  path('create-image-set/', create_image_set_view, name='create_image_set'),
    # path('image-set/<uuid:pk>/', image_set_detail_view, name='image_set_detail'),

    # path('hotel/<int:pk>/edit/', edit_hotel_view, name='hotel_edit'),
    # path('hotel/<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),
# ]

from django.urls import path
from .views import list_users_view, user_detail_view, success,create_user_view

urlpatterns = [
    path('', list_users_view, name='list_users'),
    path('create/', create_user_view, name='create_user'),

    path('user/<uuid:pk>/', user_detail_view, name='user_detail'),
    path('success/', success, name='success'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)