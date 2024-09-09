
# Plugins Documentation

## OPC UA plugins

### OPC UA Writer

```python
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from pyqt_plugin_system.plugin_manager import PluginManager


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPC-UA Writer Plugin Example")
        layout = QVBoxLayout()

        self.write_button = QPushButton("Write to OPC-UA")
        self.write_button.clicked.connect(self.write_data_to_opcua)
        layout.addWidget(self.write_button)

        self.setLayout(layout)

        # Initialize the plugin manager
        self.plugin_manager = PluginManager()

        # Load OPC-UA writer plugin
        self.plugin_manager.load_plugin("opcuaua_writer_plugin", "OPCUAWriterPlugin")

        # Plugin should now be accessible as an instance
        self.opcua_plugin = self.plugin_manager.plugins["OPCUAWriterPlugin"]
        
        # Provide the necessary parameters for the OPC-UA server and node
        self.opcua_plugin.server_url = "opc.tcp://localhost:4840"
        self.opcua_plugin.node_id = "ns=2;i=2"
        self.opcua_plugin.start()

    def write_data_to_opcua(self):
        # Trigger the plugin to write a value (you can change this value dynamically)
        self.opcua_plugin.write_value(42)  # Writing the value 42 to the OPC-UA node


# Running the application
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
