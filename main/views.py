from django.shortcuts import render

# Create your views here.
from main.models import State


def index(request):
    return render(request, "index.html")


def maps(request):
    states = State.objects.all()
    geodata = {}
    result = []
    listState = State.objects.values_list('PSTATABB', flat=True)

    for state in states:
        geometry = {}

        statedata = {
            "id": state.id,
            "properties": {"generation": state.STNGENAN, "percentage": state.calculate_percentage,
                           "name": state.PSTATABB},
            "type": "Feature",
            "geometry": state.geometry,
        }
        result.append(statedata)
    geodata["features"] = result
    return render(request, "maps.html", {"geodata": geodata, "states": listState})
