<template>
  <section class="p-4">
    <h2>System Management</h2>
    <div class="form-group">
      <label>Device Name:</label>
      <p class="form-control-plaintext">{{ deviceName }}</p>
    </div>
    <div class="form-group">
      <label>Firmware Version:</label>
      <p class="form-control-plaintext">{{ firmwareVersion }}</p>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      deviceName: "ioLogik E1242", // Example device name
      firmwareVersion: "V2.5 Build16081019", // Example firmware version
    };
  },
};
</script>
