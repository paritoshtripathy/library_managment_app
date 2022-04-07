from pyexpat import model
from attr import field
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from matplotlib.style import context

from base.models import Library_DB

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authencited_user = True

    def get_success_url(self):
        return reverse_lazy('admin-panel')

class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin-panel')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self,*args, **kwargs ):
        
        return super(Register, self).get(*args, **kwargs)    


class StudentView(ListView):
    model = Library_DB
    context_object_name = 'books'
    template_name = 'student_view.html'
    


class BookList(ListView):
    model = Library_DB
    context_object_name = 'books'
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user'] = context['books'].filter(user=self.request.user)
    
        return context

class BookDetails(LoginRequiredMixin,DetailView):
    model = Library_DB
    context_object_name = 'book'

    template_name = 'book_details.html'

class BookAdd(LoginRequiredMixin,CreateView):
    model = Library_DB
    template_name = 'book_add.html'
    fields = ['book_title','author']
    success_url = reverse_lazy('books')

class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Library_DB
    fields = ['book_title','author']
    success_url = reverse_lazy('books')
    template_name = 'book_add.html'

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Library_DB
    context_object_name = 'book'
    success_url = reverse_lazy('admin-panel')
    template_name = 'book_del.html'