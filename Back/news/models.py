'''
from djongo import models

class User(models.Model):
    nickname = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nickname


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    tag_koef = models.FloatField(default=0.5)

    class Meta:
        abstract = True

    def __str__(self):
        return self.tag_name + ", koef = " + str(self.tag_koef)


class usertag(models.Model):
    user = models.EmbeddedModelField(
        model_container=User,
    )

    tags = models.ArrayModelField(
        model_container=Tag,
    )
'''