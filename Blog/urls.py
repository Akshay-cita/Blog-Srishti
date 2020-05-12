from django.urls import path,re_path
from Blog import views
urlpatterns=[
    path('about/',views.AboutView.as_view(),name='about'),

    path('second/',views.registerView,name="registerView"),
    path('login/',views.login_view,name="login_view"),
    path('logout/',views.logout_view,name='logout_view'),
    path('postlist/',views.PostListView.as_view(),name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_post,name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    re_path(r'^comment/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
