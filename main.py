import API
import outputs
import urllib.error
import socket


def lets_begin()->list:
    '''This function asks the user to input the amount of
    addresses there are and then to type out each address'''
    list_of_locations = []
    location_number = int(input("Enter the number of addresses you are mapping: "))
    if location_number >= 2:
        for i in range(location_number):
            address = input("Enter the address: ")
            list_of_locations.append(address)
        return list_of_locations
    else:
        print('error')    



'''
def display_outputs(route_info:dict, elevation_info:dict)->None:
    ''asks for the amount of outputs and then asks user to specify
        which outputs they want to return''
    output_list = []
    output_number = int(input())
    if output_number >= 1:
        for i in range(output_number):
            which_output = input('')
            output_list.append(which_output)
    else:
        print('error')

    for item in output_list:
        get_object = outputs.specify_output(item, elevation_info, route_info)
        get_object.output()
'''

def display_outputs(route_info:dict)->None:
    '''asks for the amount of outputs and then asks user to specify
        which outputs they want to return'''
    #print(route_info)
    output_list = []
    output_number = int(input("Enter the amount of outputs you want to display: "))
    if output_number >= 1:
        for i in range(output_number):
            which_output = input('Enter the type of output (STEPS, TOTALDISTANCE, TOTALTIME, LATLONG: ')
            output_list.append(which_output.upper())
    else:
        print('error')

    for item in output_list:
        get_object = outputs.specify_output(item, route_info)
        get_object.output()

if __name__ == '__main__':
    route_info = API.read_url(API.build_map_quest_url(lets_begin()))
    try:
        API.check_error_type(route_info)
        display_outputs(route_info)
    except API.NoExistingRouteError:
        print()
        print('NO ROUTE FOUND')
    except API.MapQuestError or urllib.error.HTTPError or urllib.error.URLError or socket.error or OS.error: 
        print()
        print('MAPQUEST ERROR')
    finally:
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')

