from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'tweetproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/$', views.timeline),
    url(r'^statistics/$', views.statistics),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
