from ..webapp import database as db
from ..models.mixins import AnATTR


class StatusLog(AnATTR, db.Model):
    """
    Underly model for items in the store
    """
    # __tablename__ = 'items'

    """ FROM 'AnATTR MIXIN'
    attribute = Column(Unicode(256))
    value = Column(UnicodeText)
    active = Column(Boolean, default=False)
    minimum = Column(Unicode(256))
    maximum = Column(Unicode(256))
    """

    @staticmethod
    def add(attribute, value):
        return StatusLog(
            attribute=attribute,
            value=value)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()
