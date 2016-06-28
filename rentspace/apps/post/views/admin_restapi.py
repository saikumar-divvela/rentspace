
@permission_classes((permissions.AllowAny,))
class XPostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, user_pk, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request,user_pk, pk, format=None):
         post = self.get_object(pk)
         print (post)
         request.data["user"]=user_pk   
         serializer = PostSerializer(post,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            update_post_attributes(request.data["attributes"],serializer.data["id"])
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_pk,pk,format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def add_post_attributes(attributelist,post_id):
    for attribute in attributelist:
        attr_data = {}
        attr_data["post"]=post_id
        for name,value in attribute.items():    
            attr_data["name"]=name
            attr_data["value"]=value
            attr_serializer = PostAttributeSerializer(data=attr_data)
            if attr_serializer.is_valid():
                attr_serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_post_attributes(attributelist,post_id):
    postattributes = PostAttributes.objects.filter(post__id=post_id);
    for attribute in postattributes:
        attribute.delete()
    add_post_attributes(attributelist,post_id)

@csrf_exempt
def post_status(request,user_pk,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    
    if request.method == "GET":
        output = {}
        output["status"] = post.status
        output["is_verified"] = post.is_verified
        output["is_active"] = post.is_active
                
        serializer = PostSerializer(post)
        return JSONResponse(output)


    elif request.method == "PUT":
         data = JSONParser().parse(request)
         for key,value in data.items():
            post[key]=value    
         post.save()

         serializer = PostSerializer(post)
         return JSONResponse(serializer.data)  
         #return Response(serializer.data) 



@permission_classes((permissions.AllowAny,))
class XPostAttributeList(APIView):
    def get(self,request,user_pk,post_pk,format=None):
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,post_pk,format=None):    
        print (request.data)
        update_post_attributes(request.data["attributes"],post_pk)
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)

    def put(self,request,user_pk,post_pk,format=None):    
        print (request.data)
        update_post_attributes(request.data["attributes"],post_pk)
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)



@permission_classes((permissions.AllowAny,))
class PostList(APIView):
    def get(self,request,user_pk,format=None):
        user = UserDetailUserDetail().get_object(user_pk)
        posts = Post.objects.filter(user__id=user_pk);
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,format=None):    
        user =UserDetail().get_object(user_pk)
        request.data["user"]= user_pk
        serializer = PostSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            #add_post_attributes(request.data["attributes"],serializer.data["id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        print ("************************************************************")
        serializer.save(user=self.request.user)