from django.urls import path
from . import views # to use classes from views.py

#use of dynamic urls
urlpatterns = [
    path('',views.IndexView.as_view(),name="home"),#home page
    path('products/<product>',views.product_cat,name="productcat"),#product category
    path('signup',views.signup,name="signup"),#signup page
    path('products/<product_brand>/<product_slug>',views.ProductPageView.as_view(),name="product_page"),#product category
]