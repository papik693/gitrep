from .views import BooksViewSet, AddBook, ImportBook
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'addbook', AddBook, basename='addbooks')
router.register(r'importbook', ImportBook, basename='importbooks')

urlpatterns = router.urls
