from geopy.distance import distance as points_distance
from satellites.models import Satellite


def get_near_satellites(latitude, longitude, distance):
    # NOTE: distance is in KM.
    # point coordinates: (latitude, longitude)
    base_point = (latitude, longitude)
    satellites = list(Satellite.objects.all())
    result = []
    for sate in satellites:
        sate_point = (sate.latitude, sate.longitude)
        pdistance = points_distance(base_point, sate_point)
        if pdistance < distance:
            result.append(sate)
    return [sate.to_json() for sate in result]
