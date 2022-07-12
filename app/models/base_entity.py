from app import db
from sqlalchemy.sql import func

class BaseEntity:
    createdate = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updatedate = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deletedate = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True)
