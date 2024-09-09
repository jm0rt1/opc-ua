from abc import ABC, abstractmethod
from PyQt5.QtCore import QObject


class BasePlugin(QObject, ABC):
    """
    Abstract base class for all plugins in the PyQt plugin system.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

    @abstractmethod
    def start(self):
        """
        Method to start the plugin. All plugins must implement this.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Method to stop the plugin. All plugins must implement this.
        """
        pass
