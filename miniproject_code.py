H_dist = {}
def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes m
    # ditance of starting node from itself is zero
    g[start_node] = 0  # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None  # node with Lowest f( ) is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            break
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # remove n from the open_set and add it to closed_set
        # because all of its neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    if n == None:
        print('Path does not exist!')
        return None

    # reconstruct the path from the start_node to n
    path = []
    while parents[n] != n:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    path.reverse()
    print(f'Path found: {path}')
    return path


# define function to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# for simplicity we'll consider heuristic distances given
# and this function returns heuristic distance for all nodes


import math

EARTH_RADIUS = 6371  # Earth's radius in kilometers
APPROXIMATION_FACTOR = 0.5  # Heuristic approximation factor


def calculate_heuristic(start, goal):
    """
    Calculate the heuristic value (straight-line distance) between two coordinates.
    The coordinates should be in (latitude, longitude) format.
    """
    lat1, lon1 = start
    lat2, lon2 = goal

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Constants for Vincenty's formulae
    a = 6378.137  # Equatorial radius of the Earth in meters
    f = 1 / 298.257223563  # Earth's flattening

    # Calculating differences
    delta_lon = lon2_rad - lon1_rad

    # Vincenty's formulae
    numerator = math.sqrt(math.pow(math.cos(lat2_rad) * math.sin(delta_lon), 2) +
                          math.pow(math.cos(lat1_rad) * math.sin(lat2_rad) -
                                   math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(delta_lon), 2))
    denominator = math.sin(lat1_rad) * math.sin(lat2_rad) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.cos(
        delta_lon)
    delta_sigma = math.atan2(numerator, denominator)

    # Distance calculation
    distance = a * delta_sigma
    return distance


def calculate_heuristics(cities, goal):
    """
    Calculate heuristic values for multiple cities based on the goal city.
    Returns a dictionary with city names as keys and heuristic values as values.
    """
    heuristics = {}
    goal_city = None
    for city in cities:
        if city['city'] == goal:
            goal_city = city
            break

    if goal_city is None:
        return heuristics  # Return empty dictionary if the goal city is not found

    end = (goal_city['latitude'], goal_city['longitude'])
    for city in cities:
        start = (city['latitude'], city['longitude'])
        heuristic_value = calculate_heuristic(start, end)
        heuristics[city['city']] = heuristic_value

    return heuristics

def heuristic(n):
    H_dist = heuristics
    return H_dist[n]


