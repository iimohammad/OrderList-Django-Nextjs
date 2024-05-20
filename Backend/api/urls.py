from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from userauths import views as userauth_views
from rest_framework.routers import DefaultRouter
from vendors import views as vendor_views
from products import views as product_views
from orders import views as orders_views
from supportsite import views as supportsite_views

urlpatterns = [
    path('user/', include('rest_framework.urls')),
    path('user/token/', userauth_views.MyTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register/', userauth_views.RegisterView.as_view()),
    path('user/profile/', userauth_views.ProfileViewSet.as_view()),
    path('user/phone-verification/', userauth_views.Phone_Verification_send_sms.as_view()),
    path('user/phone-verification-code/', userauth_views.Phone_Verification.as_view()),

    #Orders
    path('order-list/', orders_views.OrderListCreateAPIView.as_view(),name='order-list'),
    path('order-create/',orders_views.OrderCreateView.as_view()),
    path('order-update/',orders_views.OrderUpdateView.as_view()),
    path('my-order-list/',orders_views.OrderListByUserID.as_view()),


    # Products
    path('product/tag/',product_views.TagViewsets.as_view()),
    path('product/category/',product_views.CategoryViewset.as_view()),
    path('product/product/',product_views.ProductViewsets.as_view()),
    path('product/brand/',product_views.BrandViewset.as_view()),

    # Vendor 
    path('vendor/response-order-create/',vendor_views.ResponseOrdersView.as_view()),
    path('vendor/response-order-list/',vendor_views.ResponseOrdersListView.as_view()),

    #Ticket to Technical Support of Site
    path('user/send-ticket/',supportsite_views.SendMessageToTechnicalSupport.as_view()),
    path('user/receive-ticket/',supportsite_views.ShowUserReceiveMessages.as_view()),
    path('admin/ticket/', supportsite_views.ShowAllReceiveMessages.as_view()),

] 