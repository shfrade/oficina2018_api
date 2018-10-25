from rest_framework import viewsets
from .serializers import ProdutoSerializer
from .models import Produto


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Produto.objects.all().order_by('-quantidade')
    serializer_class = ProdutoSerializer
