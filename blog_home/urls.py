from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("about/", views.about_page, name='blog_home_about'),
    path("post/<int:pk>/", views.detailed_view, name='blog_home_detailed_view'),
    path("post/new/", views.BlogCreateView.as_view(), name='new_post'),
    path("post/<int:pk>/edit", views.BlogUpdateView.as_view(), name='post_edit'),
    path("post/<int:pk>/delete", views.BlogDeleteView.as_view(), name='post_delete'),
    path('accounts/logout/', views.custom_logout, name='logout_u'),
]