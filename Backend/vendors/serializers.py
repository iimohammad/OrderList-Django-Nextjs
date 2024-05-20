from rest_framework import serializers
from vendors.models import ResponseOrders
from userauths.serializers import UserSerializer
from orders.serializers import OrderSerializer


class ResponseOrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = ResponseOrders
        fields = [
            'user', 'response_date', 'order', 'price', 'deliver_time', 'quantity', 'description', 'factor'
        ]
        read_only_fields = ['response_date']  

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
