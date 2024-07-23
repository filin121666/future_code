import abc


class Electriacal_appliance(abc.ABC):
    pass


class Computer(Electriacal_appliance):
    pass


class Phone(Electriacal_appliance):
    pass


class Smartphone(Phone, Computer):
    pass


class Samsung(Smartphone):
    pass
