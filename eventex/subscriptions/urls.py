from django.conf.urls import url
from eventex.subscriptions import views as eventex_subs

urlpatterns = [
    url(r'^$', eventex_subs.new, name='new'),
    url(r'^(\d+)/$', eventex_subs.detail, name='detail'),
]
