from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^user/(?P<username>\w{0,50})',views.profile,name='profile'),
    url(r'^ajax-like-photo/$',views.ajaxlikephoto,name = 'like_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
