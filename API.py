import urllib.parse
import json
import urllib.request

#Consumer Key		ZsamDKpuQn6SSr0BwKH4LkuTAKJfpCe2
#Consumer Secret	Tdqlc6zcha6shcW1



def build_map_quest_url(list_of_locations: list)-> str:
    '''this function takes in the locations inputed in lets_begin
       and returns a URL the can be used in the API'''
    DIRECTIONS_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route'
    API_KEY = 'ZsamDKpuQn6SSr0BwKH4LkuTAKJfpCe2'
    query_parameters = []
    query_parameters.append(('key', API_KEY))
    query_parameters.append(('from', list_of_locations[0]))       
    for location in list_of_locations[1:]:
        query_parameters.append(('to', location))
    #print(DIRECTIONS_MAPQUEST_URL + '?' + urllib.parse.urlencode(query_parameters))
    return DIRECTIONS_MAPQUEST_URL + '?' + urllib.parse.urlencode(query_parameters)
    
def read_url(url: str) ->dict:
    '''this function takes a url and returns a Python Dictionary representing the parsed Json response'''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


def build_elevation_url(route_info: dict)-> str:
    '''this function takes in LATLONG information from the mapquest api
        and builds elevation url'''
    ELEVATION_MAPQUEST_URL = 'http://open.mapquestapi.com/elevation/v1/profile'
    API_KEY = 'ZsamDKpuQn6SSr0BwKH4LkuTAKJfpCe2'
    query_parameters = []
    key_parameters = []
    key_parameters.append(('key', API_KEY))
    key_parameters.append(('shapeFormat', 'raw'))
    for point in route_info['route']['locations']:        
        latlng = (str(point['latLng']['lat']).split()) +(str(point['latLng']['lng']).split())
        query_parameters += latlng
    location_string = (','.join(query_parameters))
    key_parameters.append(('latLngCollection', location_string))
    return ELEVATION_MAPQUEST_URL + '?' + urllib.parse.urlencode(key_parameters) 

class NoExistingRouteError(Exception):
    pass

class MapQuestError(Exception):
    pass


def check_error_type(route_info: dict):
    '''Determines error type by seeing the what status code appears
        in the mapquest api'''
    statuscode = route_info['info']['statuscode']
    possible_errors = (601, 602, 604, 605, 606, 607, 608, 609, 610, 611, 612, 400, 401, 402, 403, 500)

    for codes in possible_errors:
        if codes == statuscode:
            raise NoExistingRouteError
    if statuscode != 0:
        raise MapQuestError



