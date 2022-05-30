from ninja import NinjaAPI
from django.http import HttpResponse

from satellites.models import Satellite
from satellites.distance import get_near_satellites
from satellites.serializers import SatellitesCoordinatesSerializer


satellites_api = NinjaAPI(title="Satellites API", docs_url="/")


@satellites_api.post("create")
def create(request, name: str, latitude: float, longitude: float):
    """Create a new satellite.

    ### Restrictions:
        - latitude in [-90, 90]
        - longitude in [-180, 180]
    """
    data = {"latitude": latitude, "longitude": longitude}
    serializer = SatellitesCoordinatesSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponse(status=400)
    serializer.validated_data.update({"name": name})
    satellite = Satellite(**serializer.validated_data)
    satellite.save()
    return satellite.to_json()


@satellites_api.get("list")
def list_satellites(request):
    """Get all avilable satellites."""
    queryset = Satellite.objects.all()
    satellites = [sate.to_json() for sate in queryset]
    return satellites


def get_by_name_or_404(name, to_delete=False):
    try:
        satellite = Satellite.objects.get(pk=name)
    except Satellite.DoesNotExist:
        response = HttpResponse(status=404)
        return response
    else:
        return_sate = satellite.to_json()
        if to_delete:
            satellite.delete()
        return return_sate


@satellites_api.delete("delete")
def delete(request, name):
    "Delete satellite by name."
    return get_by_name_or_404(name, to_delete=True)


@satellites_api.get("get-by-name")
def get_by_name(request, name: str):
    """Get satellite by name."""
    return get_by_name_or_404(name)


@satellites_api.get("get-by-position")
def get_by_position(request, latitude: float, longitude: float, distance: float):
    """Get satellites located less than distance from (latitude, longitude).

    ### Restrictions:
        - latitude in [-90, 90]
        - longitude in [-180, 180]
    """
    data = {"latitude": latitude, "longitude": longitude}
    serializer = SatellitesCoordinatesSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponse(status=400)
    near_satellites = get_near_satellites(latitude, longitude, distance)
    return near_satellites
