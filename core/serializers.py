from .models import LittleLemonUser
from rest_framework import serializers

class LittleLemonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LittleLemonUser
        fields = [
            'username',
            'email',
            'groups',
            'id'
        ]
        depth = 1
    
    @staticmethod
    def serialize(model, many):
        return LittleLemonUserSerializer(model, many=many).data
