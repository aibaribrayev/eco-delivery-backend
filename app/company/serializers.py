"""
Serializers for companies Api
"""

from rest_framework import serializers
from core.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']
        read_only_fields = ['id']
        
class CompanyDetailSerializer(CompanySerializer): 
    class Meta(CompanySerializer.Meta):
        fields = CompanySerializer.Meta.fields

    