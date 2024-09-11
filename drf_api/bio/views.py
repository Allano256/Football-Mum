from django.http import Http404
from .models import Bio
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import BioSerializer
# from rest_framework.decorators import api_view, permission_classes


# Create your views here.

class BioList(APIView):
    """
    List all profiles created in the database.
    """
    def get(self,request):
        bio = Bio.objects.all()
        serializer=BioSerializer(bio,many=True, context={'request': request})
        return Response(serializer.data)

    
class BioDetail(APIView):
    """
    This function will return one profile based on the ID.
    """
    def get_object(self):
        try:
            return Bio.objects.get(pk=self.kwargs['pk'])
        except Bio.DoesNotExist:
            raise NotFound('Bio does not exist')


    def get(self,request, pk):
        bio = self.get_object()
        serializer = BioSerializer(bio, context={'request': request})
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    def get_object(self):
        try:
            return Bio.objects.get(pk=self.kwargs['pk'])
        except Bio.DoesNotExist:
            raise NotFound('Bio does not exist...')
        
    def put(self, request, pk):
        """
        This function will update a profile,nOT WORKING RIGHT NOW.
        """
        try:
            Bio.objects.get(pk=self.kwargs['pk'])
        except Bio.DoesNotExist:
            raise NotFound('Bio does not exist!!!')


        bio =self.get_object()
        serializer = BioSerializer(bio, data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    

