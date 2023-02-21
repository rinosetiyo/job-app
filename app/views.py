from django.shortcuts import render
from .models import Job


# Create your views here.
def index(request):
    data = Job.objects.all()
    context = {
        "jobs": data,
    }
    return render(request, "app/index.html", context)


def detailView(request, id):
    data = Job.objects.get(id=id)
    context = {
        "jobs": data,
    }
    return render(request, "app/view-job.html", context)
