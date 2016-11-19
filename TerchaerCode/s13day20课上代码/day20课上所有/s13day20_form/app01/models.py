from django.db import models

# Create your models here.

class UserType(models.Model):
    caption = models.CharField(max_length=16)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    user_type = models.ForeignKey('UserType')

# 多对多

# class B2G(models.Model):
#     b_id = models.ForeignKey('Boy')
#     g_id = models.ForeignKey('Girl')
# 吴文煜1，吴文煜2，吴文煜3，吴文煜4
class Boy(models.Model):
    username = models.CharField(max_length=16)

    def __str__(self):
        return str(self.id)
# 怀军1，怀军2，怀军3，怀军4，怀军5，怀军6，
class Girl(models.Model):
    name = models.CharField(max_length=16)
    b = models.ManyToManyField('Boy')
    def __str__(self):
        return str(self.id)














