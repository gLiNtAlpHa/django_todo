from django.contrib import admin
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# Register your models here.
class CustomLoginView(LoginView):
    template_name = 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    # tasks = Task.objects.all()
    # for task in tasks:
    #     print(f'user taslisk: {task.user}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(f'related field: {context["tasks"].model.user.field.name}')
        # print(Task._meta.get_field("user").related_query_name())
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "base_app/task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['tittle','description','complete']
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)





class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['tittle','description','complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
