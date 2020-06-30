import re
import string
import random
from otl.models import Qbank
from otl.models import Question
from otl.models import Ref
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Ref
from .models import Set
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
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

class Option:
	def __init__(self, choice, ans):
		self.choice = choice
		self.ans = ans


# Separating text and options and ans from each question
class Mcq:
	def __init__(self, text):
		reg = re.compile(r'(.*)\no\)(.*)\no\)(.*)\no\)(.*)\no\)(.*)\n(\d)')
		fragments = reg.search(text)
		count=1
		self.question = fragments.group(count)
		self.options = []
		count += 1
		while(count <= 5):
			myoption = Option(fragments.group(count), int(fragments.group(6)) == count-1)
			self.options.append(myoption)
			count+=1
			
		
# Separating the chunk of questions containing the text, options and ans
class qp:
	def __init__(self, filename):
		f = open(filename)
		text = f.read()
		reg = re.compile(r'.*\no\).*\no\).*\no\).*\no\).*\n\d')
		fragments = reg.findall(text)
		self.fullset = []
		for elt in fragments:
			mymcq = Mcq(elt)
			self.fullset.append(mymcq)
	def olotpalot(self):
		random.shuffle(self.fullset)
		for elt in x.fullset:
			random.shuffle(elt.options)
				

def loadquestion(filename):
	x=qp(filename)
	#x.olotpalot()
	for elt in x.fullset:
		qbank=Qbank()
		qbank.headline=elt.question
		qbank.option1=elt.options[0].choice
		if elt.options[0].ans:
			qbank.correctoption=1
		qbank.option2=elt.options[1].choice
		if elt.options[1].ans:
			qbank.correctoption=2
		qbank.option3=elt.options[2].choice
		if elt.options[2].ans:
			qbank.correctoption=3
		qbank.option4=elt.options[3].choice
		if elt.options[3].ans:
			qbank.correctoption=4
		qbank.save()
	paper=Question.objects.create(title='chemistry')
	allquestion=Qbank.objects.all()
	for q in allquestion:
		q.question.add(paper)

def createtemplate():
	questionset = Question.objects.get(title='chemistry').qbank_set.all()
	temp_ref=[]
	y=['1','2','3','4','5','6','7','8','9','10']
	file=open("question.html", "w")
	file.write('{% extends "base.html" %}\n\n')
	file.write('{% block content %}\n')
	file.write('<form method="POST">\n')
	file.write('{% csrf_token %}\n')
	file.write('\t{{ form.non_field_errors }}\n')
	file.write('\t{{ form.source.errors }}\n')
	file.write('\t{{ form.source }}\n')
	file.write('<div class="well">\n')
	file.write('<ol>\n')
	for elt, ans in zip(questionset, y):
		file.write('<p>\t<li>')
		file.write(elt.headline)
		file.write('\n')
		file.write('\t\t<ol>\n')
		file.write('\t\t\t<li>')
		file.write(elt.option1)
		file.write('\n')
		file.write('\t\t\t<li>')
		file.write(elt.option2)
		file.write('\n')
		file.write('\t\t\t<li>')
		file.write(elt.option3)
		file.write('\n')
		file.write('\t\t\t<li>')
		file.write(elt.option4)
		file.write('\n')
		file.write('\t\t</ol>\n')
		file.write('\t{{ form.AnsQ' + ans + '.label_tag }}\n')
		file.write('\t{{ form.AnsQ' + ans + '.errors }}\n')
		file.write('\t{{ form.AnsQ' + ans + ' }}\n')
		file.write('</p>\n')
		temp_ref.append(int(elt.correctoption))
	file.write('</ol>\n')
	file.write('</div>\n')
	file.write('<input type="submit" value="submit" class="btn btn-primary btn-lg">\n')
	file.write("</form>\n")
	file.write("{% endblock %}\n")
	file.close()

	reference=Ref(AnsQ1=temp_ref[0],
			AnsQ2=temp_ref[1],
			AnsQ3=temp_ref[2],
			AnsQ4=temp_ref[3],
			AnsQ5=temp_ref[4],
			AnsQ6=temp_ref[5],
			AnsQ7=temp_ref[6],
			AnsQ8=temp_ref[7],
			AnsQ9=temp_ref[8],
			AnsQ10=temp_ref[9])
	reference.save()	


def send_otl_email():
	text_content="Your one time link Email"
	subject="Request for your comment"
	template_name="email/otl.html"
	from_email=settings.EMAIL_HOST_USER
	users=User.objects.all()
	for user in users:
		recipients=[user.email]

		kwargs = {
			"uidb64":urlsafe_base64_encode(force_bytes(user.pk)),
			"token":default_token_generator.make_token(user)
		}

		the_url=reverse('user_comments', kwargs=kwargs)
		otl_url="{0}://{1}{2}".format("http", "127.0.0.1:8000", the_url)

		context = {
			'user' : user,
			'otl_url': otl_url,
		}
		html_content = render_to_string(template_name, context)
		email=EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		email.send()
		print("Mail has been sent to {0}\n".format(user.email))

def send_result():
	ref_result=Ref.objects.get(pk=1)
	text_content = "Your result is now here"
	from_email=settings.EMAIL_HOST_USER
	subject="Your result"
	template_name='email/result.html'
	results = Set.objects.filter(sent_result=False)
	for result in results:
		recipient=[result.submitby.email]
		context={
			'ref_result' : ref_result,
			'user_result': result,
			}
		html_content = render_to_string( template_name, context)
		email = EmailMultiAlternatives(subject, text_content, from_email, recipient)
		email.attach_alternative(html_content, "text/html")
		email.send()
		result.sent_result=True
		result.save()
		print("Mail has been sent to {0}\n".format(result.submitby.email))
