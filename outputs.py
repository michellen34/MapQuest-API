class STEPS:
    def __init__(self, route):
        self.route_info = route
    def output(self):
        print()
        print('DIRECTIONS')
        for directions in self.route_info['route']['legs']:
            for x in directions['maneuvers']:
                print(x['narrative'])

class TOTALDISTANCE:
    def __init__(self, route):
        self.route_info = route
    def output(self):
        print()
        print('TOTAL DISTANCE: ' + str(int(round(self.route_info['route']['distance']))) + ' miles')
    
class TOTALTIME:
    def __init__(self, route):
        self.route_info = route
    def output(self):
        print()
        print('TOTAL TIME: ' + str(round(int(self.route_info['route']['time'])/60)) + ' minutes')

        
class LATLONG:
    def __init__(self, route):
        self.route_info = route
    def output(self):
        print()
        print('LATLONGS')
        for point in self.route_info['route']['locations']:
            if point['latLng']['lng'] < 0:
                x = str(("%.2f" % point['latLng']['lng'])) +' S'
            elif point['latLng']['lng'] > 0:
                x = str(("%.2f" % point['latLng']['lng'])) +' N'
            if point['latLng']['lat'] < 0:
                y = str(("%.2f" %point['latLng']['lat'])) + ' W'
            else:
                y = str(("%.2f" %point['latLng']['lat'])) + ' E'
            print(x + ' ' + y)




def specify_output(which_output: str, route: dict):
    if which_output == 'STEPS':
        return STEPS(route)
    elif which_output == 'TOTALDISTANCE':
        return TOTALDISTANCE(route)
    elif which_output == 'TOTALTIME':
        return TOTALTIME(route)
    elif which_output == 'LATLONG':
        return LATLONG(route)
    else:
        print('error')    

