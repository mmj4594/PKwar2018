# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from .models import Quiz, QuizNow, Bingo, Score, RightWrong, Announcement
from django.shortcuts import render

# Create your views here.
def quiz(request):
	return render(request, "quiz/quiz.html")

def announcement(request):
	announce = Announcement.objects.order_by('-pk')[0]

	return JsonResponse({'num': announce.pk, 'is_quiz_start': announce.is_quiz_start, 'ment': announce.ment})

def json(request):
	bingos = Bingo.objects.all()

	postech = [[0]*5 for i in range(5)]
	kaist = [[0]*5 for i in range(5)]

	for bingo in bingos:
		if bingo.is_postech:
			postech[bingo.x - 1][bingo.y - 1] = {'num': bingo.quiz.quiz_number, 'passed': bingo.passed, 'right': bingo.right}
		else:
			kaist[bingo.x - 1][bingo.y - 1] = {'num': bingo.quiz.quiz_number, 'passed': bingo.passed, 'right': bingo.right}
	
	scores = Score.objects.all()

	for score in scores:
		if score.is_postech:
			postechscore = score.score
		else:
			kaistscore = score.score

	rightwrongs = RightWrong.objects.all()

	for rightwrong in rightwrongs:
		if rightwrong.is_postech:
			postechrw = rightwrong.right_wrong
		else:
			kaistrw = rightwrong.right_wrong

	quiznow = QuizNow.objects.all()[0]
	qn = {}
	qn["num"] = quiznow.quiz_now.quiz_number
	qn["content"] = quiznow.quiz_now.quiz_content
	if quiznow.quiz_now.quiz_image:
		qn["url"] = quiznow.quiz_now.quiz_image.url
	else:
		qn["url"] = ""

	if quiznow.quiz_now.option1:
		qn["option1"] = quiznow.quiz_now.option1
	
	if quiznow.quiz_now.option2:
		qn["option2"] = quiznow.quiz_now.option2
									
	if quiznow.quiz_now.option3:
		qn["option3"] = quiznow.quiz_now.option3
	if quiznow.quiz_now.option4:
		qn["option4"] = quiznow.quiz_now.option4
	if quiznow.quiz_now.option5:
		qn["option5"] = quiznow.quiz_now.option5
	if quiznow.quiz_now.option6:
		qn["option6"] = quiznow.quiz_now.option6
	if quiznow.quiz_now.option7:
		qn["option7"] = quiznow.quiz_now.option7
	if quiznow.quiz_now.option8:
		qn["option8"] = quiznow.quiz_now.option8
	if quiznow.quiz_now.option9:
		qn["option9"] = quiznow.quiz_now.option9
	if quiznow.quiz_now.option10:
		qn["option10"] = quiznow.quiz_now.option10

	
	return JsonResponse({'quiznow': qn, 'postech_bingo': postech, 'kaist_bingo': kaist, 'postechscore': postechscore, 'kaistscore': kaistscore, 'postechrw': postechrw, 'kaistrw': kaistrw, })
