from rest_framework import serializers
from .models import Post
from .models import SavedPost
from comment.serializers import CommentSerializer



class PostSerializer(serializers.ModelSerializer):

	comments = CommentSerializer(many = True , read_only = True)
	username = serializers.CharField(source = 'user.username',read_only=True)
	id = serializers.CharField(read_only=True)
	saved = serializers.CharField(read_only=True)
	
	

	class Meta:
		model = Post
		fields = ('id','user','username','body','date','saved','comments')
		extra_kwargs = {'date' : {'read_only' : True}}



class SavedPostSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = SavedPost
		fields = ('user','post')