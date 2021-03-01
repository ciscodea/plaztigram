# Django
from django.urls import path

# View
from users import views


urlpatterns = [
    # Management
    path(
        route='users/login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='users/logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='users/signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='users/me/profile/',
        view=views.update_profile,
        name='update_profile'
    ),

    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(template_name='users/detail.html'),
        name='detail'
    ),
  

]
