from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

from rest_framework import status

def exception_handler(exc,context):
    # print(exc,"----",context)

    error = "%s %s %s" % (context["view"],context["request"].method,exc)
    print(error)


    #先让DRF的内部程序执行，看能否处理异常，根据reponse的返回值来确定异常是否处理
    response = drf_exception_handler(exc,context)
    #如果位NONE则未处理异常，自定义处理
    if response is None:
        return Response(
            {"error_message":"程序有误，稍后重试"},
            #自定义状态码
            # status=500,exception=None
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,exception=None
                        )
        # return Response({"error_msg": error})  #异常具体信息，一般不让用户看

    # 如果Response不为空  说明异常信息已经被DRF处理了 直接返回即可
    return response
