from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView ,FormView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# Create your views here.
class IndexView (TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'sajjad'
        context['posts'] = Post.objects.all()
        return context
    
    

class PostListView (PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'
    
class PostDetailView (LoginRequiredMixin,DetailView):
    model = Post
    

...
# class PostCreateView (FormView):
#     template_name = 'contact.html'
#     form_class = PostForm
#     success_url = '/blog/post/'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
...
class PostCreateView (LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','status','category','published_date']
    success_url = '/blog/post/'
    # template_name = 'contact.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView (LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    template_name = 'contact.html'
    

class PostDeleteView (LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'