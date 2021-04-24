"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render, redirect
from django.views.generic import RedirectView
from web3auth import views
from . import views as vs
from django.conf import settings
from django.conf.urls.static import static
from Posts import urls as post_url
from Posts import views as post_view
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.views import LogoutView


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'web3auth/login.html')
    else:
        return redirect('index/')


def auto_login(request):
    if not request.user.is_authenticated:
        return render(request, 'web3auth/autologin.html')
    else:
        return redirect('/admin/')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/index')),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', login, name='login'),
    url(r'^index1/', vs.index1, name='index'),
    url(r'^uploads/', vs.upload_file, name='uploads'),
    url(r'^auto_login/', auto_login, name='autologin'),
    url(r'^login_api/$', views.login_api, name='web3auth_login_api'),
    url(r'^signup_api/$', views.signup_api, name='web3auth_signup_api'),
    url(r'^signup/$', views.signup_view, name='web3auth_signup'),
    url(r'^shop/', vs.shop, name='shop'),
    url(r'^shop/(?P<name>[-\w]+)/(?P<pk>\d+)/$', post_view.PostDetail.as_view( ), name='single'),
    url(r'^frontend/', TemplateView.as_view(template_name="build/index.html")), ### react ?
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
