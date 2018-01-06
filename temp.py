def get_distance1(c_map_info, p_map_info):
    try:
        c_lon, c_lat = c_map_info.split(',')
        p_lon, p_lat = p_map_info.split(',')
        lat1, lon1, lat2, lon2 = float(c_lat), float(c_lon), float(p_lat), float(p_lon)
        R = 6371  # Earth radius in km
        d_lat = np.radians(lat2 - lat1)
        d_lon = np.radians(lon2 - lon1)
        r_lat1 = np.radians(lat1)
        r_lat2 = np.radians(lat2)
        a = np.sin(d_lat / 2.) ** 2 + np.cos(r_lat1) * np.cos(r_lat2) * np.sin(d_lon / 2.) ** 2
        haversine = 2 * R * np.arcsin(np.sqrt(a))
        return haversine  # return dist_from_coordinates(float(c_lat), float(c_lon), float(p_lat), float(p_lon))
    except:
        pass
    return -1

def dist_from_coordinates(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    # conversion to radians
    d_lat = np.radians(lat2 - lat1)
    d_lon = np.radians(lon2 - lon1)
    r_lat1 = np.radians(lat1)
    r_lat2 = np.radians(lat2)
    # haversine formula
    a = np.sin(d_lat / 2.) ** 2 + np.cos(r_lat1) * np.cos(r_lat2) * np.sin(d_lon / 2.) ** 2

    haversine = 2 * R * np.arcsin(np.sqrt(a))

    return haversine


def get_distance(c_map_info, p_map_info):
    try:
        c_lon, c_lat = c_map_info.split(',')
        p_lon, p_lat = p_map_info.split(',')
        return dist_from_coordinates(float(c_lat), float(c_lon), float(p_lat), float(p_lon))
    except:
        pass
    return -1

print get_distance('104.240685,23.369383','88.884317,29.263647')