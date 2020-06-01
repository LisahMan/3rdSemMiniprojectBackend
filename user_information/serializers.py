from rest_framework import serializers
from .models import UserInformation
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
	phone_number = serializers.CharField(source='user_information.phone_number',write_only = True)	
	email = serializers.CharField(read_only = True)
	id = serializers.CharField(read_only=True)
	
	

	class Meta:
		model = User
		fields = ('id','username' , 'password' ,'phone_number','email')
		extra_kwargs = {'password' : {'write_only' : True}}


	def create(self,validated_data):
		user = User.objects.create_user(username = validated_data['username'] , password = validated_data['password'])
		UserInformation.objects.create(user = user ,phone_number = validated_data['user_information']['phone_number'])
		return user

