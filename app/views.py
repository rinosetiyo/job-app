from django.shortcuts import render
from .models import JobPost


# Create your views here.
def index(request):
    data = JobPost.objects.all()
    context = {
        "jobs": data,
    }
    return render(request, "app/index.html", context)


def detailView(request, id):
    data = JobPost.objects.get(id=id)
    context = {
        "jobs": data,
    }
    return render(request, "app/view-job.html", context)
