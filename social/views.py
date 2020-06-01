from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Social
from .serializers import SocialSerializer


class SocialCreate(APIView):

	def post(self,request):
		serializers = SocialSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status = status.HTTP_201_CREATED)
		return Response(serializers.errors , status = status.HTTP_400_BAD_REQUEST)

class SocialDelete(APIView):

	def delete(self,request,fk,pk):
		try:
			social = Social.objects.get(follower = fk,following = pk)
		except Social.DoesNotExist:
			raise Http404

		social.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)


class SocialFollowingGet(APIView):

	def get(self,request,pk):
		try:
			social = Social.objects.filter(follower = pk)
		except Social.DoesNotExist:
			raise Http404

		serializers = SocialSerializer(social,many = True)
		return Response(serializers.data)

class SocialFollowerGet(APIView):

	def get(self,request,pk):
		try:
			social = Social.objects.filter(following = pk)
		except Social.DoesNotExist:
			raise Http404

		serializers = SocialSerializer(social , many = True)
		return Response(serializers.data)





