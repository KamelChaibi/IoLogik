<template>
  <section class="p-4">
    <h2>Welcome to ioLogik Series</h2>
    <div class="card my-3">
      <div class="card-body">
        <p><strong>Model Name:</strong> E1242</p>
        <p><strong>Serial Number:</strong> TAEHC1023380</p>
        <p><strong>Firmware Version:</strong> V2.5 Build16081019</p>
        <p><strong>BIOS Version:</strong> V2.2.0</p>
        <p><strong>Ethernet MAC Address:</strong> 00:90:e8:4f:0a:36</p>
        <p><strong>Ethernet IP Address:</strong> {{ ipAddress }}</p>
        <p><strong>Peer to Peer:</strong> Disable</p>
      </div>
    </div>
    <h3>I/O Status</h3>
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>Channel</th>
                <th>Mode</th>
                <th>Status</th>
                <th>Filter</th>
                <th>Counter Trigger</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>DI-00</td>
                <td>DI</td>
                <td>OFF</td>
                <td>100.0 ms</td>
                <td>--</td>
              </tr>
            </tbody>
          </table>
  </section>
</template>

<script>
export default {
  props: {
    ipAddress: {
      type: String,
      required: true, 
    },
  },
};
</script>
