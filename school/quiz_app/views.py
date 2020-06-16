from django.shortcuts import render
from django.http import HttpResponse
import os
import requests
import random
url = 'https://opentdb.com/api.php?amount=10'
r = requests.get(url)
api_response = r.json()
questions = []
options =[]
correct_answer = []
def index(request):
	if request.method == "POST":
		display_type = request.POST.get("option", None)
		print(display_type)
		data = api_response['results']
		for i in data:
			if i['correct_answer'] not in i['incorrect_answers']:
				i['incorrect_answers'].append(i['correct_answer'])
			random.shuffle(i['incorrect_answers'])
			questions.append(i['question'])
			options.append(i['incorrect_answers'])
			correct_answer.append(i['correct_answer'])
		context = {'questions': zip(questions,options, correct_answer)}
	return render(request, 'index.html', context)
