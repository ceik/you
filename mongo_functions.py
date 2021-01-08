import csv
from pymongo import MongoClient


def get_order_items():
    """Return all order items in the local MongoDB as a list of lists."""
    client = MongoClient('localhost', 27017)
    db = client.you
    order_items = db.order_items

    result = []

    for doc in order_items.find():
        line = []
        for value in doc.values():
            line.append(str(value))

        result.append(line)

    client.close()

    print('order items retrieved successfully')
    return result


def import_order_items(data_file):
    """Import all order items in the provided data file to local
    Mongo DB instance."""
    client = MongoClient('localhost', 27017)

    db = client.you
    order_items = db.order_items

    with open(data_file, 'r') as source_file:
        reader = csv.reader(source_file, delimiter=',')
        keys = reader.__next__()
        for row in reader:
            order_item = dict(zip(keys, row))
            try:
                # Might be better to use insert_many() instead
                order_item_id = order_items.insert_one(order_item).inserted_id
                print('insert success: {}'.format(order_item_id))
            except:
                print('insert failed: {}'.format(order_item))

    print('order items import successful')
    client.close()


def drop_order_items():
    """Drop all entries in the order_items collection."""
    client = MongoClient('localhost', 27017)

    db = client.you
    order_items = db.order_items

    order_items.delete_many({})

    print('order items dropped')
    client.close()
