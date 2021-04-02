from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import * 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def students_list_dec(request):
    students = Student.objects.all()

    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def studentDetails(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
    serialize = StudentSerializer(data= request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)


@api_view(['PUT'])
def studentUpdate(request,pk):
    student = Student.objects.get(id=pk)

    serialize = StudentSerializer(instance=student,data= request.data)

    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)



class StudentregCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def student_list(request):
      if(request.method == 'GET'):
        students = Student.objects.all()

        serializer = StudentSerializer(students,many=True)
        return JsonResponse(serializer.data, safe = False)


# Create your views here.
@csrf_exempt
def article_list(request):

    if(request.method == 'GET'):
        articles = Article.objects.all()

        serializer = ArticleSerializer(articles,many=True)
        print(f'the data {serializer.data}')
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        print('Post request got hit')
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JSONParser(serializer.errors,status=400)

@csrf_exempt
def article_detail(request,pk):
    try:
        article = Article.objects.get(id=pk)
    
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if(request.method=='GET'):
         serializer = ArticleSerializer(article)
         return JsonResponse(serializer.data, safe = False)

    elif(request.method=='PUT'):
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JSONParser(serializer.errors,status=400)
    

    elif(request.method == "DELETE"):
        article.delete()
        return HttpResponse(status=204)

@csrf_exempt
def student_detail(request,pk):
    try:
        article = Student.objects.get(id=pk)
    
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    
    if(request.method=='GET'):
         serializer = StudentSerializer(article)
         return JsonResponse(serializer.data, safe = False)
    
    elif(request.method=='PUT'):
        data = JSONParser().parse(request)
        serializer = StudentSerializer(article,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JSONParser(serializer.errors,status=400)