from dataclasses import field
from rest_framework import serializers
from .models import Coordination,Client

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Client
        fields='__all__'
        
class CoordinateSerializer(serializers.ModelSerializer):
    clients=serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Coordination
        fields='__all__'
        #연결된 몇개의 외래키까지 보여줄 것인지 설정할 수 있다.
        depth=1
        
