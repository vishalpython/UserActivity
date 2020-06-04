from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.serializers import serialize
# Create your views here.
class UserRegistration(View):
    def post(self,request):
        ucf=UserCreationForm(request.POST)
        if ucf.is_valid():
            ucf.save()
            messages.success(request,"Saved")
            return redirect("user")
        else:
            return render(request, "Userform.html", {"ucf":ucf})
    def get(self,request):
        return render(request,"Userform.html",{"ucf":UserCreationForm()})


class UserLogin(View):
    def get(self,request):
        return render(request,"login.html",{"af":AuthenticationForm()})
    def post(self,request):
        pass


class ProfileUpdate(UpdateView):
    template_name = "update.html"
    model = User
    success_url = "/home/"
    fields = ('first_name','last_name','is_staff','email')


class UserActivity(View):
    def get(self,request):

        PM=User.objects.all()
        data=serialize("json",PM)
        return HttpResponse(data,content_type="application/json")