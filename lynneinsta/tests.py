from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from models import Profile,Pic,Comment,Follow
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(username='lynne')
        self.user.save()
        self.profile=Profile(user=self.user,name='lynne',bio='hey there',profile_pic='default.png')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    def test_saveProfile(self):
        self.profile.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)
        
class PicTestClass(TestCase):
    def setUp(self):
        self.user=User(username='lynne')
        self.user.save()
        self.profile=Profile(user=self.user,name='linetlucy',bio='hey there',profile_pic='default.png')
        self.pic=Pic(id=1, likes=5, image='default.png', title='dress', description='cute dress',user=self.profile)
    def tearDown(self):
        Pic.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.pic, Pic))
    def test_save_pic(self):
        saved_pic=Pic.objects.all().delete()
        self.assertTrue((len(saved_pic))>0)
    def test_delete_pic(self):
        self.pic.delete_pic()
        deleted_pic = Pic.objects.all()
        self.assertTrue(len(deleted_pic)==0) 

class CommentTestClass(TestCase):
    def setUp(self):
        self.user=User(username='lynne')
        self.user.save()
        self.profile=Profile(user=self.user,name='linetlucy',bio='hey there',profile_pic='default.png')
        self.pic=Pic(id=1, likes=10, image='default.png', title='dress', description='cute dress',user=self.profile)
        self.comment=Comment(user=self.user,comment='cute!')
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment)) 

class FollowTestCase(TestCase):
    def setUp(self):
        self.user=User(username='lynne')
        self.user.save()
        self.follow=Follow(user=self.user, follower=200, followed=1000)
    def test_instance(self):
        self.assertTrue(isinstance(self.follow, Follow))

