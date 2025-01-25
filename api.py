from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary to store network settings
network_settings = {
    "dhcp_active": True,
    "ip_address": "192.168.1.100",
    "subnet_mask": "255.255.255.0",
    "cidr": "/24",
    "default_gateway": "192.168.1.1",
    "dns_1": "8.8.8.8",
    "dns_2": "8.8.4.4",
    "mac_address": "00:90:e8:4f:0a:36",
}

# Simulated DHCP-provided settings
dhcp_settings = {
    "ip_address": "192.168.1.100",
    "subnet_mask": "255.255.255.0",
    "default_gateway": "192.168.1.1",
}

@app.route("/network-settings", methods=["GET"])
def get_network_settings():
    """
    Endpoint to fetch the current network settings.
    """
    return jsonify(network_settings)

@app.route("/dhcp-settings", methods=["GET"])
def get_dhcp_settings():
    """
    Endpoint to fetch DHCP-provided settings.
    """
    return jsonify(dhcp_settings)

@app.route("/network-settings", methods=["POST"])
def update_network_settings():
    """
    Endpoint to update network settings.
    """
    data = request.json
    network_settings.update(data)
    return jsonify({"message": "Settings updated successfully!"})

@app.route("/get-ip", methods=["GET"])
def get_ip():
    """
    Endpoint to fetch the current IP address.
    """
    return jsonify({"ip": network_settings["ip_address"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)