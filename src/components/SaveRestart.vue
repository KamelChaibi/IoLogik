<template>
    <div class="save-restart">
      <h2>Save and Restart</h2>
      <button @click="saveAndRestart">Save Settings and Restart</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      saveAndRestart() {
        console.log('Settings saved and system restarting.');
      },
    },
  };
  </script>
  
  <style>
  .save-restart {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
  }
  </style>
  