from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context ={}
    return render(request, 'index.html', context)

@login_required
def test_admin(request):
	context = {}
	return render(request, 'test.html', context)