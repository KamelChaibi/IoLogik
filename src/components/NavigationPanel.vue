<template>
  <nav class="nav flex-column p-3">
    <button
      class="btn btn-dark text-start w-100 mb-2"
      v-for="(page, index) in pages"
      :key="index"
      @click="navigate(page.component)"
    >
      {{ page.name }}
    </button>
  </nav>
</template>

<script>
export default {
  emits: ["navigate"],
  data() {
    return {
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
    navigate(component) {
      this.$emit("navigate", component); 
    },
  },
};
</script>
