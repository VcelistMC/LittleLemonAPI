from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.


@api_view()
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response({"user": model_to_dict(request.user)})
