from pyqt_plugin_system.base_plugin import BasePlugin


class ExamplePlugin(BasePlugin):
    """
    An example plugin that prints messages when started and stopped.
    """

    def start(self):
        print("Example Plugin Started")

    def stop(self):
        print("Example Plugin Stopped")
