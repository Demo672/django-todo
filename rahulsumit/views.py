from django.shortcuts import render

def index(req):
    return render(req, "home.html")

def todo(req):
    return render(req, "todo.html")

def signUp(req):
    return render(req, "signUp.html")