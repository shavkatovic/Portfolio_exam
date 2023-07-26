from django.contrib.auth.hashers import make_password
from django.forms import ModelForm

from apps.models import User, Service, Portfolio, Testimonial, Price, Blog


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'about', 'position', 'password')

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'description')


class Portfolioform(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'cotegory', 'image')


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ('name', 'description')


class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ('basic', 'premium')


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'title', 'description')
