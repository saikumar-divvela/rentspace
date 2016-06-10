from django.shortcuts import render

'''

# Get -> returns all photos of given post
# Post -> Adds one photo to post    
# example curl -X POST -H "Content-Type: application/json"  -d '{"title": "test pic12","description": "this is a test pic12", "filetype": "test type"}' -F "filedata=@a.txt" http://localhost:8000/users/1/posts/2/images/
# Delete -> Delete all photos of the post
@permission_classes((permissions.AllowAny,))
class ImageList(APIView):
    #parser_classes = (FileUploadParser, )    
    parser_classes = (MultiPartParser, FormParser,)

    def get(self,request,user_pk,post_pk,format=None):
        print ("Get request for all images")
        post =PostDetail().get_object(post_pk)
        images = Image.objects.filter(post__id=post_pk) 
        serializer = ImageSerializer(images,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,post_pk,format=None):    
        print ("Post request for all images")
        print (request.data)
        tmpdir = "/tmp/media"
        uploaded_file = request.FILES['filedata']
        filename =   str(uploaded_file)      
    
        if not os.path.exists(os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk)):
            os.makedirs(os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk))

        destfile = os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk,filename)

        with open(destfile, 'wb+') as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)

        request.data["filename"] =  filename
        request.data["filepath"] =  destfile
        request.data["url"] = uuid.uuid4()
        request.data["post"]= post_pk
        request.data["size"] = os.path.getsize (destfile)

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,user_pk,post_pk,format=None):    
        post =PostDetail().get_object(post_pk)
        images = Image.objects.filter(post__id=post_pk) 
        for image in images:
            image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

# Get -> returns details of one image
# Delete -> Delete the selected image
@permission_classes((permissions.AllowAny,))
class ImageDetail(APIView):
    def get_object(self,pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, user_pk,post_pk,pk, format=None):
        print ("Get request for one images")
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    
    def delete(self,request,user_pk,post_pk,pk,format=None):
        print ("Deleting selected images")
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class ImageDownload(APIView):
    def get(self,request,pk,format=None):
        print (pk)
        image =  Image.objects.filter(url=pk)[0]
        fileformat='raw'
        if fileformat == 'raw':
            out_file = open(image.filepath, 'rb')
            response = HttpResponse(FileWrapper(out_file), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="%s"' % image.filename
            return response

'''
