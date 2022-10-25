from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from addInfo.models import PassedPerson
import json
from django.core import serializers

# Create your views here.

@csrf_exempt   #跨域设置:绕开CSRF验证
def register(request):
    if request.method == 'POST':
        # post的请求是json格式
        data = json.loads(request.body)
        name = data.get('name')
        birth = data.get('date1')
        passDate = data.get('date2')
        gender = data.get('gender')
        desc = data.get('desc')

        print('post: ', name, birth, passDate, gender, desc)

        #(在此处添加验证)

        person = PassedPerson(name=name, birth=birth, passDate=passDate, gender=gender, desc=desc)
        person.save()
        return JsonResponse({'errno': 0, 'msg': '添加成功'})
    
    else:
        return JsonResponse({'errno': 2, 'msg': '请求方式错误, 请用POST'})



@csrf_exempt
def searchName(request):
    if request.method == 'GET':
        # get请求是text/html格式
        name = request.GET.get('name')
        print('(backend) the inputName is:', name)

        Data = PassedPerson.objects.filter(name=name)
        people = serializers.serialize("json", Data.all())
        
        return JsonResponse({'errno': 0, 'msg': 'GET reached at backend successfully!'})
    else:
        return JsonResponse({'errno': 2, 'msg': 'wrong GET!'})
