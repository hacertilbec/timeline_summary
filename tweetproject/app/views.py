from django.shortcuts import render, render_to_response
import json
from django.conf import settings
import app.codes.twitterStreaming as ts


def timeline(request):
	timeline = ts.get_timeline()
	context = {'tweets': timeline}

	return render_to_response('timeline.html', context)

def statistics(request):
	pass