<template>
  <section class="p-4">
    <h2>I/O Settings</h2>

    <!-- Inputs Section -->
    <div class="card my-3">
      <div class="card-body">
        <h3>Inputs (DI)</h3>
        <ul class="list-group">
          <li
            class="list-group-item d-flex flex-column"
            v-for="index in 8"
            :key="'input-' + index"
          >
            <div class="d-flex justify-content-between align-items-center">
              <span><strong>DI {{ index }}</strong></span>
              <span>Acceptable Types: DI, Counter, Freq</span>
            </div>
            <div class="d-flex justify-content-between align-items-center mt-2">
              <label>
                Type:
                <select
                  class="form-select"
                  v-model="getInput(index).type"
                  @change="updateInputType(index)"
                >
                  <option value="DI">DI</option>
                  <option value="Counter">Counter</option>
                  <option value="Freq">Freq</option>
                </select>
              </label>
              <span>Value DI: <strong>{{ getInput(index).value ? 'ON' : 'OFF' }}</strong></span>
              <span>Value Count: <strong>{{ getInput(index).count || 0 }}</strong></span>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <!-- Outputs Section -->
    <div class="card my-3">
      <div class="card-body">
        <h3>Outputs (DO)</h3>
        <ul class="list-group">
          <li
            class="list-group-item d-flex flex-column"
            v-for="index in 8"
            :key="'output-' + index"
          >
            <div class="d-flex justify-content-between align-items-center">
              <span><strong>DO {{ index }}</strong></span>
              <span>Acceptable Types: DO, Pulse</span>
            </div>
            <div class="d-flex justify-content-between align-items-center mt-2">
              <label>
                Type:
                <select
                  class="form-select"
                  v-model="getOutput(index).type"
                  @change="updateOutputType(index)"
                >
                  <option value="DO">DO</option>
                  <option value="Pulse">Pulse</option>
                </select>
              </label>
              <span>
                Value DO:
                <strong>{{ getOutput(index).value ? 'ON' : 'OFF' }}</strong>
                <button
                  class="btn btn-sm btn-primary ms-3"
                  @click="toggleOutput(index)"
                >
                  Toggle
                </button>
              </span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      inputs: [],
      outputs: [],
    };
  },
  methods: {
    // Fetch I/O settings from the backend
    fetchIoSettings() {
      axios
        .get("http://192.168.1.24:5000/io-settings")
        .then((response) => {
          this.inputs = response.data.inputs;
          this.outputs = response.data.outputs;
        })
        .catch((error) => {
          console.error("Error fetching I/O settings:", error);
        });
    },
    // Get input by index
    getInput(index) {
      return (
        this.inputs.find((input) => input.channel === `DI ${index}`) || {
          type: "DI",
          value: false,
          count: 0,
        }
      );
    },
    // Get output by index
    getOutput(index) {
      return (
        this.outputs.find((output) => output.channel === `DO ${index}`) || {
          type: "DO",
          value: false,
        }
      );
    },
    // Update input type
    updateInputType(index) {
      const input = this.getInput(index);
      axios
        .post("http://192.168.1.24:5000/io-settings", {
          inputs: [
            {
              channel: `DI ${index}`,
              type: input.type,
            },
          ],
        })
        .catch((error) => {
          console.error("Error updating input type:", error);
        });
    },
    // Update output type
    updateOutputType(index) {
      const output = this.getOutput(index);
      axios
        .post("http://192.168.1.24:5000/io-settings", {
          outputs: [
            {
              channel: `DO ${index}`,
              type: output.type,
            },
          ],
        })
        .catch((error) => {
          console.error("Error updating output type:", error);
        });
    },
    // Toggle output value
    toggleOutput(index) {
      const output = this.getOutput(index);
      const updatedValue = !output.value;

      axios
        .post("http://192.168.1.24:5000/io-settings", {
          outputs: [
            {
              channel: `DO ${index}`,
              value: updatedValue,
            },
          ],
        })
        .then(() => {
          output.value = updatedValue;
        })
        .catch((error) => {
          console.error("Error toggling output:", error);
        });
    },
  },
  mounted() {
    this.fetchIoSettings();
  },
};
</script>

<style scoped>
.list-group-item {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>