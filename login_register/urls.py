"""
URL configuration for login_register project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from posts import views as post_views
from posts.views import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, UserPostListView
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.PostListView.as_view(template_name="posts/index.html"), name='index',
         kwargs={'navbar': 'home'}),
    path('register/', user_views.register, name='register',),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login',
         kwargs={'navbar': 'login'}),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout',
         kwargs={'navbar': 'logout'}),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
    path("search", post_views.PostSearch.as_view(template_name="posts/search_results.html"), name='search'),
    path('post/new/', PostCreateView.as_view(), name='post-create', kwargs={'navbar': 'new'}),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

]
