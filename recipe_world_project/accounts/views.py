from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginView(LoginView):
    # Redirect user if successful login. Default is False.
    redirect_authenticated_user = True

    def get_success_url(self):
        # The URL the user will be redirected to. 
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        # Form_invalid() is called once the login is failed.
        # In the form_invalid(), we create a flash message and rerender the login form.
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
