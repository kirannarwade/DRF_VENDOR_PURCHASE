from django.urls import path
from .import views

urlpatterns = [
    path('vendors/', views.VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:pk>/performance/',
         views.VendorPerformanceView.as_view(), name='vendor-performance'),

    path('purchase_orders/', views.PurchaseOrderListCreateView.as_view(),
         name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderDetailView.as_view(),
         name='purchase-order-detail'),
    path('purchase_orders/<int:pk>/acknowledge/',
         views.PurchaseOrderAcknowledgmentView.as_view(), name='purchase-order-acknowledge'),
         
    path('historical_performance/', views.VendorHistoricalPerformanceView.as_view(),
         name='vendor-historical-performance'),

]