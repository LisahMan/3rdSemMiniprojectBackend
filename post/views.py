from django.http import Http404 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Post
from .models import SavedPost
from .serializers import PostSerializer
from .serializers import SavedPostSerializer
from django.contrib.auth.models import User
from social.models import Social
from datetime import datetime

class PostCollection(APIView):

	def post(self,request):
		serializers = PostSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data , status = status.HTTP_201_CREATED)
		return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)
   
	
		
class PostDetail(APIView):

	def get_post(self,pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self,request,pk):
		post = self.get_post(pk)
		serializers = PostSerializer(post)
		return Response(serializers.data)

	def delete(self,request,pk):
		post = self.get_post(pk)
		post.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class PostOfUser(APIView):

	def get(self,request,pk):
		posts = Post.objects.filter(user=pk).order_by('-date')
		if posts:
			for post in posts:
				if SavedPost.objects.filter(post = post).exists():
					post.saved = "1"
				else:
					post.saved = "0"

			serializers = PostSerializer(posts,many = True)
		return Response(serializers.data)



class PostOfFollowing(APIView):

	def get(self,request,pk):
		social = Social.objects.filter(follower = pk)
		posts = Post.objects.filter(user__in = social.values_list('following')).order_by('-date') | Post.objects.filter(user = pk).order_by('-date')
		
		if posts:
			for post in posts:
				if SavedPost.objects.filter(post = post).exists():
					post.saved = "1"
				else:
					post.saved = "0"

			serializers  = PostSerializer(posts,many=True)
		return Response(serializers.data)

class PostSave(APIView):

	def post(self,request):
		serializers = SavedPostSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data , status = status.HTTP_201_CREATED)
		return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)

class PostUnsave(APIView):

	def delete(self,request,fk,pk):
		try:
			saved_post = SavedPost.objects.get(user = fk,post =pk)
		except SavedPost.DoesNotExist:
			raise Http404

		saved_post.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)

class SavedPostOfUser(APIView):

	def get(self,request,pk):

		saved_posts = SavedPost.objects.filter(user=pk)
		posts = Post.objects.filter(id__in = saved_posts.values_list('post')).order_by('-date')
		if posts:
			for post in posts:
				post.saved = "1"
			serializers = PostSerializer(posts,many=True)
			return Response(serializers.data)
		return Response("SavedPost DoesNotExists",status = status.HTTP_400_BAD_REQUEST)
