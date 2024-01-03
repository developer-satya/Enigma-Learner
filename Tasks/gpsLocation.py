import geocoder as geo

# Get location of my IP address
location = geo.ip('me')

# Print location
print(location.latlng)