


from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name=''),
    path('register/', views.register, name='register'),
    path('order/<int:id>', views.order, name='order'),
    path('product_post/', views.product_post, name='product_post'),
    path('order_list/', views.order_list, name='order_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

