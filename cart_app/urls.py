from django.urls import path
from.import views

urlpatterns=[
    path('cart_details',views.cart_details,name='cart_details'),
    path('add/<int:product_id>/',views.add_cart,name='addcart')
]