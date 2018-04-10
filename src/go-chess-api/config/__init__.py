import config.app_config as app_config

from pymongo import MongoReplicaSetClient
from pymongo import MongoClient
from pymongo.read_preferences import ReadPreference


def mongoDBHelper(dbName, readOnly=False):
    global connection
    if len(app_config.MONGODB_CONFIG) == 0:
        connection = None
        return
    try:
        connection
    except NameError:
        if app_config.MONGODB_CONFIG['RS'] != "":
            connection = MongoReplicaSetClient(
                app_config.MONGODB_CONFIG['URL'],
                replicaSet=app_config.MONGODB_CONFIG['RS'])
        else:
            connection = MongoClient(app_config.MONGODB_CONFIG['URL'])

    db = connection[dbName]
    if 'AUTH' in app_config.MONGODB_CONFIG:
        if 'true' == app_config.MONGODB_CONFIG['AUTH']:
            db.authenticate(app_config.MONGODB_CONFIG['USER'],
                            app_config.MONGODB_CONFIG['PASSWORD'])
        else:
            pass
    if readOnly:
        db.read_preference = ReadPreference.SECONDARY_PREFERRED
    else:
        db.read_preference = ReadPreference.PRIMARY_PREFERRED
    return db
