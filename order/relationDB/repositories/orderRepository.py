import json

from relationDB.models.relationModels import db, Aggregate, Event, Snapshot
from relationDB.models.enum.orderStatus import OrderStatus
from relationDB.models.order import Order
from relationDB.models.enum.enumDeserialize import from_string_to_enum


class OwnerException(Exception):
    def __init__(self, text):
        self.txt = text


class OrderRepository:

    @staticmethod
    def create_new_order(owner_id: int, order: Order) -> None:
        new_aggregate = Aggregate(owner_id=owner_id, version=0)
        db.session.add(new_aggregate)
        db.session.commit()
        OrderRepository.create_new_event(new_aggregate.id, order.serialize())

    @staticmethod
    def change_order_status(aggregate_id: int, new_status: OrderStatus):
        # aggregate = db.session.query(Aggregate).filter_by(id=aggregate_id).one()
        # if aggregate.owner_id != user_id:
        #     raise OwnerException("owner_id and user_id not match")
        order = OrderRepository.get_order(aggregate_id)
        if order.change_status(new_status):
            OrderRepository.create_new_event(aggregate_id, order.serialize_status())
            OrderRepository.create_snapshot(aggregate_id, order.serialize())

    @staticmethod
    def create_new_event(aggregate_id: int, event_data: {}) -> None:
        aggregate = db.session.query(Aggregate).filter_by(id=aggregate_id).one()
        new_event = Event(aggregate_id=aggregate_id, version=aggregate.version + 1, event_data=json.dumps(event_data))
        aggregate.version += 1
        db.session.add(aggregate)
        db.session.add(new_event)
        db.session.commit()

    @staticmethod
    def create_snapshot(aggregate_id: int, snapshot_date: {}) -> None:
        aggregate = db.session.query(Aggregate).filter_by(id=aggregate_id).one()
        new_snapshot = Snapshot(aggregate_id=aggregate_id, version=aggregate.version, snapshot_data=json.dumps(snapshot_date))
        db.session.add(new_snapshot)
        db.session.commit()

    @staticmethod
    def get_order(aggregate_id: int) -> Order:
        aggregate = db.session.query(Aggregate).filter_by(id=aggregate_id).one()
        if aggregate.snapshots:
            last_snapshot = [snapshot for snapshot in aggregate.snapshots if snapshot.version == aggregate.version][0]
            # events_from_aggregate = aggregate.events
            # events = []
            # for event in events_from_aggregate:
            #     if event.version > snapshot.version:
            #         events.append(event)
            events = [event for event in aggregate.events if event.version > last_snapshot.version]
            core_data = json.loads(last_snapshot.snapshot_data)
        else:
            events = aggregate.events
            core_data = {}
        for event in events:
            event_data = json.loads(event.event_data)
            core_data = {**core_data, **event_data}

        order = Order(core_data["order_sum"], core_data["order_products"], from_string_to_enum(core_data["order_status"]))
        return order

    @staticmethod
    def get_orders_by_user(user_id: int) -> []:
        aggregates = db.session.query(Aggregate).filter_by(owner_id=user_id).all()
        orders = []
        for aggregate in aggregates:
            order = OrderRepository.get_order(aggregate.id).serialize()
            order["aggregate_id"] = aggregate.id
            orders.append(order)

        return orders

    @staticmethod
    def get_all_orders() -> []:
        aggregates = db.session.query(Aggregate).all()
        orders = []
        for aggregate in aggregates:
            order = OrderRepository.get_order(aggregate.id).serialize()
            order["aggregate_id"] = aggregate.id
            orders.append(order)

        return orders
