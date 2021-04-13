#created manually
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    #charcounter = request.POST.get('charcounter','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations.','analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase!','analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and  char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines.','analyzed_text':analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed extra spaces.','analyzed_text':analyzed}
        djtext = analyzed

    # if charcounter == "on":
    #     count = 0
    #     for char in djtext:
    #         count += 1
    #     params = {'purpose':'Total number of characters are : ','analyzed_text':count}
    
    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)