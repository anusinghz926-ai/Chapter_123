from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', views.PostListView.as_view(), name='post_list'),
    
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),
    
    # URL for sharing posts via email
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    
    # URL for posting comments
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]