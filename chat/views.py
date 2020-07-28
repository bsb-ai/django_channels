from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from .forms import UserCreateForm, LoginForm

def index(request):
    return render(request, 'chat/index.html', {})
    
@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
class Create_Account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/login')
        return render(request, 'chat/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'chat/create.html', {'form': form,})

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('chat/')
        return render(request, 'chat/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'chat/login.html', {'form': form,})


