from the_organizer.celery_task import make_celery
from the_organizer.service import amazon_product
from ..webapp import database as db, app as current_app
from the_organizer.models import Product
import time
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

celery = make_celery(current_app)

"""

    current['title'] = item.ItemAttributes.Title
    current['id'] = item.ASIN
    current['url'] = item.DetailPageURL
    current['ItemAttributes'] = str(item.ItemAttributes)
    current['image'] = item.SmallImage.URL
    current['product_title'] = product_title
    current['part_id'] = part_id
"""

# add(part_id, title, headline, description, primary_key, url,
# amazon_url,thumbnail):


@celery.task
def background_task(title, part_id):