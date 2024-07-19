 # serializers is used to send data as json
from rest_framework import serializers
from .models import Todo
   
class TodoSerializer(serializers.ModelSerializer):
     class Meta: #to declare which data i wanna send
        model = Todo
        fields = '__all__'
        #fields = ('name','price','brand')

    

