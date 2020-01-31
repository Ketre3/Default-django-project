from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountInfoForm, AccountLoginForm, AccountRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.generic import UpdateView, CreateView #, DetailView
from .models import Account
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse, reverse_lazy


class Login(LoginView):
    template_name = 'login_register.html'
    authentication_form = AccountLoginForm

    extra_context = {'register_form': AccountRegisterForm}
    success_url = reverse_lazy("product:all")


class RegisterView(CreateView):
    template_name = 'login_register.html'
    form_class = AccountRegisterForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['register_form'] = context['form']
        context['form'] = AccountLoginForm
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # here could be better logic (using email confirmation for example)
        return reverse("account:confirm", kwargs={"pk":self.object.pk})


class UserInfo(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountInfoForm
    template_name = 'credits.html'
    login_url = reverse_lazy("account:login")
    success_url = reverse_lazy("account:info")

    def get_object(self, queryset=None):
        return self.request.user

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     sumka = kwargs['data']['avatar']
    #     print(sumka)
    #     print(type(sumka))
    #     return kwargs


class Logout(LogoutView):
    template_name = 'logout.html'
    login_url = reverse_lazy("account:login")


@user_passes_test(lambda u: not u.is_active)
def confirm_account(request, pk):
    if request.user.is_authenticated:
        return redirect("account:info")
    user = get_object_or_404(Account, pk=pk)
    user.is_active = True
    user.save()
    login(request, user)
    return render(request, 'confirm.html')
