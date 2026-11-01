from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter ,SimpleRouter


app_name = 'api_v1'
router = DefaultRouter()
router.register('post',views.PostModelViewSet,basename='post')
router.register('category',views.CategoryModelViewSet,basename='category')

urlpatterns = router.urls





# urlpatterns = [
#     # path('post/',views.postList,name='post_list'),
#     # path('post/<int:id>/', views.postDetail, name='post_detail'),
#     # path('post/',views.PostList.as_view(),name='post_list'),
#     # path('post/<int:pk>/',views.PostDetail.as_view(), name='post_detail'),
    
    
    
#     path('post/',views.postViewset.as_view({'get':'list','post':'create'}), name='post_detail'),
#     path('post/<int:pk>/',views.postViewset.as_view({'get':'retrieve','put':'update','patch':'partial_update'
#             ,'delete':'destroy'}),name='post_detail'),
# ]
    