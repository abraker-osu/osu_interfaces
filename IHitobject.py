from abc import ABCMeta, abstractmethod


class IHitobject:

    __metaclass__ = ABCMeta

    @abstractmethod
    def pos_x(self):
        raise NotImplementedError


    @abstractmethod
    def pos_y(self):
        raise NotImplementedError


    @abstractmethod
    def start_time(self):
        raise NotImplementedError


    @abstractmethod
    def end_time(self):
        raise NotImplementedError