from rest_framework import serializers
from users.models import Hgjkhglkj


class HgjkhglkjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hgjkhglkj
        fields = "__all__"
