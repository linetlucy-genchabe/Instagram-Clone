from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Pic(models.Model):
    pic = models.ImageField(upload_to = "pics/",null = True)
    user = models.ForeignKey(User,null=True)
    pic_name = models.CharField(max_length = 30,null = True)
    likes = models.IntegerField(default=0)
    pic_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True) 
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.pic_name

    def save_pic(self):
    	self.save()

    def delete_pic(self):
        self.delete()

    def update_caption(self,new_caption):
        self.pic_caption = new_caption
        self.save()
        
    @classmethod
    def get_pics_by_user(cls,id):
        sent_pics = Pic.objects.filter(user_id=id)
        return sent_pics

    @classmethod
    def get_pics_by_id(cls,id):
        fetched_pic = Pic.objects.get(id = id)
        return  fetched_pic

    class Meta:
    	ordering = ['-pub_date']

    def save_profile(self):
        self.save()

    def __str__(self):
    	return self.user.username

    
    
    

class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_pic = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_profile(cls,search_term):
		got_profiles = cls.objects.filter(first_name__icontains = search_term)
		return got_profiles
