from django.http import HttpResponse
from django.shortcuts import render
import operator

def naya(request):
    return HttpResponse("THis is your boy")

def about(request):
    return render(request, 'about.html')


def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    data = request.GET['txtarea1']
    word_list = data.split()
    list_length = len(word_list)

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

    sorted_list=sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',  {'showtxt':data, 'length':list_length, 'word_dictkey':sorted_list})