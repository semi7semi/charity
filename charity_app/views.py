from django.shortcuts import render
from django.views import View

from charity_app.models import Institution, Category


class LandingPage(View):
    def get(self, request):
        categories = Category.objects.all()
        fundations = Institution.objects.filter(type="fundation")
        organizations = Institution.objects.filter(type="organization")
        locals = Institution.objects.filter(type="local")
        ctx = {
            "fundations": fundations,
            "organizations": organizations,
            "locals": locals,
            "categories": categories}
        return render(request, "index.html", ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")

class Form(View):
    def get(self, request):
        return render(request, "form.html")
