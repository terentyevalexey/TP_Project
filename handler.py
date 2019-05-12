from abc import ABC, abstractmethod


class EventHandler(ABC):
    @abstractmethod
    def on_mouse_click(self, *point):
        pass

    @abstractmethod
    def on_key_down(self, key):
        pass

    @abstractmethod
    def on_key_pressed(self, keys):
        pass

    @abstractmethod
    def update(self):
        pass
