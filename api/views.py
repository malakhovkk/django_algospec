# from django_algospec.api import serializers
# from .models import Person
# from rest_framework import viewsets
# from rest_framework import permissions
# from api.serializers import PersonSerializer
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.hashers import make_password

# Create your views here.
# class PersonAPIView(APIView):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     def get(self, request):
#         person = Person.objects.all()
#         # nickname = request.POST['nickname']
#         serializer = PersonSerializer(person, many=True)
#         return Response(serializer.data)
#     # def get(self, )
#     def post(self, request):
#         # email = self.cleaned_data["email"]
#         serializer = PersonSerializer(data=request.data)
#         # res = Person.objects.filter(email=email)
#         # if not res:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class LogIn(APIView):
#     def post(self, request):
#         print("LogIn")
#         u =  request.POST['username']
#         p = request.POST['password']
#         print(make_password(p))
#         user_obj = Person.objects.filter()
#         # user = Person.objects.get(username=u) 
#         # this checks the plaintext password against the stored hash 
#         # correct = user.check_password(make_password(p))  
#         #res = Person.objects.filter(username=u, password=p)
#         print(u)
#         if not user_obj:
#             Response(status=status.HTTP_401_UNAUTHORIZED)
#         return Response(status=status.HTTP_200_OK)
#         #header = request.header['Authorization']  
#         #print(header)
# class Add(APIView):
#     def post(self, request):
#         print("LogIn")
        #header = request.header['Authorization']  
        #print(header)

# class PersonGetAPI(APIView):
#     def get(self, request):
#         person = Person.objects.all()
#         nickname = request.POST['nickname']
#         password = make_password(request.POST['password'])
#         res = Person.objects.filter(nickname=nickname, password=password)
#         if not res:
#            return  Response( status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response( status=status.HTTP_200_OK)
    # queryset = Person.objects.all()
    # serializer_class = PersonSerializer
    # permission_classes = [permissions.IsAuthenticated]
    