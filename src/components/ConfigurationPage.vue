<template>
  <div class="container py-4">
    <h1>Network Configuration</h1>

    <!-- Display current network settings -->
    <div class="card my-3">
      <div class="card-body">
        <h3>Current Configuration</h3>
        <ul class="list-group">
          <li class="list-group-item">
            DHCP Active: <strong>{{ networkSettings.dhcp_active ? 'Enabled' : 'Disabled' }}</strong>
          </li>
          <li class="list-group-item">
            IP Address: <strong>{{ networkSettings.ip_address || 'N/A' }}</strong>
          </li>
          <li class="list-group-item">
            Subnet Mask: <strong>{{ networkSettings.subnet_mask || 'N/A' }}</strong>
            <span v-if="networkSettings.cidr"> (CIDR: {{ networkSettings.cidr }})</span>
          </li>
          <li class="list-group-item">
            Default Gateway: <strong>{{ networkSettings.default_gateway || 'N/A' }}</strong>
          </li>
          <li class="list-group-item">
            DNS 1: <strong>{{ networkSettings.dns_1 || 'N/A' }}</strong>
          </li>
          <li class="list-group-item">
            DNS 2: <strong>{{ networkSettings.dns_2 || 'N/A' }}</strong>
          </li>
          <li class="list-group-item">
            MAC Address: <strong>{{ networkSettings.mac_address || 'N/A' }}</strong>
          </li>
        </ul>
      </div>
    </div>

    <!-- Form to update network settings -->
    <div class="card my-3">
      <div class="card-body">
        <h3>Update Configuration</h3>
        <form @submit.prevent="updateNetworkSettings">
          <div class="mb-3">
            <label for="dhcp" class="form-label">DHCP Active</label>
            <select
              id="dhcp"
              class="form-select"
              v-model="networkSettings.dhcp_active"
              @change="handleDhcpToggle"
            >
              <option :value="true">Enabled</option>
              <option :value="false">Disabled</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="ip" class="form-label">IP Address</label>
            <input
              type="text"
              id="ip"
              class="form-control"
              v-model="networkSettings.ip_address"
              :disabled="networkSettings.dhcp_active"
              :readonly="networkSettings.dhcp_active"
            />
          </div>
          <div class="mb-3">
            <label for="subnet" class="form-label">Subnet Mask</label>
            <input
              type="text"
              id="subnet"
              class="form-control"
              v-model="networkSettings.subnet_mask"
              :disabled="networkSettings.dhcp_active"
              :readonly="networkSettings.dhcp_active"
            />
          </div>
          <div class="mb-3">
            <label for="gateway" class="form-label">Default Gateway</label>
            <input
              type="text"
              id="gateway"
              class="form-control"
              v-model="networkSettings.default_gateway"
              :disabled="networkSettings.dhcp_active"
              :readonly="networkSettings.dhcp_active"
            />
          </div>
          <div class="mb-3">
            <label for="dns1" class="form-label">DNS 1</label>
            <input
              type="text"
              id="dns1"
              class="form-control"
              v-model="networkSettings.dns_1"
            />
          </div>
          <div class="mb-3">
            <label for="dns2" class="form-label">DNS 2</label>
            <input
              type="text"
              id="dns2"
              class="form-control"
              v-model="networkSettings.dns_2"
            />
          </div>
          <button type="submit" class="btn btn-primary">Save</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      networkSettings: {
        dhcp_active: true,
        ip_address: "",
        subnet_mask: "",
        cidr: "",
        default_gateway: "",
        dns_1: "",
        dns_2: "",
        mac_address: "",
      },
    };
  },
  methods: {
    // Fetch current network settings from the backend
    fetchNetworkSettings() {
      axios
        .get("http://192.168.1.24:5000/network-settings")
        .then((response) => {
          // Update the networkSettings object with the fetched data
          this.networkSettings = response.data;
        })
        .catch((error) => {
          console.error("Error fetching network settings:", error);
        });
    },

    // Update network settings on the backend
    updateNetworkSettings() {
      axios
        .post("http://192.168.1.24:5000/network-settings", this.networkSettings)
        .then(() => {
          alert("Network settings updated successfully!");
          this.fetchNetworkSettings(); // Refresh settings
        })
        .catch((error) => {
          console.error("Error updating network settings:", error);
        });
    },

    // Handle DHCP toggle
    handleDhcpToggle() {
      if (this.networkSettings.dhcp_active) {
        // If DHCP is enabled, fetch DHCP-provided settings
        axios
          .get("http://192.168.1.24:5000/dhcp-settings")
          .then((response) => {
            const dhcpData = response.data;
            // Update the networkSettings object with DHCP-provided settings
            this.networkSettings.ip_address = dhcpData.ip_address;
            this.networkSettings.subnet_mask = dhcpData.subnet_mask;
            this.networkSettings.default_gateway = dhcpData.default_gateway;
          })
          .catch((error) => {
            console.error("Error fetching DHCP settings:", error);
          });
      } else {
        // If DHCP is disabled, clear the fields (optional)
        this.networkSettings.ip_address = "";
        this.networkSettings.subnet_mask = "";
        this.networkSettings.default_gateway = "";
      }
    },
  },
  mounted() {
    this.fetchNetworkSettings();
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
.card {
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.list-group-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>