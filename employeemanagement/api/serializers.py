from rest_framework import serializers
from api.models import Employee
from django.contrib.auth.models import User


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
     model = Employee
     fields = ["first_name","middle_name","position","salary","supervisors"]


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user