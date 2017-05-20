"""mysite URL Configuration

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
import os
from django.conf.urls import url
from django.contrib import admin
from bookmarks.views import *
from django.views.generic import TemplateView


site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Browsing
    url(r'^$', main_page),
    url(r'^popular/$', popular_page),
    url(r'^user/(\w+)/$', user_page),
    url(r'^tag/([^\s]+)/$', tag_page),
    url(r'^search/$', search_page),

    # Session management
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register_page),
    url(r'^register/success/$', TemplateView.as_view(
        template_name='registration/register_success.html')),
 
    # Account management
    url(r'^save/$', bookmark_save_page),
    url(r'^vote/$', bookmark_vote_page),

    # Site media
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': site_media}),

    # Ajax
    url(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
]
