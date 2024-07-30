from django.contrib import admin
# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import hotel_image_view,success,HomePageView,CreatePostView,create_image_set_view,image_set_detail_view



from django.urls import path
from .views import list_users_view, user_detail_view, success,create_user_view,login,welcome,main ,logadm  ,user_view  ,logout ,delete_image

urlpatterns = [
    path('list_users/', list_users_view, name='list_users'),
    path('create/', create_user_view, name='create_user'),

    path('user/<uuid:pk>/', user_detail_view, name='user_detail'),
    path('success/', success, name='success'),
    path('login/', login, name='login'),
    path('welcome/<str:user_id>/', welcome, name='welcome'),
    path('', main, name='main'),
    path('logadm/', logadm, name='logadm'),

    path('user_view/<uuid:pk>', user_view,name='user_view'),
    path('logout/', logout, name='logout'),
    path('delete-image/<int:image_id>/', delete_image, name='delete_image')
    # path('user/<int:pk>/delete-image/', delete_image_view, name='delete_image'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)