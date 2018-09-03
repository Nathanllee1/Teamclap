from django.urls import path

from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('<int:pk>/edit/',
        views.BlogUpdateView.as_view(), name='article_edit'),

    path('<int:pk>/',
        views.BlogDetailView.as_view(), name='article_detail'),

    path('<int:pk>/delete/',
        views.BlogDeleteView.as_view(), name='article_delete'),
]
