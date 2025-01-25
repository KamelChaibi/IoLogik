<template>
    <div class="change-password">
      <h2>Change Password</h2>
      <form @submit.prevent="submitPasswordChange">
        <label>
          Current Password:
          <input type="password" v-model="currentPassword" />
        </label>
        <label>
          New Password:
          <input type="password" v-model="newPassword" />
        </label>
        <button type="submit">Change Password</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentPassword: '',
        newPassword: '',
      };
    },
    methods: {
      submitPasswordChange() {
        console.log('Password changed successfully.');
      },
    },
  };
  </script>
  
  <style>
  .change-password {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
  }
  </style>
  