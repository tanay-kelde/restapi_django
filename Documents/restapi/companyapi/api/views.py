from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


#companies/{complanyId}/Employees ---->custom url path banega.......
    @action(detail=True,methods=['get'])


#custom method/url contain karna h to ye kare...
#create custom api....
    def Employees(self,request,primary_key=None):

        #Exception handle......
        try:
            company=Company.objects.get(primary_key=primary_key)
            emps=Employee.objects.filter(company=company)
            emps_serializers=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializers.data)
        except Exception as e:
            print(e)
        return Response({'message':'company not might exists !! Error'})



class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer