from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from user import models


def joinform(request): # 회원가입
    return render(request, 'user/joinform.html')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def join(request):
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]
    gender = request.POST["gender"]

    models.insert(name, email, password, gender)

    return HttpResponseRedirect('/user/joinsuccess')





def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    email = request.POST["email"] # '로그인' 으로 가져온 값
    password = request.POST["password"]

    result = models.findby_email_and_password(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # login 처리
    request.session["authuser"] = result

    return HttpResponseRedirect('/')



def logout(request):
    del request.session["authuser"]
    return HttpResponseRedirect('/')




def updateform(request): # 회원정보 수정
    # Access Control(접근 제어)
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')

    authuser = request.session["authuser"]
    result = models.findbyno(authuser["no"]) # name, email, gender 받아옴
    return render(request, 'user/updateform.html')


def update(request):
    name = request.POST["name"] # '수정하기'로 가져온 값
    gender = request.POST["gender"]

    if request.POST['password'] is not '':
        password = request.POST['password']

    models.update(name, password)
    request.session['authuser']['name'] = name

    return HttpResponseRedirect('/user/updateform?result=success')