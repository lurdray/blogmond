from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # None    url(r'^eachassessment/(?P<assessment_id>\d+)/$', views.EachAssessmentView, name="eachassessment"),
    path('', views.index, name='index'),
    
    #url(r'^breakingdetail/(?P<int:breaking_id>\d+)/$', views.BreakingDetail, name='breaking_detail'),  all_post_detail
    
    path("allpost", views.AllPost, name="all_post"),
    path("allseries/", views.AllSeries, name="all_series"),
    path("alltv/", views.AllTv, name="all_tv"),
    
    path('post_detail/<int:post_id>/', views.PostDetail, name='post_detail'),
    path('breaking_detail/<int:breaking_id>/', views.BreakingDetail, name='breaking_detail'),
    path('tv_detail/<int:tv_id>/', views.TvDetail, name='tv_detail'),
    path('series_detail/<int:series_id>/', views.SeriesDetail, name='series_detail'),
    
    path("postblog/", views.PostBlog, name="postblog"),
    path("posttv/", views.PostTv, name="posttv"),
    path("postbreaking/", views.PostBreaking, name="postbreaking"),
    path("postseries/", views.PostSeries, name="postseries"),
   
]
