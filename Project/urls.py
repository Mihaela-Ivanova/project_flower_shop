from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import order_create

urlpatterns = [
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('products/', include('products.urls')),
    path('order/', order_create, name='order_create'),
]

handler404 = 'products.views.custom_404'
handler500 = 'products.views.custom_500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


