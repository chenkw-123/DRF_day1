from rest_framework.views import APIView
from rest_framework.response import Response

from student.models import Student

from .serializer import EmployeeSerilaizer,EmployeeDeSerilaizer


class StudentAPIView(APIView):

    def get(self, request, *args, **kwargs):

        user_id = kwargs.get("pk")

        if user_id:
           #查询单个信息
           emp_obj = Student.objects.get(pk=user_id)

           #单个信息序列化, data（包装成字典返回，否则依旧无法获取）
           user = EmployeeSerilaizer(emp_obj).data
           print(user,type(user))
           return Response({
               "status" : 200,
               "message" : "查询单个学生信息",
               "result" : user,
           })
        else :
            #查询所有

            emp_list = Student.objects.all()
            # 序列化  所有用户，依旧需要返回字典，否则无法获取
            users = EmployeeSerilaizer(emp_list,many=True).data
            print(users)
            return Response({
                "status" : 200,
                "message" : "查询所有学生成功",
                "result" : users,
            })

    def post(self, request, *args, **kwargs):
        """
        新增单个对象
        """
        user_data = request.data
        print(user_data)
#数据入库时，必须对前台的数据进行校验
        if not isinstance(user_data,dict) or user_data=={}:
            return Response({
                "status" : 500,
                "message" : "数据有误，添加失败！"
            })

        #进行反序列化,data必须要传，否则会报错
        serializer = EmployeeDeSerilaizer(data=user_data)
        print(serializer)
        if serializer.is_valid():
            print(serializer.is_valid())
            emp_obj = serializer.save()
            # 将创建成功的学生实例返回到前端
            return Response({
                "status": 201,
                "msg": "学生添加成功",
                "results": EmployeeSerilaizer(emp_obj).data
            })
        else:
            print(serializer.is_valid())
            return Response({
                "status": 500,
                "msg": "学生添加失败!请查看详细信息",
                # 验证失败后错误信息包含在 .errors中
                "results": serializer.errors
            })