
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CooperativeViewSet


router = DefaultRouter()
router.register(r"cooperatives",CooperativeViewSet,basename ="cooperatives")
urlpatterns=[
    path("",include(router.urls)),
    
]

# from django.urls import path, include
# from . import views
# from rest_framework.routers import DefaultRouter
# from .views import  CooperativeViewSet

# router=DefaultRouter()
# router.register(r'cooperatives',CooperativeViewSet)


# urlpatterns = [
#     path('cooperatives/',views.cooperative_list, name='cooperative_list'),
#     path('cooperatives/create/',views.cooperative_create,name='coopearative_create'),
#     path('',include(router.urls)),
#     path('cooperative/delete/',views.cooperative_delete, name='cooperative_delete'),
#     path('cooperative/update/',views.cooperative_update,name='cooperative_update'),
    
# ]


