import sys
import ast
import pandas as pd
import pygeohash as gh



def parse_argv():
    argv = sys.argv[1:]
    ll_list = argv[0].split(' ')
    index = ll_list.index('longitude')
    lat = ll_list[1:index]
    lon = ll_list[index+1:]
    return lat, lon


if __name__ == '__main__':
    pass
    latitude, longitude = parse_argv()
    data = {'latitude': [float(i) for i in latitude], 'longitude': [float(i) for i in longitude]}
    df = pd.DataFrame(data)
    df['geohash'] = df.apply(lambda x: gh.encode(x.latitude, x.longitude, precision=5), axis=1)
    print(df)
