from ..webapp import database as db
from ..models.mixins import AnATTR


class Sensor(AnATTR, db.Model):
    """
    Underly model for items in the store
    """
    # __tablename__ = 'items'

    """ FROM 'AnATTR MIXIN'
    title = title
    headline = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=True)

    primary_key = Column(Unicode(256), nullable=False, unique=True)
    url = Column(Unicode(2042), nullable=True)
    thumbnail = Column(Unicode(2042))

    active = Column(Boolean, default=False)

    submitted_date_time = db.Column(DateTime(timezone=True), nullable=False)
    updated_date_time = db.Column(DateTime(timezone=True), nullable=False)
    """

    @staticmethod
    def add(title, headline, primary_key):
        return Sensor(
            title=title,
            headline=headline,
            primary_key=primary_key)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()
