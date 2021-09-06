from rest_framework import serializers
from .models import Employee



class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields=['emp_id','emp_name','social_media']