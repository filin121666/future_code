import abc


class RailWayStation(abc.ABC):
    pass


class RailWayStation_worker(RailWayStation):
    pass


class Cashier(RailWayStation_worker):
    def sell_ticket(self):
        pass
