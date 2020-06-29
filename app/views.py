from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.parsers import MultiPartParser,JSONParser,FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import settings
from app.models import User

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

@csrf_exempt
# @csrf_protect  全局禁用csrf的时候，使用protect可以使某个视图函数单独添加csrf认证
def user(request):
    if request.method == "GET":
        print("GET SUCCESS  查询")
        username = request.GET.get("username")
        print(username)
        return HttpResponse("GET SUCCESS")
    elif request.method == "POST":
        print("POST SUCCESS  添加")
        return HttpResponse("POST SUCCESS")
    elif request.method == "PUT":
        return HttpResponse("PUT SUCCESS")
    elif request.method == "DELETE":
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")



@method_decorator(csrf_exempt, name="dispatch") #免除crsf认证
class UserView(View):

    def get(self,request,*args,**kwargs):

        #查询单个用户
        id = kwargs.get("id")
        # if id:   #查询成功
        if id:
            value = User.objects.filter(id=id).values("username","password","gender").first()
            # value = User.objects.get(id=id)
            if value:
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": value
                })
        else:
            users = User.objects.all().values("username","password","gender")
            if users:
                return JsonResponse({
                    "status": 200,
                    "message": "查询全部用户成功",
                    "results": list(users)
                })
        return JsonResponse({
            "status" : 500,
            "message" : "未查询到用户"
        })
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user_one = User.objects.create(username=username,password=password)
            return JsonResponse({
                "status":201,
                "message":"创建用户成功",
                "result":{"username":user_one.username,"password":user_one.password,"gender":user_one.gender}
            })
        except:
            return JsonResponse({
                "status":500,
                "message":"创建用户失败",
            })


    def put(self,request,*args,**kwargs):
        print("修改成功")
        return HttpResponse("修改成功")
    def delete(self,request,*args,**kwargs):
        print("删除成功")
        return HttpResponse("删除成功")



class UserAPIView(APIView):


    #局部配置渲染器，优先级更高
    # renderer_classes = (BrowsableAPIRenderer,)

    def get(self, request, *args, **kwargs):

        user_id = kwargs.get("pk")
        user_val = User.objects.get(pk=user_id)

        # print("DRF GET VIEW")
        print(request)   #drf视图使用request，django内置的无法使用，其中包含了原生的request
        print(request._request)  # 可以通过_request方法来访问原生的django的request对象
        #通过DRF视图的request获取对象
        print(request.GET)
        #通过django的request获取对象
        print(request._request.GET)
        # 通过quer_params来获取参数
        print(request.query_params)

        # 获取路径传参
        user_id = kwargs.get("pk")

        return Response("SUCESS")


    def post(self, request, *args, **kwargs):
        # print("DRF POST VIEW")

        print(request._request.POST)  #POST  django原生的request获取对象
        print(request.POST)  #通过DRF视图的request获取对象

        print(request.data)  # 可以获取多种格式的参数 DRF 扩展的请回去参数  兼容性最强
        #例如 用row方式 就只能用.data方式获取

        return Response("post SUCESS")



class StudentAPIView(APIView):
    #解析器的局部使用
    # parser_classes = [MultiPartParser]
    parser_classes = [FormParser]
    # parser_classes = [JSONParser]
    def post(self, request, *args, **kwargs):
        print("POST方法")
        # print(request.POST)
        print(request.data)

        return Response("SUCCESS")
