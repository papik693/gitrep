from rest_framework import serializers
from .models import Books, ImportBooks


class ImportBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImportBooks
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'