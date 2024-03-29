from django.urls import path
from . import views
from product.views import ProductViewsetApi
from rest_framework.routers import DefaultRouter

app_name = 'product'
urlpatterns = [
    path('category_list', views.CategoryListViewAPI.as_view(), name='category_list'),
    path('productssortedcategory/<slug:slug>', views.ProductListSortedCategoryVireApi.as_view(), name='productsortedbycategory'),

]



router = DefaultRouter()
router.register(r'products', ProductViewsetApi, basename='product')
urlpatterns += router.urls