# Example usage
cities = [
    {
        "city": "Ahmednagar",
        "latitude": 19.162772500000003,
        "longitude": 74.85802430085195
    },
    {
        "city": "Akola",
        "latitude": 20.76181225,
        "longitude": 77.1921156663574
    },
    {
        "city": "Amravati",
        "latitude": 21.15454115,
        "longitude": 77.64429617998744
    },
    {
        "city": "Aurangabad",
        "latitude": 24.786306,
        "longitude": 84.41448983395554
    },
    {
        "city": "Bhandara",
        "latitude": 21.12304765,
        "longitude": 79.79390882119336
    },
    {
        "city": "Beed",
        "latitude": 18.9918442,
        "longitude": 75.90978399809711
    },
    {
        "city": "Buldhana",
        "latitude": 20.53208,
        "longitude": 76.179911
    },
    {
        "city": "Chandrapur",
        "latitude": 20.0967555,
        "longitude": 79.50454752230621
    },
    {
        "city": "Dhule",
        "latitude": 21.13170235,
        "longitude": 74.48990147066098
    },
    {
        "city": "Gadchiroli",
        "latitude": 19.759070350000002,
        "longitude": 80.16228072580182
    },
    {
        "city": "Gondia",
        "latitude": 21.455228,
        "longitude": 80.1962729
    },
    {
        "city": "Hingoli",
        "latitude": 19.54140965,
        "longitude": 77.17376601317515
    },
    {
        "city": "Jalgaon",
        "latitude": 20.84288265,
        "longitude": 75.52612463784979
    },
    {
        "city": "Jalna",
        "latitude": 19.918832950000002,
        "longitude": 75.87085986165867
    },
    {
        "city": "Kolhapur",
        "latitude": 16.7028412,
        "longitude": 74.2405329
    },
    {
        "city": "Latur",
        "latitude": 18.35159075,
        "longitude": 76.75542361334745
    },
    {
        "city": "Mumbai City",
        "latitude": 18.9733536,
        "longitude": 72.82810491917377
    },
    {
        "city": "Mumbai suburban",
        "latitude": 19.1306115,
        "longitude": 72.88619365454353
    },
    {
        "city": "Nandurbar",
        "latitude": 21.51450155,
        "longitude": 74.54070114836503
    },
    {
        "city": "Nanded",
        "latitude": 19.09400875,
        "longitude": 77.48319215130235
    },
    {
        "city": "Nagpur",
        "latitude": 21.1498134,
        "longitude": 79.0820556
    },
    {
        "city": "Nashik",
        "latitude": 20.0112475,
        "longitude": 73.7902364
    },
    {
        "city": "Osmanabad",
        "latitude": 18.28224535,
        "longitude": 76.05881660170444
    },
    {
        "city": "Parbhani",
        "latitude": 19.29031365,
        "longitude": 76.60290343431203
    },
    {
        "city": "Pune",
        "latitude": 18.521428,
        "longitude": 73.8544541
    },
    {
        "city": "Raigad",
        "latitude": 18.4928092,
        "longitude": 73.13807095426539
    },
    {
        "city": "Ratnagiri",
        "latitude": 17.282607900000002,
        "longitude": 73.4569787039826
    },
    {
        "city": "Sindhudurg",
        "latitude": 16.135719299999998,
        "longitude": 73.65220860183584
    },
    {
        "city": "Sangli",
        "latitude": 17.1726928,
        "longitude": 74.58676543279755
    },
    {
        "city": "Solapur",
        "latitude": 17.84990665,
        "longitude": 75.27632027348457
    },
    {
        "city": "Satara",
        "latitude": 17.63612885,
        "longitude": 74.29827807601782
    },
    {
        "city": "Thane",
        "latitude": 19.1943294,
        "longitude": 72.9701779
    },
    {
        "city": "Wardha",
        "latitude": 20.82562315,
        "longitude": 78.61314549522919
    },
    {
        "city": "Washim",
        "latitude": 20.287417750000003,
        "longitude": 77.23696550258964
    },
    {
        "city": "Yavatmal",
        "latitude": 20.325703750000002,
        "longitude": 78.11691396684715
    }
    # Add more cities here
]

