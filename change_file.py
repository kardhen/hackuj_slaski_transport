#!/usr/bin/env python2
import json
import Geohash

def change_corr(cor, precision=5):
    x, y = cor
    geohash = Geohash.encode(x, y, precision=precision)
    x, y = Geohash.decode(geohash)
    return [float(x), float(y)]


def change_precision(filename, precision):
    with open('trips.geojson') as f:
        data = json.load(f)

    features = data['features']
    only_lines = filter(lambda geo: geo['geometry']['type'] == u'LineString',  features)

    for x in only_lines:
        geo = x['geometry']
        geo['coordinates'] = [change_corr(x, precision) for x in geo['coordinates']]

    with open(filename, 'w') as f:
        json.dump(data, f)
        

if __name__ == "__main__":
    from sys import argv
    filename = argv[1]
    precision = int(argv[2])
    change_precision(filename, precision)

