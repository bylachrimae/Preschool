from django import forms
from members.models import CustomMember
from .models import Text


class TextForm(forms.ModelForm):
	class Meta:
		model = Text
		fields = ('receiver','msg_title','msg_content')
		labels = {
		'receiver': 'To',
		'msg_title': 'Title',
		'msg_content': 'Content'
		}

		widgets = {
		'receiver':forms.Select(attrs={'class':'form-control','placeholder':'To'}),
		'msg_title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
		'msg_content':forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
		}
