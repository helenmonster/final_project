from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sighting
from django.shortcuts import redirect, get_object_or_404
from .forms import SightingForm
from django.db.models import Count,Sum
from django.contrib import messages 
from collections import Counter, OrderedDict
from django.db.models import Avg

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

#def add(request):
    #if request.method == 'POST':
        #form = SightingForm(request.POST)
        #if form.is_valid():
            #new_sighting = form.save()
            #return HttpResponseRedirect('/sightings/')
    #else:
        #form = SightingForm()
    #return render(request, 'sightings/add.html', {'form': form})

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

def stats(request):
    #stats_for_longitude = Sighting.objects.values('longitude').aggregate(Avg('longitude'))
    stats_for_running = Sighting.objects.values('running').annotate(count_for_this_category = Count('running')).order_by('-count_for_this_category')
    stats_for_climbing = Sighting.objects.values('climbing').annotate(count_for_this_category = Count('climbing')).order_by('-count_for_this_category')
    stats_for_shift = Sighting.objects.values('shift').annotate(Count('shift'))
    #stats_for_shift = Sighitng.objects.values('shift').annotate(count_for_this_category = Count('shift')).order_by('-count_for_this_category')
    #stats_for_latitude = Sighting.objects.values('latitude').aggregate(Avg('latitude'))
    #stats_for_age = Sighting.objects.values('age').aggregate(Avg('age'))
    stats_for_primary_fur_color = Sighting.objects.values('primary_fur_color').annotate(count_for_this_color = Count('primary_fur_color')).order_by('-count_for_this_color')
    #stats_for_primary_fur_color = Sighting.objects.values('primary_fur_color').annotate(number_of_fur_colors = Count('primary_fur_color')).order_by('number_of_fur_colors')
    stats_for_tail_twitches = Sighting.objects.values('tail_twitches').annotate(count_for_this_category = Count('tail_twitches')).order_by('-count_for_this_category')
    #stats_for_longitude  = Sighting.objects.values('longitude').order_by('longitude').annotate(stats_for_longitude = Counter('longitude'))
    #stats_for_latitude = Sighting.objects.values('latitude').order_by('latitude').annotate(stats_for_latitude = Count('latitude'))
    #stats_for_age = Sighting.objects.values('age').order_by('age').annotate(stats_for_age = Count('age'))
    #stats_for_primary_fur_color = Sighting.objects.values('primary_fur_color').order_by('primary_fur_color').annotate(Count('primary_fur_color'))
    #stats_for_tail_twitches = Sighting.objects.values('tail_twitches').order_by('tail_twitches').annotate(Count('tail_twitches'))
    context= {
           'stats_for_climbing':stats_for_climbing,
           'stats_for_shift':stats_for_shift,
           'stats_for_running':stats_for_running,
           'stats_for_primary_fur_color':stats_for_primary_fur_color,
           'stats_for_tail_twitches':stats_for_tail_twitches,
            }
    return render(request, 'sightings/stats.html', context)
