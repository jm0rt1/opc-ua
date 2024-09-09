import importlib
from PySide6.QtCore import QObject


class PluginManager(QObject):
    """
    Class for managing plugins in the PySide6 application.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.plugins = {}

    def load_plugin(self, plugin_name: str, class_name: str):
        """
        Dynamically loads and instantiates a plugin by name.
        """
        try:
            module = importlib.import_module(plugin_name)
            plugin_class = getattr(module, class_name)
            plugin_instance = plugin_class()
            plugin_instance.start()  # Start the plugin
            self.plugins[class_name] = plugin_instance
            print(f"Plugin {class_name} loaded successfully.")
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Failed to load plugin: {e}")

    def unload_plugin(self, class_name: str):
        """
        Stops and unloads a plugin by class name.
        """
        plugin = self.plugins.get(class_name)
        if plugin:
            plugin.stop()  # Stop the plugin
            del self.plugins[class_name]
            print(f"Plugin {class_name} unloaded successfully.")

    def list_plugins(self):
        """
        Returns a list of currently loaded plugins.
        """
        return list(self.plugins.keys())
