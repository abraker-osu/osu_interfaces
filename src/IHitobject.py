from abc import ABCMeta, abstractmethod
import numpy as np


class IHitobject():

    __metaclass__ = ABCMeta

    CIRCLE  = 1 << 0
    SLIDER  = 1 << 1
    NCOMBO  = 1 << 2
    SPINNER = 1 << 3
    # ???
    MANIALONG = 1 << 7

    @abstractmethod
    def pos_x(self) -> int:
        raise NotImplementedError


    @abstractmethod
    def pos_y(self) -> int:
        raise NotImplementedError


    @abstractmethod
    def start_time(self) -> int:
        raise NotImplementedError


    @abstractmethod
    def end_time(self) -> int:
        raise NotImplementedError


    @abstractmethod
    def tick_data(self) -> np.ndarray:
        raise NotImplementedError


    @abstractmethod
    def is_htype(self, hitobject_type: int) -> bool:
        raise NotImplementedError


    @abstractmethod
    def is_hlong(self) -> bool:
        raise NotImplementedError


    @abstractmethod
    def generate_tick_data(self, **kargs):
        raise NotImplementedError

