from datetime import timedelta
from django.urls.base import reverse
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import views as auth_view, get_user_model, authenticate, login
from UserManager import methods
from UserManager import forms as user_forms
from UserManager import models as user_models
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import views as auth_view
from django.http import HttpResponseRedirect


def dashboard(request):
    user_unread_posts = methods.get_user_unread_post(request)

    if request.method == 'POST':
        form = user_forms.EmailSendForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients_form = form.cleaned_data['receivers']

            recipients = str(recipients_form).split(',')
            sender = settings.EMAIL_HOST_USER

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/user/dashboard/')

    else:
        form = user_forms.EmailSendForm()

    context = {
        'user_unread_post': user_unread_posts,
        'email_sent_form': form
    }

    return render(request, 'UserManager/dashboard.html', context)


class LoginUserView(TemplateView):
    template_name = 'UserManager/login.html'

    def post(self, request, *args, **kwargs):
        login_form = user_forms.LoginForm(request.POST)

        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_email_confirm or user.is_active:
                    login(request, user)
                    print('user is logged in')
                    return HttpResponseRedirect(reverse('UserManager:dashboard'))
                elif not user.is_active:
                    messages.error(request, 'اکانت شما غیرفعال شده است')
                    return HttpResponseRedirect(reverse('UserManager:signin'))
                elif not user.is_email_confirm:
                    messages.error(request, 'ایمیل شما هنوز تایید نشده است')
                    return HttpResponseRedirect(reverse('UserManager:signin'))
                else:
                    return HttpResponseRedirect(reverse('UserManager:signin'))

        messages.warning(request, 'اطلاعات وارد شده صحیح نمی باشد')
        return HttpResponseRedirect(reverse('UserManager:signin'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['login_form'] = user_forms.LoginForm()

        return context


class SignUpUserView(TemplateView):
    template_name = 'UserManager/signup.html'

    def post(self, request):
        signup_form = user_forms.SignUpForm(request.POST)

        if signup_form.is_valid():
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password1']
            password2 = request.POST['password2']

            if password != password2:
                messages.warning(
                    request, 'رمز عبور و تکرار آن با هم برابر نیستند')
                return HttpResponseRedirect(reverse('UserManager:signup'))

            user_models.User.objects.create_user(
                email, first_name, last_name, password)
            print('user created')
            messages.success(
                request, 'ثبت نام شما با موفقیت انجام شد و میتوانید وارد حساب کاربری خود شوید')
            return HttpResponseRedirect(reverse('UserManager:signin'))

        messages.warning(
            request, 'اطلاعات وارد شده صحیح نمی باشد یا در فرم مشکلی به وجود امده است')
        return HttpResponseRedirect(reverse('UserManager:signup'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['signup_form'] = user_forms.SignUpForm()

        return context
