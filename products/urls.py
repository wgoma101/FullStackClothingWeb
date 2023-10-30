from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="home"),#home page
    path('products/<product>',views.product_cat,name="productcat"),#product category
    path('signup',views.signup,name="signup"),#signup page
    path('products/<product_brand>/<product_slug>',views.product_page,name="product_page"),#product category
]