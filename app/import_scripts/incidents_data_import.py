import pandas as pd
import numpy as np

from app.db.db_connection import get_db


def import_abandoned_vehicles(input_file: str) -> None:
    """ Import the requests for abandoned vehicles to the database.

    :param input_file: The file from which to load the requests for abandoned vehicles.
    """
    print("Getting requests for abandoned vehicles")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})
    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'license_plate', 'vehicle_make_model', 'vehicle_color',
                        'current_activity', 'most_recent_action', 'days_of_report_as_parked', 'street_address',
                        'zip_code', 'x_coordinate', 'y_coordinate', 'ward', 'police_district', 'community_area',
                        'ssa', 'latitude', 'longitude', 'geo_location', 'historical_wards_03_15', 'zip_codes',
                        'community_areas', 'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_garbage_carts(input_file: str) -> None:
    """ Import the requests for garbage carts to the database.

    :param input_file: The file from which to load the requests for garbage carts.
    """
    print("Getting requests for garbage carts")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'number_of_elements', 'current_activity',
                        'most_recent_action', 'street_address', 'zip_code', 'x_coordinate', 'y_coordinate',
                        'ward', 'police_district', 'community_area', 'ssa', 'latitude', 'longitude',
                        'location', 'historical_wards_03_15', 'zip_codes', 'community_areas',
                        'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_potholes(input_file: str) -> None:
    """ Import the requests for potholes to the database.

    :param input_file: The file from which to load the requests for potholes.
    """
    print("Getting requests for potholes")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'current_activity', 'most_recent_action',
                        'number_of_elements', 'street_address', 'zip_code', 'x_coordinate', 'y_coordinate',
                        'ward', 'police_district', 'community_area', 'ssa', 'latitude', 'longitude',
                        'location', 'historical_wards_03_15', 'zip_codes', 'community_areas',
                        'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_graffiti(input_file: str) -> None:
    """ Import the requests for graffiti to the database.

    :param input_file: The file from which to load the requests for graffiti.
    """
    print("Getting requests for graffiti")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'surface', 'graffiti_location', 'street_address',
                        'zip_code', 'x_coordinate', 'y_coordinate', 'ward', 'police_district', 'community_area',
                        'ssa', 'latitude', 'longitude', 'location', 'historical_wards_03_15', 'zip_codes',
                        'community_areas', 'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_rodent_baiting(input_file: str) -> None:
    """ Import the requests for rodent baiting to the database.

    :param input_file: The file from which to load the requests for rodent baiting.
    """
    print("Getting requests for rodent baiting")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'number_of_premises_baited', 'number_of_premises_w_garbage',
                        'number_of_premises_w_rats', 'current_activity', 'most_recent_action', 'street_address',
                        'zip_code', 'x_coordinate', 'y_coordinate', 'ward', 'police_district', 'community_area',
                        'latitude', 'longitude', 'location', 'historical_wards_03_15', 'zip_codes',
                        'community_areas', 'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_sanitation_complaints(input_file: str) -> None:
    """ Import the requests for sanitation code complaints to the database.

    :param input_file: The file from which to load the requests for sanitation code complaints.
    """
    print("Getting requests for sanitation code complaints")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'nature_of_code_violation', 'street_address',
                        'zip_code', 'x_coordinate', 'y_coordinate', 'ward', 'police_district', 'community_area',
                        'latitude', 'longitude', 'location', 'historical_wards_03_15', 'zip_codes',
                        'community_areas', 'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_tree_debris(input_file: str) -> None:
    """ Import the requests for tree debris to the database.

    :param input_file: The file from which to load the requests for tree debris.
    """
    print("Getting requests for tree debris")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'tree_location', 'current_activity',
                        'most_recent_action', 'street_address', 'zip_code', 'x_coordinate', 'y_coordinate',
                        'ward', 'police_district', 'community_area', 'latitude', 'longitude',
                        'location', 'historical_wards_03_15', 'zip_codes', 'community_areas',
                        'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_tree_trims(input_file: str) -> None:
    """ Import the requests for tree trims to the database.

    :param input_file: The file from which to load the requests for tree trims.
    """
    print("Getting requests for tree trims")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})

    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'tree_location', 'street_address', 'zip_code', 'x_coordinate',
                        'y_coordinate', 'ward', 'police_district', 'community_area', 'latitude', 'longitude',
                        'location', 'historical_wards_03_15', 'zip_codes', 'community_areas',
                        'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_alley_lights_out_or_street_lights_all_out(input_file: str, street_lights: bool):
    """ Import the requests for alley lights out or street lights all out (works the same for both of them) to the
    database.

    :param input_file: The file from which to load the requests for lights incidents.
    :param street_lights: Indicator if the method is called for street lights or not
    """
    if street_lights:
        print("Getting requests for street lights all out")
    else:
        print("Getting requests for alley lights out")

    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})
    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'street_address', 'zip_code', 'x_coordinate', 'y_coordinate',
                        'ward', 'police_district', 'community_area', 'latitude', 'longitude', 'location',
                        'historical_wards_03_15', 'zip_codes', 'community_areas', 'census_tracts', 'wards']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def import_street_lights_one_out(input_file: str):
    """ Import the requests for street lights one out to the database.

    :param input_file: The file from which to load the requests for lights incidents.
    """
    print("Getting requests for street lights one out")
    db = next(get_db())

    input_df = pd.read_csv(input_file, sep=',').replace({np.nan: None})
    input_df.columns = ['creation_date', 'status', 'completion_date', 'service_request_number',
                        'type_of_service_request', 'street_address', 'zip_code', 'x_coordinate', 'y_coordinate',
                        'ward', 'police_district', 'community_area', 'latitude', 'longitude', 'location']
    input_df = __dataframe_normalization__(input_df)
    docs = input_df.to_dict(orient='records')
    db['incidents'].insert_many(docs)


def __dataframe_normalization__(df: pd.DataFrame) -> pd.DataFrame:
    """ Normalizes a given dataframe to a desired condition (removes duplicate rows, convert times to timezone
    aware etc.)

    :param df: A pandas dataframe
    :return:  The normalized dataframe
    """
    df = df.copy(deep=True)

    df = df.drop_duplicates(['creation_date', 'status', 'completion_date', 'service_request_number',
                             'type_of_service_request', 'street_address', 'zip_code'], keep='last')

    return df
