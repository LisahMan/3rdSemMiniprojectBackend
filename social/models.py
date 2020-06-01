from django.db import models
from django.contrib.auth.models import User

class Social(models.Model):

	follower = models.ForeignKey(User,related_name = 'follower_id' ,on_delete = models.CASCADE,db_index=True)
	following = models.ForeignKey(User , related_name = 'following_id',on_delete = models.CASCADE,db_index=True)

	def __str__(self):
		return str(self.follower) + " follows " + str(self.following)

	class Meta:
		unique_together = ("follower" , "following")


		