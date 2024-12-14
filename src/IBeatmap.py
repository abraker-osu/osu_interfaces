from abc import ABCMeta, abstractmethod
import numpy as np


class IBeatmap:

    __metaclass__ = ABCMeta

    PLAYFIELD_WIDTH  = 512  # osu!px
    PLAYFIELD_HEIGHT = 384  # osu!px

    class Metadata():

        def __init__(self):
            self.beatmap_format: int
            self.artist:         str
            self.title:          str
            self.version:        str
            self.creator:        str
            self.name:           str

            self.beatmap_id:     str
            self.beatmapset_id:  str
            self.beatmap_md5:    str


    class TimingPoint():

        def __init__(self):
            self.offset:            float
            self.beat_interval:     float
            self.inherited:         bool
            self.meter:             int

            self.beat_length:       float
            self.bpm:               float
            self.slider_multiplier: float


    class Difficulty():

        def __init__(self):
            self.hp: float | None
            self.cs: float | None
            self.od: float | None
            self.ar: float | None
            self.sm: float | None
            self.st: float | None


    @abstractmethod
    def data(self) -> np.ndarray:
        raise NotImplementedError


    @abstractmethod
    def get_diff_data(self) -> Difficulty:
        raise NotImplementedError


    @abstractmethod
    def get_hitobjects(self) -> list:
        raise NotImplementedError


    @abstractmethod
    def set_cs(self, cs: float):
        raise NotImplementedError


    @abstractmethod
    def set_ar(self, ar: float):
        raise NotImplementedError


    @abstractmethod
    def set_od(self, od: float):
        raise NotImplementedError


    @abstractmethod
    def set_hp(self, hp: float):
        raise NotImplementedError


    @abstractmethod
    def set_sm(self, sm: float):
        raise NotImplementedError


    @abstractmethod
    def set_st(self, st: float):
        raise NotImplementedError
