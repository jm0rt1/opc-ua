from opcua import Client, ua
from pyqt_plugin_system.base_plugin import BasePlugin
from PySide6.QtCore import Slot, QObject


class OPCUAWriterPlugin(BasePlugin):
    """
    Plugin that writes data to an OPC-UA server.
    """

    def __init__(self, server_url: str, node_id: str, parent=None):
        """
        Initializes the plugin with the OPC-UA server details.
        :param server_url: The URL of the OPC-UA server.
        :param node_id: The ID of the node to write data to.
        """
        super().__init__(parent)
        self.server_url = server_url
        self.node_id = node_id
        self.client = None

    def start(self):
        """
        Connects to the OPC-UA server and prepares the plugin.
        """
        try:
            # Connect to the OPC-UA server
            self.client = Client(self.server_url)
            self.client.connect()
            print(f"Connected to OPC-UA server at {self.server_url}.")
        except Exception as e:
            print(f"Failed to connect to OPC-UA server: {e}")

    def stop(self):
        """
        Disconnects from the OPC-UA server.
        """
        if self.client:
            self.client.disconnect()
            print(f"Disconnected from OPC-UA server at {self.server_url}.")

    @Slot(object)
    def write_value(self, value):
        """
        Writes a value to the OPC-UA server node.
        :param value: The value to write to the OPC-UA node.
        """
        if not self.client:
            print("Not connected to the OPC-UA server.")
            return

        try:
            node = self.client.get_node(self.node_id)
            # Modify the type as needed
            node.set_value(ua.Variant(value, ua.VariantType.Int16))
            print(f"Successfully wrote {value} to OPC-UA node {self.node_id}.")
        except Exception as e:
            print(f"Failed to write value to OPC-UA node: {e}")
