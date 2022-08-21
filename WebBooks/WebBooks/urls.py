
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import re_path as url





urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    url( r'^books/$', views.BookListView.as_view(), name='books'),
    url( r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    ]