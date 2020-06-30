from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddUser(models.Model):
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	name = models.CharField(max_length=30)

class Set(models.Model):
        opts = (('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'))
        AnsQ1 = models.CharField(max_length=1, choices=opts)
        AnsQ2 = models.CharField(max_length=1, choices=opts)
        AnsQ3 = models.CharField(max_length=1, choices=opts)
        AnsQ4 = models.CharField(max_length=1, choices=opts)
        AnsQ5 = models.CharField(max_length=1, choices=opts)
        AnsQ6 = models.CharField(max_length=1, choices=opts)
        AnsQ7 = models.CharField(max_length=1, choices=opts)
        AnsQ8 = models.CharField(max_length=1, choices=opts)
        AnsQ9 = models.CharField(max_length=1, choices=opts)
        AnsQ10 = models.CharField(max_length=1, choices=opts)
        marks_obtained=models.IntegerField(default=0)
        submitby= models.ForeignKey(User, on_delete=models.CASCADE)
        sent_result=models.BooleanField(default=False)

        def get_absolute_url(self):
                return reverse('success', kwargs=self.marks_obtained)

class Ref(models.Model):
        opts = (('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'))
        AnsQ1 = models.CharField(max_length=1, choices=opts)
        AnsQ2 = models.CharField(max_length=1, choices=opts)
        AnsQ3 = models.CharField(max_length=1, choices=opts)
        AnsQ4 = models.CharField(max_length=1, choices=opts)
        AnsQ5 = models.CharField(max_length=1, choices=opts)
        AnsQ6 = models.CharField(max_length=1, choices=opts)
        AnsQ7 = models.CharField(max_length=1, choices=opts)
        AnsQ8 = models.CharField(max_length=1, choices=opts)
        AnsQ9 = models.CharField(max_length=1, choices=opts)
        AnsQ10 = models.CharField(max_length=1, choices=opts)

class Question(models.Model):
	title=models.CharField(max_length=20)

	class Meta:
		ordering=['title']

	def __str__(self):
		return self.title

class Qbank(models.Model):
	headline=models.CharField(max_length=400, blank=True)
	option1=models.CharField(max_length=100, blank=True)
	option2=models.CharField(max_length=100, blank=True)
	option3=models.CharField(max_length=100, blank=True)
	option4=models.CharField(max_length=100, blank=True)
	correctoption=models.IntegerField()
	question=models.ManyToManyField(Question)
