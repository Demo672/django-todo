from django.shortcuts import render

def index(req):
    return render(req, "home.html")

def signIn(req):
    return render(req, "sign_in.html")