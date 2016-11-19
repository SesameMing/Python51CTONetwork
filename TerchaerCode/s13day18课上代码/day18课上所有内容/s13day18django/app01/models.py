from django.db import models

# Create your models here.
from django.db import models

# 陈超，普通用户
# 淮军，超级用户
class Gender(models.Model):
    name = models.CharField(max_length=32)


class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='用户名',editable=False)
    email = models.EmailField(db_index=True)
    memo = models.TextField()
    img = models.ImageField(upload_to='upload')
    user_type = models.ForeignKey("UserType", null=True, blank=True)# unique
    # user_type = models.OneToOneField("UserType", null=True, blank=True)# unique
    # ctime = models.DateTimeField(auto_now_add=True)
    # uptime = models.DateTimeField(auto_now=True)

    # gender = models.ForeignKey(Gender)
    gender_choices = (
        (0, "男"),
        (1, "女"),
    )
    gender = models.IntegerField(choices=gender_choices,default=1)

# 普通用户，超级用户
class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class B2G(models.Model):
    boy = models.ForeignKey('Boy')
    girl = models.ForeignKey('Girl')

class Boy(models.Model):
    name = models.CharField(max_length=32)
# 吴文煜，王建，王志刚，杜宝强

class Girl(models.Model):
    name = models.CharField(max_length=32)

    f = models.ManyToManyField(Boy)
# 铁锤，钢弹，如花
