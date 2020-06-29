from rest_framework import serializers


from api.models import Employee
from drf_day1 import settings
#定义序列化的类，与模型是相对应的

class EmployeeSerilaizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()

    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        print(obj.gender, type(obj))
        # 性别是choices类型  get_字段名_display()直接访问值
        return obj.get_gender_display()

    # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        print(obj.pic)
        # http://127.0.0.1:8000/media/pic/000.jpg
        print("http://127.0.0.1:8000"+settings.MEDIA_URL + str(obj.pic))

        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))

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

    password = serializers.CharField()
    phone = serializers.IntegerField()

    #必须在方法中定义create，否则save无法完成
    def create(self, validated_data):
        # 方法中完成新增
        print(validated_data)
        return Employee.objects.create(**validated_data)
