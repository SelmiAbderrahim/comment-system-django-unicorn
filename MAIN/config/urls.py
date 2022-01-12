from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("comment.urls")), 
	]
urlpatterns.append(path("unicorn/", include("django_unicorn.urls")))