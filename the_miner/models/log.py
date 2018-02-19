from ..webapp import database as db
from ..models.mixins import BaseEntityMixin


class StatusLog(BaseEntityMixin, db.Model):
    """
    Underly model for items in the store
    """
    # __tablename__ = 'items'

    """ FROM 'BaseEntityMixin MIXIN'
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
    # part_id = db.Column(db.Integer, ForeignKey('parts.id'))
    # part = db.relationship("Part")



    @staticmethod
    def add(title, headline, description, primary_key, url, thumbnail):
        return StatusLog(
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
