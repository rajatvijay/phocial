from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# In order to keep your code generic, use the get_user_model() method
# to retrieve the user model and the AUTH_USER_MODEL setting to refer to
# it when defining model's relations to the user model, instead of referring
# to the auth User model directly.

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL)
  date_of_birth = models.DateField(blank=True, null=True) # what is Blank and Null?
  photo = models.ImageField(upload_to='uses/%Y/%m/%d', blank=True)
  
  def __str__(self):
    return 'Profile for user {}'.format(self.user.username)

class Contact(models.Model):
  user_from = models.ForeignKey(User, related_name='rel_from_set')
  user_to = models.ForeignKey(User, related_name='rel_to_set')
  created = models.DateTimeField(auto_now_add=True, db_index=True)

  class Meta:
    ordering = ('-created', )

  def __str__(self):
    return '{0} follows {1}',format(self.user_from, self.user_to)

#Add following to the User model dynamically
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))