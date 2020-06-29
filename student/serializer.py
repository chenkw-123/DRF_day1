from rest_framework import serializers


from student.models import Student
from drf_day1 import settings
#定义序列化的类，与模型是相对应的

class EmployeeSerilaizer(serializers.Serializer):
    username = serializers.CharField()
    # gender = serializers.IntegerField()

    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        print(obj.gender, type(obj))
        return obj.get_gender_display()

#反序列化
class EmployeeDeSerilaizer(serializers.Serializer):
    # username = serializers.CharField()

    username = serializers.CharField(

        max_length=8,
        min_length=2,
        error_messages= {
            "max_length" : "长度过长",
            "min_length" : "长度太短",
        }
    )
    phone = serializers.IntegerField()

    #必须在方法中定义create，否则save无法完成
    def create(self, validated_data):
        # 方法中完成新增
        print(validated_data)
        return Student.objects.create(**validated_data)
