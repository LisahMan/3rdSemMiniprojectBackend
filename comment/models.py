from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from datetime import datetime

class Comment(models.Model):
	
	user = models.ForeignKey(User , related_name = 'user_comment',on_delete = models.CASCADE,db_index=True)
	post = models.ForeignKey(Post , related_name = 'comments',on_delete = models.CASCADE,db_index=True)
	content = models.TextField()
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return str(self.user) + " " + self.content

