from django.conf.urls import url

from core.views import IndexPageView

urlpatterns = [
    url(r'^welcome/$', IndexPageView.as_view(), name='index'),
]
