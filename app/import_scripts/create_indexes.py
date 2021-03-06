import pymongo

from app.db.db_connection import get_db


def create_indexes():
    db = next(get_db())
    db['incidents'].create_index([('type_of_service_request', pymongo.ASCENDING)])
    db['incidents'].create_index([('creation_date', pymongo.ASCENDING)])
    db['incidents'].create_index([('type_of_service_request', pymongo.ASCENDING), ('creation_date', pymongo.ASCENDING)])
    db['incidents'].create_index([('geo_location', pymongo.GEOSPHERE)])
    db['incidents'].create_index([('total_votes', pymongo.ASCENDING)])

    db['citizens'].create_index([('total_votes', pymongo.ASCENDING)])
    db['citizens'].create_index([('total_wards', pymongo.ASCENDING)])
    db['citizens'].create_index([('telephone_number', pymongo.ASCENDING)])
    db['citizens'].create_index([('name', pymongo.ASCENDING)])


if __name__ == '__main__':
    create_indexes()
