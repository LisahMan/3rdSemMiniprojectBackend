from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):

	user = models.ForeignKey(User , related_name = 'user_post',on_delete = models.CASCADE,db_index=True)
	body = models.TextField()
	date = models.DateTimeField(default=datetime.now)
	saved = models.CharField(default = '0' ,max_length=1)

	def __str__(self):
		return str(self.user) + " " + self.body + " "  + str(self.date)


class SavedPost(models.Model):

	user = models.ForeignKey(User , related_name='saved_post_user',on_delete = models.CASCADE,db_index=True)
	post = models.ForeignKey(Post,related_name='saved_post',on_delete= models.CASCADE)

	def __str__(self):
		return str(self.user) + " " + str(self.post)

