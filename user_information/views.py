from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserInformation
from .serializers import UserSerializers
from django.contrib.auth import authenticate
from social.models import Social

class UserCollection(APIView):

	def get(self,request):
		user = User.objects.all()
		serializers = UserSerializers(user , many = True)
		return Response(serializers.data)

	def post(self,request):
		serializers = UserSerializers(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data , status = status.HTTP_201_CREATED)
		return Response(serializers.errors ,status = status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

	def get_user(self,pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist :
			raise Http404

	def get(self,request,pk):
		user = self.get_user(pk)
		serializers = UserSerializers(user)
		return Response(serializers.data)

	def destroy(self,request,pk):
		user = self.get_user(pk)
		user.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class CheckUserDetail(APIView):

	def post(self,request):

		username = request.data['username']
		password = request.data['password']

		try:
			user = authenticate(username = username , password = password)
			if user:
				serializers = UserSerializers(user)
				return Response(serializers.data)
			else:
				return Response(data = "error",status = status.HTTP_400_BAD_REQUEST)
		except User.DoesNotExist:
			raise Http404

class SearchUser(APIView):

	def post(self,request,pk):
		username = request.data['username']

		try:
			user = User.objects.get(pk=pk)
			searched_user = User.objects.filter(username__icontains = username)
		except User.DoesNotExist:
			raise Http404

		if searched_user:
			for sUser in searched_user:
				if user.follower_id.filter(following = sUser).exists():
					sUser.email = "1"
				else:
					sUser.email = "0"
					if(sUser.username == user.username):
						sUser.email = "2"

			serializers = UserSerializers(searched_user,many = True)
			return Response(serializers.data)
		return Response(data = "User Does Not Exists",status = status.HTTP_400_BAD_REQUEST)


class FollowerOfUser(APIView):

	def get(self,request,pk):
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

		if user:
			social = Social.objects.filter(follower = pk)
			followed_user = User.objects.filter(id__in = social.values_list('following'))
			for fUser in followed_user:
				fUser.email = "1"
			serializers = UserSerializers(followed_user,many=True)
			return Response(serializers.data)
		return Response(data = "User DoesNotExist",status = status.HTTP_400_BAD_REQUEST)


