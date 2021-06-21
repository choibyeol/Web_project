from django.urls import path, include
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'khu_calendar'

urlpatterns = [
    url(r'^$', views.khu_calendar.as_view(), name='khu_calendar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path(r'^$', views.post_list, name='post_list'),
# ]
