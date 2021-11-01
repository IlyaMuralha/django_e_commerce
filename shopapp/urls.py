from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),

    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.remove_cart, name='remove_cart'),
    path('cart/remove_product/<int:product_id>', views.remove_product, name='remove_product'),

    path('account/create/', views.sing_up_view, name='signup'),
    path('account/singin/', views.sing_in_view, name='signin'),
    path('account/signout/', views.sign_out_view, name='signout'),
]
