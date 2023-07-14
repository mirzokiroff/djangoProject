from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, HttpResponse, redirect
from main.models import Subscribe, Service
from main.forms import EmailForm
from django.views.generic import CreateView
from django.db.models import Q
from .forms import SearchForm
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def search_results(query):
    pass


def search(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = search_results(query)

    context = {
        'form': form,
        'results': results,
        'no_results': False
    }

    if not results:
        context['no_results'] = True

    return render(request, 'search.html', context)


def home(request):
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     searcher = MyUser.objects.filter(Q(title__icontains=q) | Q(tags__icontains=q))
    #
    # else:
    #     searcher = MyUser.objects.all().order_by('-id')
    #     q = None
    services = Service.objects.all()
    code = EmailForm.objects
    contex = {"objects": code}
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        EmailForm.objects.create(
            name=name, phone_number=phone, email=email, message=message
        )
    # return render(request, 'index.html', (contex, "base.html"), {"services": services})
    return render(request, 'index.html')
    # return render(request, 'index.html', contex {"searcher": searcher, 'q': q})


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


from main.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1
                    )
                    user.save()
                    return redirect('login')
            else:
                messages.error(request, 'Passwords are not equal!')
                return redirect('register')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'register_form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Username or password not found')
            return redirect('login')

    return render(request, "login.html")


# def form(request):
#     # Forgot Password functionality
#     if request.method == 'GET' and 'forgot_password' in request.GET:
#         form = PasswordResetForm(request.GET)
#         if form.is_valid():
#             form.save(request=request)
#             messages.success(request, 'A password reset link has been sent to your email.')
#             return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('index')


class EmailView(CreateView):
    template_name = 'base.html'
    model = Subscribe
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):
        # Forma to'g'ri vaqtida yuborilgan bo'lsa
        # Email ni database ga saqlash
        email = form.cleaned_data['email']
        self.object = form.save()  # Email ma'lumotini saqlash
        return super().form_valid(form)


def send(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Ma'lumotlarni yuborish
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')


class ImageUpdateView(UpdateView):
    fields = ('photo')
