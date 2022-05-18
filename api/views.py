from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .serializers import MessageSerializer

from message.models import Message

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def createMessage(request):
    serializer = MessageSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data)

    return Response(serializer.errors)