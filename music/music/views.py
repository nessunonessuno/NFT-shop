import random
import string

from django.shortcuts import render, redirect, reverse
from django.urls.exceptions import NoReverseMatch
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from web3auth.forms import LoginForm, SignupForm
from web3auth.utils import recover_to_addr
from django.utils.translation import ugettext_lazy as _
from web3auth.settings import app_settings
from django.http import HttpResponse
from .forms import UploadFileForm
from .handle_data import mint_with_metadata, upload_file_ipfs
import json
from Database.models import Post


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            nm = form.cleaned_data['name']
            dsc = form.cleaned_data['description']
            ft = form.cleaned_data['filetype']
            qty = form.cleaned_data['quantity']
            prc = form.cleaned_data['price']
            ipfs_location = f'http://127.0.0.1:8080/ipfs/{upload_file_ipfs(request.FILES["file"])}'
            mint_with_metadata(request.POST, ipfs_location)
            save = Post(name=nm, description=dsc, filetype=ft, quantity=qty, price=prc, file_location=ipfs_location, sold=False)
            save.save()

            return redirect('/uploads/')
        else:
            return redirect("/")
    else:
        form = UploadFileForm()
    return render(request, 'web3auth/upload.html', {'form': form})

def shop(request):
    post = Post.objects.all()
    return render(request, 'web3auth/shop.html', {'post':post})

def index1(request):
    token = request.session.get('login_token')
    form = LoginForm(token, request.POST)
    if form.is_valid():
        sign, address = form.cleaned_data.get("signature"), form.cleaned_data.get("address")
        del request.session['login_token']
        user = authenticate(request, token=token, address=address, signature=sign)
        if user:
            login(request, user, 'web3auth.backend.Web3Backend')
    return render(request,
                  "web3auth/index.html",
                  {'form': form})

