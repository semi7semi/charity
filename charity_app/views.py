from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib.auth.models import User
from charity_app.forms import RegisterUserForm, LogForm
from charity_app.models import Institution, Category, Donation


class LandingPage(View):
    def get(self, request):
        categories = Category.objects.all()
        fundations = Institution.objects.filter(type="fundation")
        organizations = Institution.objects.filter(type="organization")
        locals = Institution.objects.filter(type="local")
        donation = Donation.objects.all()
        total_quantity = sum(donation.values_list('quantity', flat=True))
        no_of_inst = len(donation.annotate(Count('institution', distinct=True)))
        ctx = {
            "fundations": fundations,
            "organizations": organizations,
            "locals": locals,
            "categories": categories,
            "total_quantity": total_quantity,
            "no_of_inst": no_of_inst
        }
        return render(request, "index.html", ctx)


class UserDetails(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        donations = Donation.objects.filter(user=user.id)
        ctx = {
            "user": user,
            "donations": donations
        }
        return render(request, "user_details.html", ctx)


class Login(FormView):
    # logowanie i authentykacja
    form_class = LogForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        print("sss")
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, "Zły login lub haslo")
        return super().form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("landing-page")


# class Login2(View):
#     def get(self, request):
#         return render(request, "login.html")
#     def post(self, request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(request, username=email, password=password)
#         if user:
#             login(request, user)
#         return redirect("landing-page")


class Register(View):
    def get(self, request):
        form = RegisterUserForm()
        ctx = {"form": form}
        return render(request, "register.html", ctx)
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.username = user.email
            user.save()
        return redirect("landing-page")


# class Register2(View):
#     def get(self, request):
#         return render(request, "register.html")
#     def post(self, request):
#         name = request.POST.get("name")
#         surname = request.POST.get("surname")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         password2 = request.POST.get("password2")
#         if not name or not surname or not email or not password or not password2 or password != password2:
#             ctx = {"error": "Uzupelnij wszystkie pola"}
#             return render(request, "register.html", ctx)
#         else:
#             user = User()
#             user.username = email
#             user.first_name = name
#             user.last_name = surname
#             user.email = email
#             user.set_password(password)
#             user.save()
#             return redirect("landing-page")


class Form(View):
    def get(self, request, pk):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        ctx = {
            "categories": categories,
            "institutions": institutions}
        return render(request, "form.html", ctx)
    def post(selfself, request, pk):
        quantity = request.POST.get("bags")
        categories = request.POST.get("categories")
        institution = request.POST.get("organization")
        adress = request.POST.get("adress")
        phone_number = request.POST.get("phone")
        city = request.POST.get("city")
        zip_code = request.POST.get("postcode")
        pick_up_date = request.POST.get("date")
        pick_up_time = request.POST.get("time")
        pick_up_comment = request.POST.get("more_info")
        user = User.objects.get(pk=pk)
        donation = Donation()
        donation.quantity = quantity
        donation.institution = institution
        donation.address = adress
        donation.phone_number = phone_number
        donation.city = city
        donation.zip_code = zip_code
        donation.pick_up_date = pick_up_date
        donation.pick_up_time = pick_up_time
        donation.pick_up_comment = pick_up_comment
        donation.user = user
        for cat in categories:
            donation.categories.add(cat)
        # donation.save()
        return redirect("form-confirmation.html")
