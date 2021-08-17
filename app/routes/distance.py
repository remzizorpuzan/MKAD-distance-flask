from flask import Flask, render_template, request, Blueprint
from geopy.geocoders import Nominatim
from geopy import distance
import requests
import logging

distance_page = Blueprint('distance_page', __name__,
                          template_folder='templates')

# Instantiate of logging format
logging.basicConfig(filename='.log', level=logging.INFO,
                    format='%(message)s', filemode='w')

# API KEY
API_KEY = '1146f8f5-004d-4c97-b921-d6173b6feb2c'


@distance_page.route('/distance', methods=['POST'])
def find_distance():

    # -x,+x,-y,+y - Moscow Ring road border coordinates
    MKAD_border_coordinates = [37.329, 37.895, 55.503, 55.917]

    # Static MKAD coordinates.
    MKAD_coordinates = (55.690976835869535, 37.41301096956567)

    # By using API key and address destination, making API call and put response into json object.
    address_input = request.form['distance']
    response = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=' +
                            API_KEY+'&format=json&geocode='+address_input+'&results=1')
    json_object = response.json()

    # Checks API response status code and response is valid.
    if response.status_code == 200:

        # Create temp position that response filter for featureMember
        temp_position = json_object["response"]["GeoObjectCollection"]["featureMember"]

        # If feature member list in Null then the address input is invalid
        if len(temp_position) == 0:
            final_distance = "INVALID ADDRESS!"

        else:
            # FeatureMember list is not null then mean it has featureMember and includes position.
            position = json_object["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]

            # Response longitude and latitude comes with white space. Splits those two values.
            splitted_positions = position.split()

            # API response coordinates comes reverse because of this, second element setted as first position. Second element as first position.
            # For making calculation, values are converted to float.
            first_pos = float(splitted_positions[1])
            second_pos = float(splitted_positions[0])

            # Hold coordinates into one variable.
            aim_position = (first_pos, second_pos)

            # Checks input address already inside border coordinates of MKAD.
            if MKAD_border_coordinates[0] <= second_pos <= MKAD_border_coordinates[1] and MKAD_border_coordinates[2] <= first_pos <= MKAD_border_coordinates[3]:
                final_distance = "Already inside MKAD"
            else:
                # By using geopy, distance between two points calculated.
                distance_calc = distance.distance(
                    aim_position, MKAD_coordinates)
                final_distance = str(distance_calc)
                # Adds results to the .log file.
                logging.info("Distance between MKAD ->"+final_distance)
    # If status code different than 200, returns error message.
    else:
        final_distance = "INVALID ADDRESS"
    return render_template('distance.html', distance=final_distance)
