#!usr/bin/python3

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('path/to/credentials/json/file')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-db-name.firebaseio.com' 
})

# database document root 
ref = db.reference('test-iot')


def search_all():
    return ref.get()


def get_data_by_sensor_name(sensor):
    sensor_key = get_key_by_sensor_name(sensor)
    snapshot = search_all()
    for key, val in snapshot.items():
        if sensor_key == key:
            return val
    return 0


# Add new data
def add_new_data(sensor, humid, led, temp):
    ref.push({
            'name': sensor,
            'humid': humid,
            'led': led,
            'temp': temp
    })


def get_key_by_sensor_name(sensor):
    snapshot = search_all()
    for key, val in snapshot.items():
        if val['name'] == sensor:
            return key
    return 0


# update data
def update_data(sensor, humid, led, temp):
    update_ref = ref.child(get_key_by_sensor_name(sensor))
    update_ref.update({
            'humid': humid,
            'led': led,
            'temp': temp
    })


# check duplicates
def check_duplicate(sensor, humid, led, temp):
    data = get_data_by_sensor_name(sensor)
    if data != 0:
        update_data(sensor, humid, led, temp)


def insert_sensor():
    sensor_input = input("Enter sensor name : ")
    humid_input = input("Enter humidity : ")
    led_input = input("Enter led status : ")
    temp_input = input("Enter tempreture : ")
    add_new_data(sensor_input, humid_input, led_input, temp_input)


def update_sensor():
    sensor_input = input("Enter sensor name : ")
    humid_input = input("Enter humidity : ")
    led_input = input("Enter led status : ")
    temp_input = input("Enter tempreture : ")
    check_duplicate(sensor_input, humid_input, led_input, temp_input)


def main():
    choice = ''
    while choice != 'q':
        print('\nMenu\n')
        print('01. Add new sensor.')
        print('02. Update sensor values.')
        print('03. Get all sensor details.')
        print('04. Get a sensor detail.')
        print('Enter \'q\' to exit.\n')

        choice = input('Enter your choice : ')

        if(choice == '1'):
            insert_sensor()
        elif(choice == '2'):
            update_sensor()
        elif(choice == '3'):
            print(search_all())
            print('\n')
        elif(choice == '4'):
            sensor_name = input("Enter sensor name : ")
            print(get_data_by_sensor_name(sensor_name))
            print('\n')


if __name__ == '__main__':
    main()

