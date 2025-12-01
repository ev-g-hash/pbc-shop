# shop/urls.py
"""
URL configuration for shop project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from main_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('aboutas/', views.aboutas, name='aboutas'),
    path('readmore/', views.readmore, name='readmore'),
    path('forms/', views.forms, name='forms'),
    path('order-product/', views.order_product, name='order_product'),
    path('goods/', include('goods.urls', namespace='goods')),
]

# Добавляем обработку статических и медиа файлов для development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Для production - обслуживаем файлы напрямую
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]