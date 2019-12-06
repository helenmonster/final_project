from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sighting
from django.shortcuts import redirect, get_object_or_404
from .forms import SightingForm

def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'sightings/map.html',context)

def sightings(request):
    squirrels = Sighting.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/sightings.html',context)

def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            new_sighting = form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = SightingForm()
    return render(request, 'sightings/add.html', {'form': form})

def id(request,squirrel_id):
    try:
        squirrel = Sighting.objects.get(unique_squirrel_id = squirrel_id)
    except Sighting.DoesNotExist:
        squirrel = None

    form = SightingForm(request.POST or None, instance=squirrel)
    context = {
            'squirrel':squirrel,
            'form':form,
            }
    if form.is_valid():
        squirrel = form.save()
        squirrel.save()
        context = {
                'squirrel':squirrel,
                'form':form,
                }
    return render(request,'sightings/squirrel_id.html',context)

