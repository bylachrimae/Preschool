from django.db import models
from members.models import CustomMember
from datetime import date

class Text(models.Model):
	sender = models.ForeignKey(CustomMember,related_name='sender',on_delete=models.CASCADE)
	receiver = models.ForeignKey(CustomMember,related_name='receiver',on_delete=models.CASCADE)
	msg_title = models.CharField('Message Title',max_length=120)
	msg_content = models.TextField(blank=True)
	msg_date = models.DateTimeField(auto_now_add=True)
	read = models.BooleanField(default=False)

