from rest_framework import serializers
from api.models import Company,Employee
 


#formate of create serializers
# class SerializerName(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ModelName
#         fields = List of Fields



# create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    comapny_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    Employee_id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"


