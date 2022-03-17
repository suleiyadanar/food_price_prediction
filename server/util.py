import json
import pickle
import sklearn
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_price_estimate(location, commodity, sales_catagory):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = commodity
    x[1] = sales_catagory
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def get_location():
    return __locations


def load_artifacts():
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", 'r')as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[257:]
    with open("./artifacts/food_price_model.pickle", 'rb')as f:
        __model = pickle.load(f)


if __name__ == "__main__":
    load_artifacts()
    print(get_location())
    print(get_price_estimate('Afghanistan', 1, 1))
    print(get_price_estimate('Zimbabwe', 0, 0))
