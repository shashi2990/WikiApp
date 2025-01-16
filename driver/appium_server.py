# driver/appium_server.py

import time
import subprocess


def start_appium_server():
    """Start the Appium server in a subprocess."""
    appium_process = subprocess.Popen(
        ["appium", "--relaxed-security"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(5)  # Wait for the server to start
    return appium_process


def stop_appium_server(process):
    """Stop the Appium server."""
    process.terminate()
    process.wait()
