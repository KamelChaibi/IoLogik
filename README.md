# ioLogik Remote Ethernet I/O Server

A web-based interface for configuring and managing Moxa ioLogik Ethernet I/O Servers. This application provides a user-friendly dashboard to monitor device status, configure network settings, I/O parameters, and various communication protocols such as Modbus, SNMP, Ethernet/IP, and more.

## Features

- **Device Overview**: Monitor the current status and basic information of the ioLogik device.
- **Network Settings**: Configure IP address, subnet mask, gateway, DNS, and DHCP settings.
- **I/O Settings**: Manage input/output configurations for the device.
- **Protocol Configurations**:
  - User-defined Modbus Addressing
  - AOPC Server Settings
  - Peer-to-Peer Settings
  - SNMP Settings
  - RESTful API Settings
  - Ethernet/IP Settings
- **System Management**: Handle system-level operations.
- **Security**: Change passwords and load factory defaults.
- **Save/Restart**: Apply changes and restart the device.

## Prerequisites

- Node.js (v14 or higher)
- npm (comes with Node.js)
- Python 3.x (for the backend API)
- Flask and flask-cors (install via pip)

## Installation

### Frontend (Vue.js)

1. Clone the repository:
   ```
   git clone https://github.com/KamelChaibi/IoLogik.git
   cd iologik
   ```

2. Install dependencies:
   ```
   npm install
   ```

### Backend (Flask API)

1. Ensure Python 3.x is installed.

2. Install required Python packages:
   ```
   pip install flask flask-cors
   ```

## Running the Application

### Start the Backend API

1. Navigate to the project root directory.

2. Run the Flask API server:
   ```
   python api.py
   ```
   The API will be available at `http://localhost:5000`.

### Start the Frontend

1. In a new terminal, from the project root:
   ```
   npm run serve
   ```
   The application will be available at `http://localhost:8080` (or the port specified by Vue CLI).

2. Open your browser and navigate to the provided URL to access the ioLogik configuration interface.

## API Documentation

The backend provides the following RESTful endpoints:

- `GET /network-settings`: Retrieve current network settings.
- `GET /dhcp-settings`: Retrieve DHCP-provided settings.
- `POST /network-settings`: Update network settings (expects JSON payload).
- `GET /get-ip`: Retrieve the current IP address.

All endpoints support CORS for cross-origin requests from the frontend.

## Project Structure

- `src/`: Vue.js frontend source code
  - `components/`: Reusable Vue components for each configuration page
  - `App.vue`: Main application component
  - `main.js`: Entry point for the Vue app
- `api.py`: Flask backend API
- `public/`: Static assets
- `package.json`: Frontend dependencies and scripts

## Compiles and Hot-Reloads for Development

```
npm run serve
```

## Compiles and Minifies for Production

```
npm run build
```

## Lints and Fixes Files

```
npm run lint
```

## Customize Configuration

See [Configuration Reference](https://cli.vuejs.org/config/).
