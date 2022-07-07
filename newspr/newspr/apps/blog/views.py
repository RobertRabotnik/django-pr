from django.shortcuts import render, redirect
from django.views.generic import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from newspr.apps.blog.forms import CommentAddForm
from blog.models import * 
from django.db.models import Q
from users.models import CustomUser

def home_page(request):
    posts = Post.objects.order_by('-pub_date')[:3]
    return render(request,'main.html',context={'posts':posts})

# posts

class ListPost(ListView):
    template_name = 'blog/list_posts.html'
    model = Post 

    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.model.objects.order_by('-pub_date')
        search = self.request.GET.get('search')
        if search:
            context['posts'] = self.model.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
            return context
        
        return context

class DetailPost(DetailView):
    template_name = 'blog/detail_post.html'
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        context['comments'] = context['post'].comment_set.order_by('-pub_date')
        return context 


# Comments 

class CommentAdd(LoginRequiredMixin, FormView):
    template_name = 'blog/comment_add.html'
    login_url = 'users:login'
    model = Comment
    form_class = CommentAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context   
    
    def form_valid(self,form,**kwargs):
        request_user = CustomUser.objects.get(id=self.request.user.id)
        post = Post.objects.get(pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.user = request_user
        comment.post = post
        comment.save()
        return super().form_valid(form)

    def get_success_url(self,**kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        return reverse('blog:detail_post',args=(post.id,))
   

# categorys

class ListCategorys(ListView):
    template_name = 'blog/list_cat.html'
    model = Category 
    context_object_name = 'cats'

class CategoryPosts(ListView):
    template_name = 'blog/posts_cat.html'
    model = Category 

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs) 
        context['cat'] = self.model.objects.get(slug__iexact=self.kwargs['slug'])
        context['posts'] = context['cat'].posts.order_by('-pub_date')
        return context 


