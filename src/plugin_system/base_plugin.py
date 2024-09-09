from abc import ABC, abstractmethod
from PySide6.QtCore import QObject


class BasePlugin(QObject, ABC):
    """
    Abstract base class for all plugins in the PySide6 plugin system.
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
