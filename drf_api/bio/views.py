
from .models import Bio
from rest_framework.views  import APIView
from rest_framework.response import Response
from .serializers import BioSerializer


# Create your views here.

class BioList(APIView):
    """
    List all bios
    """
    def get(self,request):
        bio = Bio.objects.all()
        serializer=BioSerializer(bio,many=True, context={'request': request})
        return Response(serializer.data)

    


