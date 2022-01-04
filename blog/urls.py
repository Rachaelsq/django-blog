''' 
=================
BLOGAPP URLS
=================
'''

from . import views
from django.urls import path
from .views import DeleteView, DetailView, BlogDetail
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView

urlpatterns = [
    #path('', views.home, name='blog-home'),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('<str:blog>/<slug:slug>/', BlogDetail.as_view(), name='blog-detail')
    #path('<str:author>/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    #path('<str:author>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
''' urlpatterns = [
    #path('<slug:slug>', views.BlogView.as_view(), name='blog_view')
    #path('blog/<int:pk>/', BlogDetail.as_view(), name='blog'),
    #path('blog/', views.BlogDetail.as_view(), name='blog_detail'),
    #path('blog/<int:pk>/', BlogDetail.as_view(), name='blog'),
    path('<slug:slug>', views.BlogDetail.as_view(), name='blog_detail'),
] '''