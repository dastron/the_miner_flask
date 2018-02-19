from the_miner.models import Miner
from the_miner.webapp import database as db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound


def getMinerID(primary_key):
    try:
        miner_exist = db.session.query(Miner).filter(
            Miner.primary_key == primary_key).one()

    except MultipleResultsFound, e:
        print e

    except NoResultFound, e:
        print 'no user, create one'

    return miner_exist
