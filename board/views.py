from math import ceil

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from board import models

LIST_COUNT = 10


def index(request):
    results = models.findall()
    data = {'boardlist': results}

    # page = request.GET.get("p")
    # page = 1 if page is None else int(page)
    #
    # print(page)

    # totalcount = models.count()
    # boardlist = models.findall(page, LIST_COUNT)

    # paging 정보를 계산
    # pagecount = ceil(totalcount / LIST_COUNT)
    #
    # data = {
    #     "boardlist": boardlist,
    #     'pagecount': pagecount,
    #     'netpage': 7,
    #     'prvpage': 5,
    #     'curpage': 2
    #
    # }

    return render(request, 'board/index.html', data)



def view(request):
    no = 1
    result = models.findbyno(no)
    data = {'board': result}
    return render(request, 'board/view.html', data)

def writeform(request):
    # Access Control(접근 제어)
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = request.session['authuser']['no']

    # 1. user 데이터를 가져오기
    result = models.findbyno(no)
    data = {'user': result}

    return render(request, 'board/writeform.html', data)


def write(request):
    no = request.session['authuser']['no']
    title = request.POST['title']
    content = request.POST['content']
    models.write(no, title, content)
    return HttpResponseRedirect('/board/view')



def updateform(request):
    return render(request, 'board/updateform.html')