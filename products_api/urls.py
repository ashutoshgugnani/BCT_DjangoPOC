from django.urls import path
from django.urls.resolvers import get_ns_resolver
from .views import product_detail, product_list,ProdcutAPIView,GenericAPIView

urlpatterns=[
    path('product/',product_list),
    path('detail/<int:pk>/',product_detail),

    path('classProduct',ProdcutAPIView.as_view()),

    path('genericProduct',GenericAPIView.as_view())
]