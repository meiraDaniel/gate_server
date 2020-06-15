from flask import Flask, request, jsonify
from flaskapi import app, db

from flaskapi.models import Tour, Client

methods = ['GET', 'POST']


@app.route('/places', methods=['GET'])
def get_places():

    list_tours = []

    isSummer = request.args.get('isSummer')

    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')

    if isSummer=='true':
        query_tours = Tour.query.filter_by(isSummer=True)
    elif isSummer=='false':
        query_tours = Tour.query.filter_by(isSummer=False)
    else:
        response = jsonify({'error': 'Deu BO!!'})
        return response

    
    for tour in query_tours:
        list_tours.append(tour.as_dict())
    
    response = jsonify({'tours': list_tours})
    return response

@app.route('/clients', methods=['GET'])
def get_clients():

    list_clients = []

    isSummer = request.args.get('isSummer')

    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')

    if isSummer=='true':
        query_clients = Client.query.join(Client.tour, aliased=True).filter_by(isSummer=True)
    elif isSummer=='false':
        query_clients = Client.query.join(Client.tour, aliased=True).filter_by(isSummer=False)
    else:
        response = jsonify({'error': 'Deu BO!!'})
        return response

    
    for client in query_clients:

        tour_name = client.tour.tour_name
        tour_place = client.tour.place

        client = client.as_dict()
        
        client['tour_name'] = tour_name
        client['tour_place'] = tour_place

        del client['tour_id']

        list_clients.append(client)
    
    response = jsonify({'clients': list_clients})
    return response



# tour_1 = Tour(tour_name='Aventure Winter', place='Christchurch, New Zealand', activities='Hiking,Skiing,Snowboarding,Mountains,Climbing,Camping,Food Tasting', price=1280, number_days=6, number_people=1, isSummer=False, sale=True)
# tour_2 = Tour(tour_name='Wild Winter', place='Queenstown, New Zealand', activities='Rainforests,Hiking,Boat Ride,Glaciers,Skiing', price=789, number_days=4, isSummer=False)
# tour_3 = Tour(tour_name='Alpine Explorer', place='Christchurch, New Zealand', activities='Hiking,Skiing,Snowboarding,Mountains,Climbing,Camping,Glaciers,Hot Pools,Bike Rides,Food Tasting', price=2320, number_days=9, number_people=2, isSummer=False)
# tour_4 = Tour(tour_name='LOTR Winter', place='Rotorua, New Zealand', activities='City Tour,Hiking,Boat Rides,Trails,Food Tasting,Maori Culture,Skiing,Mountains', price=3568, number_days=6, number_people=4, isSummer=False, sale=True)


# tour_1 = Tour(tour_name='Auckland Adventure', place='Auckland, New Zealand', activities='Skydive,Bungee Jump', price=580.99, number_days=2, number_people=1, sale=True)
# tour_2 = Tour(tour_name='Auckland Vintage', place='Auckland, New Zealand', activities='City Tours,Wine Tasting,Food Tasting,Museums,Sailing', price=1450, number_days=4)
# tour_3 = Tour(tour_name='Wild Auckland', place='Auckland, New Zealand', activities='Surf,Hiking,Trails,Sailing,Camping,Ka', price=2320, number_days=5, number_people=4, sale=True)
# tour_4 = Tour(tour_name='LOTR Basic', place='Rotorua, New Zealand', activities='City Tour,Hiking,Boat Rides,Trails,Food Tasting,Maori Culture', price=3135, number_days=6, number_people=4, sale=True)
# tour_5 = Tour(tour_name='LOTR Premium', place='Rotorua, New Zealand', activities='City Tour,Trails,Climbing,Sailing,Maori Culture,Kayak,Camping,Wine Tasting,Food Tasting', price=4850, number_days=12, number_people=4)



























































    #
