from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Company

from company.serializers import (
    CompanySerializer, 
    CompanyDetailSerializer,
)

COMPANIES_URL = reverse('company:company-list')

def detail_url(company_id): 
    return reverse('company:company-detail',args=[company_id])

def create_company(**params):
    """Create and return a sample company."""
    defaults = {
        'name': 'Sample Company name',
    }
    defaults.update(params)

    company = Company.objects.create(**defaults)
    return company
 


class CompanyApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_companies(self):
        """Test retrieving a list of companies."""
        create_company()

        res = self.client.get(COMPANIES_URL)

        companies = Company.objects.all().order_by('-id')
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_company_detail(self): 
        """test company detail"""
        company = create_company()

        url = detail_url(company.id)
        res = self.client.get(url)

        serializer = CompanyDetailSerializer(company)
        self.assertEqual(res.data, serializer.data)

    def test_create_company(self): 
        payload = {
            'name' : 'Sample company'
        }
        res = self.client.post(COMPANIES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        company = Company.objects.get(id = res.data['id'])
        for k, v in payload.items(): 
            self.assertEqual(getattr(company, k), v)
        self.assertEqual(company.name, payload['name'])