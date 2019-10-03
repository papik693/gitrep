from rest_framework import mixins
from rest_framework import viewsets
from .serializers import BooksSerializer, ImportBooksSerializer
from .models import Books
import json
from urllib.request import urlopen
from rest_framework.decorators import action
from django_filters import rest_framework as filters
import urllib
from rest_framework.response import Response


def newbook(data):
    for item in data['items']:
        book = Books()
        title = item['volumeInfo'].get('title', 0)
        book.title = item['volumeInfo'].get('title', 0)
        book.authors = item['volumeInfo'].get('authors', 0)
        book.publishedDate = item['volumeInfo'].get('publishedDate', 0)
        book.industryIdentifiers = item['volumeInfo'].get('industryIdentifiers', 0)
        book.pageCount = item['volumeInfo'].get("pageCount", 0)
        book.imageLinks = item['volumeInfo'].get('imageLinks', 0)
        book.language = item['volumeInfo'].get('language', 0)
        if Books.objects.filter(title=title).exists():
            pass
        else:
            book.save(title)


class BooksFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    authors = filters.CharFilter(lookup_expr='icontains')
    language = filters.CharFilter(lookup_expr='icontains')
    publishedDate = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Books
        fields = ('title', 'authors', 'language', 'publishedDate')


class BooksViewSet(viewsets.ReadOnlyModelViewSet):
    model = Books
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    data = json.load(urlopen('https://www.googleapis.com/books/v1/volumes?q=Hobbit'))
    filterset_class = BooksFilter
    newbook(data)


class AddBook(viewsets.GenericViewSet, mixins.CreateModelMixin,):
    model = Books
    serializer_class = BooksSerializer
    lookup_field = 'pk'
    @action(detail=True, methods=['post'])
    def post(self, request, pk=None):
        book = self.get_object()
        serializer = BooksSerializer
        book.save()
        return Response()


class ImportBook(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = ImportBooksSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        url = 'https://www.googleapis.com/books/v1/volumes?q='
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        q = urllib.parse.quote(serializer.data['q'])
        intitle =       urllib.parse.quote(serializer.data['intitle'])
        inauthor =      urllib.parse.quote(serializer.data['inauthor'])
        inpublisher =   urllib.parse.quote(serializer.data['inpublisher'])
        subject =       urllib.parse.quote(serializer.data['subject'])
        isbn =          urllib.parse.quote(serializer.data['isbn'])
        lccn =          urllib.parse.quote(serializer.data['lccn'])
        oclc =          urllib.parse.quote(serializer.data['oclc'])
        url = 'https://www.googleapis.com/books/v1/volumes?q='+q
        if intitle != '':
            url = url+'&intitle='+intitle
        if inauthor != '':
            url = url+'&inauthor='+inauthor
        if inpublisher != '':
            url = url+'&inpublisher='+inpublisher
        if subject != '':
            url = url+'&subject='+subject
        if isbn != '':
            url = url+'&isbn='+isbn
        if lccn != '':
            url = url+'&lccn='+lccn
        if oclc != '':
            url = url+'&oclc='+oclc
        newbook(json.load(urlopen(url)))
        return Response()

    def get_queryset(self):
        pass
