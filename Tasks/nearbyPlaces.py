import geocoder as geo
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_user_location():
    location = geo.ip('me')
    return location.latlng

def find_nearby_places(lat, lon, place_type, radius):
    geolocator = Nominatim(user_agent="nearby_search")
    location = geolocator.reverse((lat, lon))
    print(f"\nYour current location: {location}\n")
    
    query = f"{place_type} near {lat}, {lon}"
    try:
        places = geolocator.geocode(query, exactly_one=False, limit=None)
        if places:
            for place in places:
                place_coords = (place.latitude, place.longitude)
                place_distance = geodesic((lat, lon), place_coords).kilometers
                if place_distance <= radius:
                    print(f"{place.address} ({place_distance:.2f} km)")
        else:
            print("No nearby places found for the given type.")
    except:
        print("Error: Unable to fetch nearby places.")



if __name__ == '__main__':
    cor = get_user_location()
    lat, lon = cor[0], cor[1]

    place_type = input("What type of place are you looking for? (e.g., park, mall, ATM, hotel): ")
    search_radius = float(input("Enter the search radius (in kilometers): "))
    find_nearby_places(float(lat), float(lon), place_type, search_radius)
