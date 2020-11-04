
trip = {
    "driver": {
        "first_name": "Danny",
        "last_name": "Dreyfus",
        "avg_rating": 3.6,
        "total_rides": 950
    },
    "vehicle": {
        "make": "Tesla",
        "model": "Cybertruck",
        "year": 2021,
        "color": "silver"
    },
    "rideshare": True,
    "pickup_location": "Union Station",
    "stops": [
        {"sequence": 1, "passenger": "Vishal", "destination": "Logan Circle", "fare": 3.99},
        {"sequence": 2, "passenger": "Clara", "destination": "Dupont Circle", "fare": 5.99},
        {"sequence": 3, "passenger": "Lee", "destination": "Georgetown University", "fare": 7.99}
    ]
}


if __name__ == "__main__":

    print("------------------")
    print("PROCESSING RIDESHARE DATA...")
    print("------------------")
    print(trip)
    # breakpoint()

    #
    # QUESTION A
    #
    # "Print" a human-friendly message to denote the driver’s first name (i.e. "Your driver is Danny):


    #
    # QUESTION B
    #
    # "Print" the number of stops this trip makes (i.e. 3):


    #
    # QUESTION C
    #
    # Assuming the stops will always be listed in ascending order of their stop sequence,
    # ... "print" the destination of the second stop (i.e. "Dupont Circle"):



    #
    # QUESTION D
    #
    # Loop through each of the trip’s stops and "print" that stop’s passenger name,
    # ... one at a time (i.e. "Vishal", then "Clara", then "Lee", each on a separate line):



    #
    # QUESTION E
    #
    # "Print" the total fare for this trip.
    # ... The total fare is equal to the sum of all individual stop fares (i.e. $17.98).
    # ... Don’t worry about rounding or adjusting the decimal places (i.e. format function not necessary),
    # ... but do include a dollar sign.
