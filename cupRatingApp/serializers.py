from rest_framework import serializers

from .models import Cup

# this is the serializer for the Cup model
class CupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = '__all__'
        depth = 0

    def save(self):
        new_cup = Cup(
            name=self.validated_data['name'],
            description=self.validated_data['description'],
            image=self.validated_data['image'],
            price=self.validated_data['price'],
            rating=self.validated_data['rating']
        )
        new_cup.save()
        return new_cup
