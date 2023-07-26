from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView
from httpx import get, post
from apps.forms import RegisterForm, ServiceForm, Portfolioform, TestimonialForm, PriceForm, BlogForm
from apps.models import User, Service, Portfolio, Testimonial, Blog, Price


def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot5941896545:AAGU9xMqtM5iDY3gMEeuxshTJF07Q7XdGhI/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
    print(response.text, response.status_code)


# Create your views here.

def home(request):
    if request.POST:
        m = f'''📥 New mail\n📩 From: {request.get['email']}\n👱 Name: {request.get['name']}\n📄 Message: {request.get['messages']}'''
        send_message(1038185913, m)

    service = Service.objects.all()
    blog = Blog.objects.all()
    portfolio = Portfolio.objects.all()
    price = Price.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'index.html', {'service': service, 'blog': blog, 'portfolio': portfolio, 'price': price,
                                          'testimonial': testimonial})


class Login(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
            return redirect(reverse_lazy('home'))
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return redirect(reverse_lazy('home'))


class Register(CreateView):
    template_name = 'register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class ServiceView(CreateView):
    template_name = 'add_service.html'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('home')


class PortfolioView(CreateView):
    template_name = 'add_portfolio.html'
    model = Portfolio
    form_class = Portfolioform
    success_url = reverse_lazy('home')


class TestimonialView(CreateView):
    template_name = 'add_testimonial.html'
    model = Testimonial
    form_class = TestimonialForm
    success_url = reverse_lazy('home')


class PriceView(CreateView):
    template_name = 'add_price.html'
    model = Price
    form_class = PriceForm
    success_url = reverse_lazy('home')


class BlogView(CreateView):
    template_name = 'add_blog.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('home')
