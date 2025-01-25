<template>
    <div class="load-factory-default">
      <h2>Load Factory Default</h2>
      <button @click="resetToDefault">Reset to Factory Settings</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      resetToDefault() {
        console.log('Factory settings restored.');
      },
    },
  };
  </script>
  
  <style>
  .load-factory-default {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
  }
  </style>
  