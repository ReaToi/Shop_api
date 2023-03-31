from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from rest_framework import status


@api_view(["GET"])
def review_list_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def review_detail_api_view(request):
    try:
        review = Review.objects.all(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(["GET"])
def category_list_api_view(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request):
    try:
        category = Category.objects.all(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': "Category not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def product_derail_api_view(request, id):
    try:
        product = Product.objects.all(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': "Product not found!"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)

