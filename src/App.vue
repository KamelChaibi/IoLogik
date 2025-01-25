<template>
  <div id="app" class="container-fluid p-0">
    <header class="app-header text-white py-3">
      <h1 class="text-center">ioLogik Remote Ethernet I/O Server</h1>
      <div class="text-center small">
        <span>Model: E1242 Ethernet IO Server</span> |
        <span>IP: {{ ipAddress }}</span> |
        <span>MAC Address: 00:90:e8:4f:0a:36</span> |
        <span>Serial No: TAEHC1023380</span> |
        <span>Firmware: V2.5 Build16081019</span>
      </div>
    </header>

    <div class="d-flex">
      <aside class="sidebar vh-100">
        <nav class="nav flex-column p-3">
          <button
            v-for="(page, index) in pages"
            :key="index"
            class="btn btn-dark text-start w-100 mb-2"
            @click="navigatePage(page.component)"
          >
            {{ page.name }}
          </button>
        </nav>
      </aside>

      <main class="flex-grow-1 p-4 bg-light">
        <component :is="currentPage" :ipAddress="ipAddress" />
      </main>
    </div>
  </div>
</template>

<script>
import DeviceOverview from "./components/DeviceOverview.vue";
import ConfigurationPage from "./components/ConfigurationPage.vue";
import UserDefinedModbus from "./components/UserDefinedModbus.vue";
import AopcServerSettings from "./components/AopcServerSettings.vue";
import IoSettings from "./components/IoSettings.vue";
import PeerToPeerSettings from "./components/PeerToPeerSettings.vue";
import SnmpSettings from "./components/SnmpSettings.vue";
import RestfulSettings from "./components/RestfulSettings.vue";
import EthernetIpSettings from "./components/EthernetIpSettings.vue";
import SystemManagement from "./components/SystemManagement.vue";
import ChangePassword from "./components/ChangePassword.vue";
import LoadFactoryDefault from "./components/LoadFactoryDefault.vue";
import SaveRestart from "./components/SaveRestart.vue";

export default {
  name: "App",
  components: {
    DeviceOverview,
    ConfigurationPage,
    UserDefinedModbus,
    AopcServerSettings,
    IoSettings,
    PeerToPeerSettings,
    SnmpSettings,
    RestfulSettings,
    EthernetIpSettings,
    SystemManagement,
    ChangePassword,
    LoadFactoryDefault,
    SaveRestart,
  },
  data() {
    return {
      currentPage: "DeviceOverview",
      ipAddress: "Loading...", // Initialize with a placeholder
      pages: [
        { name: "Overview", component: "DeviceOverview" },
        { name: "Network Settings", component: "ConfigurationPage" },
        { name: "User-defined Modbus Addressing", component: "UserDefinedModbus" },
        { name: "AOCP Server Settings", component: "AopcServerSettings" },
        { name: "I/O Settings", component: "IoSettings" },
        { name: "Peer to Peer Settings", component: "PeerToPeerSettings" },
        { name: "SNMP Settings", component: "SnmpSettings" },
        { name: "RESTful Settings", component: "RestfulSettings" },
        { name: "Ethernet/IP Settings", component: "EthernetIpSettings" },
        { name: "System Management", component: "SystemManagement" },
        { name: "Change Password", component: "ChangePassword" },
        { name: "Load Factory Default", component: "LoadFactoryDefault" },
        { name: "Save/Restart", component: "SaveRestart" },
      ],
    };
  },
  methods: {
    fetchIPAddress() {
      fetch("http://192.168.1.24:5000/get-ip")
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          this.ipAddress = data.ip; // Update the ipAddress with the fetched value
        })
        .catch((error) => {
          console.error("Error fetching IP address:", error);
          this.ipAddress = "Error loading IP"; // Display an error message
        });
    },
    navigatePage(component) {
      this.currentPage = component;
    },
  },
  mounted() {
    this.fetchIPAddress(); // Fetch the IP address when the component is mounted
  },
};
</script>

<style scoped>
.app-header {
  background-color: #343a40;
}

.sidebar {
  background-color: #343a40;
  color: white;
  padding: 1rem;
}

.nav button {
  font-size: 14px;
  border: none;
}

.nav button:hover {
  background-color: #495057;
}

.text-white {
  color: white;
}
</style>