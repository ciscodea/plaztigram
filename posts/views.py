# Django
from django.urls import  reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

#Forms
from posts.forms import PostForm, CommentForm

# Models

from posts.models import Post, Comment

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('posts:feed'))


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    queryset = Post.objects.all()
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'



class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a ew Post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and prfile to context"""
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile 
        return context


class CreateCommentView(LoginRequiredMixin, CreateView):
    # Create a ew Post
    template_name = 'posts/add_comment.html'
    form_class = CommentForm
    queryset = Post.objects.all()
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        # Add user and prfile to context
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile 

        return context