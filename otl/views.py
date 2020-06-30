from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from .forms import Fullset
from .models import Ref
from django.contrib.auth import login, logout

# Create your views here.

def comments(request, uidb64=None, token=None):
	try:
		uid=force_text(urlsafe_base64_decode(uidb64))
		user=User.objects.get(pk=uid)
	except User.DoesNotExist:
		user = None
	if user and default_token_generator.check_token(user, token):
		if request.method=="POST":
			form=Fullset(request.POST)
			if form.is_valid():
				answer=form.save(commit=False)
				answer.submitby=user
				answer.marks_obtained = 0
				reference=Ref.objects.get(pk=1)
				if answer.AnsQ1==reference.AnsQ1:
					answer.marks_obtained +=1
				if answer.AnsQ2==reference.AnsQ2:
					answer.marks_obtained +=1
				if answer.AnsQ3==reference.AnsQ3:
					answer.marks_obtained +=1
				if answer.AnsQ4==reference.AnsQ4:
					answer.marks_obtained +=1
				if answer.AnsQ5==reference.AnsQ5:
					answer.marks_obtained +=1
				if answer.AnsQ6==reference.AnsQ6:
					answer.marks_obtained +=1
				if answer.AnsQ7==reference.AnsQ7:
					answer.marks_obtained +=1
				if answer.AnsQ8==reference.AnsQ8:
					answer.marks_obtained +=1
				if answer.AnsQ9==reference.AnsQ9:
					answer.marks_obtained +=1
				if answer.AnsQ10==reference.AnsQ10:
					answer.marks_obtained +=1
				answer.save()
				login(request, user)
				logout(request)
				return HttpResponseRedirect('/success/')
		else:
			form=Fullset()
		return render(request, 'question.html', {'form':form})
	else:
		return HttpResponse("Your time has expired")
