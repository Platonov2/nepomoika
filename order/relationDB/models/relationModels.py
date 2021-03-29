from flask_sqlalchemy import SQLAlchemy
from server import server


db = SQLAlchemy(server)

# -------------------model tables-------------------------


class Snapshot(db.Model):
    __tablename__ = 'snapshot_table'
    id = db.Column(db.Integer, primary_key=True)
    aggregate_id = db.Column(db.Integer, db.ForeignKey("aggregate_table.id"))
    version = db.Column(db.Integer, nullable=False)
    snapshot_data = db.Column(db.String(2000), nullable=False)


class Event(db.Model):
    __tablename__ = 'event_table'
    id = db.Column(db.Integer, primary_key=True)
    aggregate_id = db.Column(db.Integer, db.ForeignKey("aggregate_table.id"))
    version = db.Column(db.Integer, nullable=False)
    event_data = db.Column(db.String(2000), nullable=False)


class Aggregate(db.Model):
    __tablename__ = 'aggregate_table'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False)
    version = db.Column(db.Integer, nullable=False)

    events = db.relationship(Event, cascade="all,delete", lazy="select", backref=db.backref('aggregate', uselist=False))
    snapshots = db.relationship(Snapshot, cascade="all,delete", lazy="select", backref=db.backref('aggregate', uselist=False))

