from django.db import models
from django.contrib.auth.models import User

class UserInformation(models.Model):

	user = models.OneToOneField(User,related_name='user_information',on_delete = models.CASCADE,db_index=True)
	phone_number = models.CharField(max_length=10)


	def __str__(self):
		return str(self.user) + " " + self.phone_number