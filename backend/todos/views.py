
from django.shortcuts import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

def home (request):
    return HttpResponse('Hi there')


class TaskAPIView(APIView):
    # lookup_field = "id"
    def get(self, request):
        tasks= Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"status":200, "data": serializer.data })

    def post(self, request):
        data= {
            'title': request.data.get('title'),
            'description': request.data.get('description')
        }
        serializer = TaskSerializer(data=data)
        if not serializer.is_valid():
            return Response ({"status":"Invalid Data."})

        serializer.save()
        return Response({'status':200 , 'message': "task created successfully."})
        


    def put(self, request):
        id = request.data.get('id')
        task= Task.objects.get(pk=id)
        if not task:
            return Response({"response":"invalid id"})

        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'completed': request.data.get('completed')
        }

        serializer= TaskSerializer(instance=task, data= data, partial=True)
        if not serializer.is_valid():
            return Response({"status":"forbidden"})

        serializer.save()
        return Response({'status':200 , 'message': "task updated successfully."})


        
    def delete(self,request, pk , format=None):
        try:
            # id = request.data.get('id')
            id=pk
            task= Task.objects.get(pk=id)

            if not task:
                return Response({"Response":"Invalid id"})
            
            task.delete()
            return Response({'status':200 , 'message': "task deleted successfully."})

        except Exception as e:
            print(e)
     

