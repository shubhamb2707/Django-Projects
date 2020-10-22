from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import Student_Serializer

@api_view(["GET","POST"])
def Student_list(request):
	 if request.method == "GET":
	 	ins = Student.objects.all()
	 	ins_serializer = Student_Serializer(ins , many=True)
	 	return Response(ins_serializer.data)

	 elif request.method == "POST":
	 	ins_serializer = Student_Serializer(ins , many=True)
	 	if ins_serializer.is_valid():
	 		ins = Student.objects.all()
	 		ins_serializer.save()

	 		return Response(ins_serializer.data)
	 	else:
	 		ins = Student.objects.all()
	 		ins_serializer = Student_Serializer(ins , many=True)
	 		return Response(ins_serializer.errors)
