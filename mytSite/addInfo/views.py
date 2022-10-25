from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from addInfo.models import PassedPerson
import json

# Create your views here.

@csrf_exempt   #跨域设置:绕开CSRF验证
def register(request):
    if request.method == 'POST':
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


