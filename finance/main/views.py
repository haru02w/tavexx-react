from django.db.models import Sum, Q, F
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from main.models import OperationModel
from main.serializers import OperationSerializer

# Create your views here.


class OperationViewset(ModelViewSet):
    queryset = OperationModel.objects.all()
    serializer_class = OperationSerializer
    lookup_value_regex = "[^/]+"


class OperationStats(ViewSet):

    lookup_value_regex = "[^/]+"

    def list(self, request):
        response = OperationModel.objects.aggregate(
            total_entrada=Sum("valor", filter=Q(tipo=OperationModel.TypeChoices.DEPOSIT)),
            total_saida=Sum("valor", filter=Q(tipo=OperationModel.TypeChoices.WITHDRAWAL)),
            total=F("total_entrada") - F("total_saida"),
        )
        return Response(response)
