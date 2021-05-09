import json
import datetime
import subprocess
from django.http import HttpResponse
import os
# from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.shortcuts import render
import k8s_container_automation.templates 

from django.conf import settings

def readpipe(pipe):
	response = ''
	for line in iter(pipe.readline, ''):
			print(line)
			if line:
				response += str(line)
			else:
				break
	return response

def start_service(yaml_name, action):
	yaml = os.path.join(settings.BASE_DIR, 'yaml', yaml_name)
	response = ''
	try:
		p = subprocess.Popen(['kubectl', action , '-f', yaml], stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
	except Exception as e:
		print(e)
		response = str(e)
	else:
		response += readpipe(p.stdout)
		response += readpipe(p.stderr)

	response

def service1(request):
	response = start_service('service1.yaml', 'create')
	return HttpResponse(response)

def http(request):
	response = start_service('http.yaml', 'create')
	return HttpResponse(response)

def stop(request):

	response = start_service('service1.yaml', 'delete')
	return HttpResponse(response)


	

def index(request):
	return render(request, 'index.html')

