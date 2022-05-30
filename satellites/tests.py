import pytest
import factory
from pytest_factoryboy import register
from factory.django import DjangoModelFactory

from satellites.distance import get_near_satellites


class SatelliteFactory(DjangoModelFactory):
    class Meta:
        model = 'satellites.Satellite'

    name = factory.Sequence(lambda n: "test-sat_{}".format(n))
    latitude = factory.Sequence(lambda n: "{}".format(n))
    longitude = factory.Sequence(lambda n: "U{}".format(n))


register(SatelliteFactory)


@pytest.mark.parametrize("point, distance, added", [
    ((11.161, 30.436), 1900, True),
    ((45.321, 30.581), 77, False),
    ((21.713, 23.426), 1680, True),
    ((10.823, 3.165), 1000, False),
    ((21.042, 4.429), 56, False),
    ((35.153, 40.052), 3990, True),
])
@pytest.mark.django_db
def test_get_near_satellites(point, distance, added, satellite_factory):
    satellite_factory(latitude=point[0], longitude=point[1])
    base_point = (10.1, 13.3)
    result = get_near_satellites(base_point[0], base_point[1], distance)
    assert len(result) == int(added)
