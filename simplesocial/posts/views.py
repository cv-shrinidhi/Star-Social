#  POSTS VIEWS.PY

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from posts import models
from groups import models as m
from posts import forms
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user','group') # mixin that allows to provide a tuple of related models
    # that is user that the post belongs to and the group to which the post belongs to

# we use select_related when object to be selected is single object, ie, OneToOneField or ForeignKey
# we use prefetch_related when object is a set of things, ie, ManyToManyField or reverse ForeignKey

# iss class me kuch samajh nhi aaya h check it later
class UserPost(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            # below line is eg of ORM (Object Relational Mappers)
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            # prefetch_related does a separate lookup for each relationship then does joining in python
            # see more in django docs for User.objects funtions CHECK!!!!
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
        # return context data object connected to whoever posted (the specific user)


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
        # the above query says that the username passed has to be the username
        # and has to be equal to the username of the models object


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        # this is done to connect the actual post to the user itself
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all') # after you delete a post it takes back to all the posts

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
