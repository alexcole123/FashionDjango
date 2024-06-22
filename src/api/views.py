from django.shortcuts import render
from api.models import ClothingSerializer
from clothing.models import ClothingModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Get JSON of all cloths
@api_view(["GET"]) #Expose following function only on GET request
def get_cloths(request):
    try:
        #Get all cloths from database
        cloths = ClothingModel.objects.all()

        #Create a serializer for converting cloths into json:
        serializer = ClothingSerializer(cloths, many = True) #many = true --> convert into list

        #Response back the serializer json:
        return Response(serializer.data)
    except Exception as err:
        json = {"error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#Get JSON of one cloth:

@api_view(["GET"]) #Expose following function only on GET request
def get_cloth(request, id):

    try:

        #Get cloth from database
        cloth = ClothingModel.objects.get(pk = id)

        #Create a serializer for converting cloth into json:
        serializer = ClothingSerializer(cloth)

        #Response back the serializer json:
        return Response(serializer.data) #status code = 200 as default
    
    except ClothingModel.DoesNotExist:
        json = { "error": f"id {id} not found"}
        return Response(json, status = status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = {"error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


#Add new cloth
@api_view(["POST"]) #Expose following function only on POST request
def add_cloth(request):
    try:

        #Get given cloth for adding
        cloth = request.data

        #Create serializer for saving that cloth:
        serializer = ClothingSerializer(data = cloth) 

        #Validate
        if not serializer.is_valid():
            json = {"error": serializer.errors}
            return Response(json, status = status.HTTP_400_BAD_REQUEST) #Validation error

        #Save to database
        serializer.save()

        # Take the added cloth containing cloth id
        added_cloth = serializer.data

        #return the added cloth:
        return Response(added_cloth, status= status.HTTP_201_CREATED)
    
    except Exception as err:
        json = {"error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#Edit existing cloth
@api_view(["PUT"]) #Expose following function only on PUT request
def edit_cloth(request, id):
    try:

        #if cloth not found
        exist = ClothingModel.objects.filter(id = id).exists()
        if not exist:
            json = {"error": f"id {id} not found."}
            return Response(json, status=status.HTTP_404_NOT_FOUND)

        #Get given cloth for editing
        cloth = request.data

        #Create serializer for saving that cloth:
        serializer = ClothingSerializer(data = cloth, instance= ClothingModel(pk = id)) 

        #Validate
        if not serializer.is_valid():
            json = {"error": serializer.errors}
            return Response(json, status = status.HTTP_400_BAD_REQUEST) #Validation error

        #Save to database
        serializer.save()

        # Take the updated cloth containing cloth id
        update_cloth = serializer.data

        #return the added cloth:
        return Response(update_cloth)
    
    except Exception as err:
        json = {"error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

#Delete existing cloth
@api_view(["DELETE"]) #Expose following function only on DELETE request
def delete_cloth(request, id):
    try:

        #if cloth not found
        exist = ClothingModel.objects.filter(id = id).exists()
        if not exist:
            json = {"error": f"id {id} not found."}
            return Response(json, status=status.HTTP_404_NOT_FOUND)

        #Create dummy cloth for delete
        dummy_cloth = ClothingModel(pk = id)

        #Delete this cloth from database
        dummy_cloth.delete()

        #Response back nothing
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    except Exception as err:
        json = {"error": str(err) }
        return Response(json, status = status.HTTP_500_INTERNAL_SERVER_ERROR)