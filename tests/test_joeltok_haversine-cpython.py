from cProfile import Profile
import math
import random
import sys


# List Optimised Haversine function
def haversine(lat1, lon1, lat2, lon2):
    miles_constant = 3959
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    mi = miles_constant * c
    return mi


def data_gen_mult(length):
    print(f"data_gen, length: {length}")
    array = [{'latitude': 0.0, 'longitude': 0.0}] * length
    for i in range(length):
        array[i]['longitude'] = random.random() * 360.0 - 180.0
        array[i]['latitude'] = random.random() * 180.0 - 90.0
    return array


def data_gen_append(length):
    print(f"data_gen, length: {length}")
    array = []
    for i in range(length):
        array.append({
            'longitude': random.random() * 360.0 - 180.0,
            'latitude': random.random() * 180.0 - 90.0
        })
    return array


def test_mult():
    data = data_gen_mult(int(sys.argv[1]))
    for o in data:
        o['distance'] = haversine(40.671, -73.985, o['latitude'], o['longitude'])


def test_append():
    data = data_gen_append(int(sys.argv[1]))
    for o in data:
        o['distance'] = haversine(40.671, -73.985, o['latitude'], o['longitude'])


if __name__ == "__main__":
    p = Profile()
    res = p.run("test_mult()")
    res.print_stats(sort=True)
