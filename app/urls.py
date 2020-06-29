from django.urls import path

from app import views
urlpatterns = [

    path("user/",views.user),
    path("users/",views.UserView.as_view()),
    #匹配携带参数的路由
    path("users/<str:id>/",views.UserView.as_view()),

    path("api_users/",views.UserAPIView.as_view()),
    path("api_users/<str:pk>/", views.UserAPIView.as_view()),
    path("student/",views.StudentAPIView.as_view())
]