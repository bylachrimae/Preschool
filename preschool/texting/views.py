from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Text
from .forms import TextForm
from members.models import CustomMember
from django.contrib import messages

#User to User Messaging
@login_required
def send_text(request):
	if request.method == "POST":
		form = TextForm(request.POST or None)
		if form.is_valid():
			msg=form.save(commit=False)
			msg.sender = request.user
			msg.save()
			messages.success(request,'The Message is Sent Successfully!')
			return redirect('home')
	else:
		form = TextForm()
	return render(request,'texting/send_text.html',{'form':form})

#Single Text View
@login_required
def text_detail(request,text_id):
	text = Text.objects.get(id=text_id)
	text.read = True
	text.save()
	return render(request,'texting/text_detail.html',{'text':text})

#SentBox View
@login_required
def sentbox(request):
	user_messages = Text.objects.filter(sender=request.user)
	return render(request,'texting/sentbox.html',{'user_messages':user_messages})

#Message Inbox
@login_required
def inbox(request):
	user_messages = Text.objects.filter(receiver = request.user)
	return render(request,'texting/inbox.html',{'user_messages':user_messages})

#Delete Message
@login_required
def delete_text(request,text_id):
	text = Text.objects.get(id=text_id)
	text.delete()
	messages.success(request,'The Message is Deleted Successfully')
	return redirect('inbox')
