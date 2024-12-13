from abc import ABCMeta, abstractmethod


class IReplay:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_play_data(self):
        raise NotImplementedError