
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
class details(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField(blank=False,null=False)
    dob=models.DateTimeField(blank=False,null=False)
    entry_date=models.DateTimeField(default=timezone.now)
    phone_no=models.IntegerField(blank=False)
    sex_choices=(('m','male'),('f','female'))
    sex=models.CharField(max_length=1,choices=sex_choices)
    def  __str__(self):
        return self.name

