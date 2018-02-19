from ..webapp import database as db
from ..models.mixins import AnATTR


class EventLog(AnATTR, db.Model):
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
    rig = db.Column(Unicode(256))
    miner1 = db.Column(db.Boolean, default=True)
    miner2 = db.Column(db.Boolean, default=True)
    miner3 = db.Column(db.Boolean, default=True)
    miner4 = db.Column(db.Boolean, default=True)
    miner5 = db.Column(db.Boolean, default=True)
    miner6 = db.Column(db.Boolean, default=True)

    raw = db.Column(db.UnicodeText(), nullable=False)
    status = db.Column(db.Boolean, default=False)

    @staticmethod
    def add(title, headline, description, primary_key, url, thumbnail):
        return EventLog(
            title=title,
            headline=headline,
            description=description,
            primary_key=primary_key,
            url=url,
            thumbnail=thumbnail)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()
