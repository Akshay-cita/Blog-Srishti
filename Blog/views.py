from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from Blog.forms import PostForm,CommentForm,UserForm,UserProfileInfoform
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from Blog.models import Post,Comment,UserProfileInfo
# Create your views here.
class AboutView(TemplateView):
    template_name='about.html'
class PostListView(ListView):
    model=Post
    template_name='post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
class  CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post
    template_name='post_form.html'
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=PostForm
    success_url=reverse_lazy('post_list')
class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name = 'blog/post_list.html'
    model=Post
    template_name='post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
##################################################
####################################################

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active :
                login(request,user)
                return HttpResponseRedirect(reverse('post_list'))

            else:
                return HttpResponse("ACCOUNT is NOT ACTIVE")
        else:
            print("Some tried to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("invalid login response")
    else:
        return render(request,'login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('about'))




def registerView(request):
    registered='False'

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered='True'
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoform()
    return render(request,'signup.html', {'user_form':user_form,
                                     'profile_form':profile_form,
                                     'registered':registered})









@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)





@login_required
def add_comment_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form=CommentForm(request,POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
