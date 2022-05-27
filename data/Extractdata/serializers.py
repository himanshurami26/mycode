from rest_framework import serializers

from .models import ContryDetails,Category,StudentDetails,filedetails


class UploadsopSerializer(serializers.Serializer):
    files = serializers.FileField()


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContryDetails
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class StudentDetailsserializer(serializers.ModelSerializer):

    country_id = serializers.RelatedField(source='ContryDetails', read_only=True)
    category_id = serializers.RelatedField(source='Category', read_only=True)
    
    class Meta:
        model = StudentDetails
        fields = '__all__'


class FiledetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = filedetails
        fields = '__all__'
