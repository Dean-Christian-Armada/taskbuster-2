from django.shortcuts import render
import datetime
from django.utils.timezone import now

now_naive = datetime.datetime.now()
now_aware = now()

def home(request):
	today = datetime.date.today()
	context_dict = {'today':today, 'now': now()}
	template = "taskbuster/index.html"
	return render(request, template, context_dict)
def home_files(request, filename):
	return render(request, filename, {}, content_type='text/plain')