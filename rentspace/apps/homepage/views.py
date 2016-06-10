from django.shortcuts import render

from users.models import User,Post,PostAttributes,Image
from users.serializers import UserSerializer,PostSerializer,PostAttributeSerializer,ImageSerializer,CommentSerializer

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser, FormParser

from rest_framework import permissions
from rest_framework.decorators import permission_classes

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse
from django.template import loader

from wsgiref.util import FileWrapper


import json
import os
import uuid


def index(request):
    template = loader.get_template('index.html')
    context ={}
    return HttpResponse(template.render(context, request))

    #return render_to_response('index.html', context_instance=RequestContext(request))
