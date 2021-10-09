# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    params = {'name':'Mr. Grey'}
    return render(request, 'index.html', params)

def analyze(request):
    # Grab Data
    djtext = request.POST.get('text', 'default')
    djcapfirst = request.POST.get('capfirst', 'off')
    djcapall = request.POST.get('capall', 'off')
    djsmallall = request.POST.get('smallall', 'off')
    djremovepunc = request.POST.get('removepunc', 'off')

    # Analyze Data
    if djcapfirst == 'on':
        djtext_modified = djtext.title()
        params = {'analyzed_data':djtext_modified}
    
    elif djcapall == 'on':
        djtext_modified = djtext.upper()
        params = {'analyzed_data':djtext_modified}
    
    elif djsmallall == 'on':
        djtext_modified = djtext.lower()
        params = {'analyzed_data': djtext_modified}
    
    if djremovepunc == 'on':
        djtext_modified = djtext.translate(str.maketrans('', '', string.punctuation))
        params = {'analyzed_data': djtext_modified}
    
    djcount = 0
    djcount_modified = 0
    if djcapfirst == 'on' or djcapall == 'on' or djsmallall == 'on' or djremovepunc == 'on':
        for i in djtext_modified:
            djcount_modified += 1
        params = {'analyzed_data': djtext_modified, 'djcount':djcount_modified, 'modified_or_not':'Modified Paragraph'}
    else:
        for i in djtext:
            djcount += 1
        params = {'djcount':djcount, 'modified_or_not':'Paragraph'}
        # return render(request, 'analyze.html', params)
    
    return render(request, 'analyze.html', params)
