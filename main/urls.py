from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home),
    path('register', views.register),
    path('login',views.LoginPage),
    path('logout',views.logoutp),
    path('products',views.products,name='products'),
    path('add_products',views.add_product),
    path('pro/<int:phone_id>', views.more_details, name='detailpage'),
    path('del/<int:phone_id>',views.delete_item,name='delete'),
    path('item/<int:phone_id>',views.edit_item,name='update'),
    path('compare',views.compare),
    path('comparison_result',views.comparison_result,name='comparison_result'),
    path('search_results/', views.search_results, name='search_results'),
    path('user', views.user_list),
    path('delete/<str:username>',views.delete_user,name='delete_user'),
    path('Brands',views.brand_list),
    path('Brands/<int:brand_id>',views.brand_items,name="brand_items"),
    path('add_brand',views.add_brand),
    path('Brand/<int:brand_id>',views.brand_details,name="brand_details"),
    path('edit_brand/<int:brand_id>',views.edit_brand,name="brand_update"),
    path('delete_brand/<int:brand_id>', views.delete_brand, name='delete_brand'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)