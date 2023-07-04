from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewset,EmployeeViewset
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'Employees', EmployeeViewset)

urlpatterns = [
    path('',include(router.urls))
   
]


#extra url chahiye kyuki  company me companyId ke sare epmloyee lega.
#companies/{complanyId}/Employees
