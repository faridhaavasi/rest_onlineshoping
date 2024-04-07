from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer, CartAddSerializer
from product.models import Product
from .cart import Cart


class CartViewApi(APIView):
    serializer_class = CartSerializer

    def get(self, request):
        cart = Cart(request)

        ser = self.serializer_class(cart)
        return Response(ser.data)
class CartAddViewApi(APIView):
    serializer_class = CartAddSerializer
    def post(self, request,):
        cart = Cart(request)
        ser = self.serializer_class(data=request.POST)
        if ser.is_valid():
            product = Product.objects.get(id=ser.validated_data['id_of_product'])
            cart.add(product, quantity=ser.validated_data['quantity'])
            return Response({'massage': 'added'})
        return Response(ser.errors)


