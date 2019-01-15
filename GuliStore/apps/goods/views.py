from django.shortcuts import render,HttpResponse
from django.views import View
from .models import Student
from django.core import serializers
import json
from django.http import JsonResponse
# Create your views here.

class StudentsView(View):
    def get(self,request):
        all_students = Student.objects.all()
        data = serializers.serialize('json',all_students)
        data = json.loads(data)
        return JsonResponse(data,status=200,safe=False)

    def post(self,request):
        return HttpResponse('新建的对象', status=201)

class StudentsSingle(View):
    def get(self,request,pk):
        student = Student.objects.filter(id=pk)
        data = serializers.serialize('json', student)
        data = json.loads(data)
        return JsonResponse(data, status=200, safe=False)

    def put(self,request,pk):
        return HttpResponse('修改的对象', status=201)

    def delete(self,request,pk):
        Student.objects.filter(id=pk).delete()
        return HttpResponse(status=204)