from django.shortcuts import render
from rest_framework.views import APIView
from Book.models import Book
from Book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from Book.permissions import IsAdminOrReadOnly
from django.db.models import Q
from utils import paginations
# Create your views here.

class BookApi(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self, request):
            """
                get all  Book and filter by title and use paginations
            """
            search = request.query_params.get('search')
            page = request.query_params.get('page')
            qty = request.query_params.get('qty')

            sneppit = Book.objects.all().order_by('-id')

            if search:
                sneppit = sneppit.filter(
                    Q(title__icontains=search)
                )
            output = BookSerializer(sneppit, many=True).data
            if page and qty:
                output = paginations.page(output, qty, page)
            return Response(data={'data': output})

    def post(self, request):
            """
                create single  Book
            """
            data = request.data
            user = request.user
            title = data.get('title')
            subtitle = data.get('subtitle')
            author = data.get('author')


            payload = {
                "user": user.id,
                "title": title,
                "subtitle": subtitle,
                "author": author

            }

            serializer = BookSerializer(data=payload)

            if not serializer.is_valid():
                return Response(serializer.errors)
        
            serializer.save()
            return Response(serializer.data)
        
    def patch(self, request,pk):
            """
                edit single  Book
            """
            try:
                sneppit = Book.objects.get(id=pk)
            except Exception:
                return Response({'error': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer(sneppit, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors)
            serializer.save()
            return Response(serializer.data)

    def delete(self, request,pk):
            """
                delete single  Book
            """

            sneppit = Book.objects.get(id=pk)
            sneppit.delete()

            return Response({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