# Describe your graph here
Graph_nodes = {
    'Ahmednagar': [('Pune', 127.57673900018662), ('Aurangabad', 114.3327755250468),('Nashik', 157.3327755250468),('Solapur', 264.3327755250468),('Thane', 259.3327755250468),('Beed', 264.3327755250468)],
    'Akola': [('Bhandara', 335.023684089565), ('Buldhana', 99.0806926621851), ('Amravati', 98.6784341817348),
              ('Washim', 80.9084460295408), ('Yavatmal', 165.4640718878952)],
    'Amravati': [('Akola', 97.6784341817348), ('Buldhana', 196.0806926621851), ('Yavatmal', 92.4640718878952)],
    'Aurangabad': [('Ahmednagar', 116.57673900018662), ('Pune', 237.57673900018662), ('Jalna', 59.90542956009256)],
    'Bhandara': [('Nagpur', 62.6186211977658), ('Gondia', 79.3436034585726), ('Chandrapur', 209.897895376471),
                 ('Akola', 334.023684089565)],
    'Beed': [('Ahmednagar', 126.57673900018662), ('Latur', 136.9391389412124), ('Osmanabad', 115.35654232386239)],
    'Buldhana': [('Akola', 100.0806926621851), ('Amravati', 197.0806926621851), ('Yavatmal', 266.2083091003581)],
    'Chandrapur': [('Bhandara', 212.897895376471), ('Gondia', 239.897895376471)],
    'Dhule': [('Nandurbar', 156.82871611731406), ('Nashik', 157.9831763027634), ('Jalgaon', 99.9831763027634)],
    'Gadchiroli': [('Chandrapur', 81.897895376471), ('Gondia', 158.4699641867342)],
    'Gondia': [('Bhandara', 105.3436034585726), ('Chandrapur', 239.897895376471), ('Gadchiroli', 157.4699641867342)],
    'Hingoli': [('Nanded', 505.64806040845434), ('Parbhani', 301.8345287123086)],
    'Jalgaon': [('Nashik', 254.2139893421987), ('Dhule', 158.9831763027634)],
    'Jalna': [('Aurangabad', 60.90542956009256), ('Beed', 101.88449344129455)],
    'Kolhapur': [('Sangli', 47.0064751216056), ('Ratnagiri', 132.18889264568892), ('Sindhudurg', 129.4439288746589)],
    'Latur': [('Beed', 136.9391389412124), ('Osmanabad', 74.35654232386239), ('Nanded', 143.64806040845434)],
    'Mumbai City': [('Mumbai suburban', 10.2166), ('Thane', 23.2181)],
    'Mumbai suburban': [('Mumbai City', 10.2166), ('Thane', 23.801)],
    'Nandurbar': [('Dhule', 93.82871611731406)],
    'Nanded': [('Hingoli', 89.64806040845434), ('Parbhani', 68.8345287123086), ('Latur', 143.64806040845434),('Yavatmal',194.12345678)],
    'Nagpur': [('Bhandara', 62.6186211977658), ('Chandrapur', 153.897895376471), ('Wardha', 77.8426071489758), ('Amravati', 157.8426071489758)],
    'Nashik': [('Dhule', 158.09495634352123), ('Jalgaon', 256.2139893421987),(' Aurangabad', 187.112334567),(' Ahmednagar',157.2198456), ('Thane',146.12456783)],
    'Osmanabad': [('Beed', 112), ('Latur', 70),('Ahemadnagar', 217),('Solapur',66)],
    'Parbhani': [('Hingoli', 75), ('Nanded', 67),('Jalna',161),('Beed',147),('Latur',128),('Buldhana',198)],
    'Pune': [('Ahmednagar', 121),('Satara',110),('Solapur',253),('Thane',155),('Raigad',113)],
    'Raigad': [('Thane', 175), ('Pune', 125),('Satara',219),('Ratnagiri',258)],
    'Ratnagiri': [('Kolhapur', 313),('Ratnagiri',258), ('Sindhudurg', 266),('Satara',191),('Sangli',173)],
    'Sindhudurg': [('Kolhapur', 127), ('Ratnagiri',131)],
    'Sangli': [('Kolhapur', 169.0064751216056), ('Satara', 109.17032500231562),('Solapur',190)],
    'Solapur': [('Osmanabad', 66.28676534044484),('Sangli',190),('Satara',241),('Pune',253),('Ahmednagar',264)],
    'Satara': [('Sangli', 122.0064751216056),('Ratnagiri',194),('Pune',110),('Solapur',241),('Raigad',142)],
    'Thane': [('Mumbai suburban', 28.801),('Nashik',148),('Raigad',177),('Pune',155),('Ahmednagar',235)],
    'Wardha': [('Nagpur', 76.8426071489758),('Amravati',122),('Yavatmal',69),('Chandrapur',130)],
    'Washim': [('Akola', 84.9084460295408),('Hingoli',244),('Buldhana',147),('Yavatmal' ,134),('Amravati',133)],
    'Yavatmal': [('Chandrapur', 156), ('Amravati', 93.2083091003581), ('Wardha',69),('Washim',160),('Hingoli',176),('Nanded',190)]}
heuristics = calculate_heuristics(cities, "Chandrapur")
print(heuristics)
aStarAlgo("Amravati","Chandrapur")
