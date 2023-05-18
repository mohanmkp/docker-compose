from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from product.serializers import *
from .models import *



class product_view(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = product_serializer
    queryset = products.objects.all()




