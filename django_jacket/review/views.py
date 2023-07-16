from django.contrib.auth.models import User

from .models import Review
from .serializers import ReviewSerializer

from product.models import Product

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status, permissions, authentication


class ReviewDetail(APIView):
    def get(self, request, product_slug, format=None):
        reviews = self.get_object(product_slug)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def get_object(self, product_slug):
        try:
            return Review.objects.filter(product=product_slug)
        except Review.DoesNotExist as e:
            print(e)
    

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def sendReview(request):    
    print(User.objects.get(username=request.user.username))
    serializer = ReviewSerializer(data=getData(request))

    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def getData(request):
    reviewData = request.data
    reviewData['user'] = User.objects.get(username=request.user.username).id
    
    return reviewData
