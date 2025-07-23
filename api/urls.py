# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import (DocumentViewSet,
    LoanViewSet,
    CooperativePartnerBankViewSet,
    UserViewSet,
    LoanRepaymentViewSet,
    STKPushView, 
    daraja_callback,
    FarmerWealthViewSet,
    daraja_callback,

)



router = DefaultRouter()
router.register(r'loan_Repayments',LoanRepaymentViewSet, basename="LoanRepayments")
router.register(r'documents',DocumentViewSet,basename="documents")
router.register(r'loans', LoanViewSet, basename="loans")
router.register(r'cooperative_partner_banks',CooperativePartnerBankViewSet,basename="bankpartners")
router.register(r'farmer_wealth',FarmerWealthViewSet,basename="farmer_wealth")
router.register(r"users",UserViewSet,basename ="users")
urlpatterns = [
    path('', include(router.urls)),
    path('disbursment/stk-push/', STKPushView.as_view(), name='disbursment-stk-push'),
    path('disbursment/callback/', daraja_callback, name='disbursment-callback') 
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





