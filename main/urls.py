from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.views import home, about, service, contact, login, Subscribe, EmailView, search, send
from main.views import register, logout

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('email/', EmailView.as_view(), name='email'),
    path('email/', Subscribe, name='email'),
    path('register/', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('search/', search, name='search'),
    path('send/', send, name='send'),
    # path('Forgot password/', form, name='Forgot password?')
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
]
