"""GuliStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import xadmin
from django.views.static import serve
from GuliStore.settings import MEDIA_ROOT
from goods.views import StudentsView,StudentsSingle

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)',serve,{'document_root':MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    url(r'^students/$',StudentsView.as_view()),
    url(r'^students/(\d+)/$', StudentsSingle.as_view()),
]
