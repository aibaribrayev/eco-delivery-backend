from rest_framework import viewsets
from rest_framework import permissions

from core.models import Company
from company import serializers

class CompanyViewSet(viewsets.ModelViewSet): 
    serializer_class = serializers.CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self): 
        return self.queryset.order_by('-id')

    def get_serializer_class(self): 
        if self.action == 'list': 
            return serializers.CompanySerializer
        return self.serializer_class
    
    def perform_create(self, serializer): 
        serializer.save()

