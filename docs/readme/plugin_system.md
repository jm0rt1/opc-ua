# Plugin System Manual

## Usage in PyQt Application
Once packaged and installed via pip install pyqt-plugin-system, you can use the library in your PyQt application like this:

python
Copy code
from pyqt_plugin_system.plugin_manager import PluginManager
from PyQt5.QtWidgets import QApplication

app = QApplication([])

# Initialize the plugin manager
plugin_manager = PluginManager()

# Dynamically load a plugin
plugin_manager.load_plugin("example_plugin", "ExamplePlugin")

# List loaded plugins
print(plugin_manager.list_plugins())

# Unload a plugin
plugin_manager.unload_plugin("ExamplePlugin")

app.exec_()

