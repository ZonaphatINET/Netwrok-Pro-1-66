const express = require('express');
const { Session } = require('snmp-native');
const app = express();
const port = 3000;
const ip_add = '192.168.75.50';
const community = 'private';

const managePort = (port, action, callback) => {
  const session = new Session({ host: ip_add, community });
  const oid = [1, 3, 6, 1, 2, 1, 2, 2, 1, 7, port];
  const type = 2;

  session.set({ oid, value: action, type }, (error) => {
    callback(error ? error : null);
    session.close();
  });
};

const getPortData = (oid, callback) => {
  const session = new Session({ host: ip_add, community });

  session.getSubtree({ oid }, (error, varbinds) => {
    const data = {};
    if (!error) varbinds.forEach(vb => data[vb.oid[vb.oid.length - 1]] = vb.value);
    callback(error, data);
    session.close();
  });
};

const getPortName = (callback) => getPortData([1, 3, 6, 1, 2, 1, 2, 2, 1, 2], callback);
const getPortStatus = (callback) => getPortData([1, 3, 6, 1, 2, 1, 2, 2, 1, 7], (error, data) => {
  const portStatus = {};
  if (!error) Object.entries(data).forEach(([port, value]) => portStatus[port] = value === 1 ? 'Up' : 'Down');
  callback(error, portStatus);
});

const resStatus = (res, error, status = 200) => res.status(status).send(error ? `Error: ${error.message}` : '');

     
const resHTML = (res, portStatus, portName) => res.send(`
  <html>
    <head>
      <title>Custom SNMP Port Status</title>
      <style>
        .status-up { color: green; }
        .status-down { color: red; }
      </style>
    </head>
    <body>
      <h1>Custom SNMP Port Status</h1>
      <table>
        <thead><tr><th>Port Name</th><th>Actions</th></tr></thead>
        <tbody>
          ${Object.entries(portStatus).map(([port]) => `
            <tr>
              <td class="${portStatus[port] === 'Up' ? 'status-up' : 'status-down'}">${portName[port] || 'Port ' + port}</td>
              <td>
                <a href="/manage/${port}/1">เปิด</a> 
                <a href="/manage/${port}/2">ปิด</a>
              </td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </body>
  </html>
`);
app.get('/manage/:port/:action', (req, res) => {
  const { port, action } = req.params;
  managePort(port, action, (error) => res.redirect(error ? '/error' : '/'));
});

app.get('/error', (req, res) => resStatus(res, 'Error occurred', 500));

app.get('/', (req, res) => {
  getPortStatus((error, portStatus) => {
    if (error) return resStatus(res, error, 500);
    getPortName((nameError, portName) => {
      if (nameError) return resStatus(res, nameError, 500);
      resHTML(res, portStatus, portName);
    });
  });
});

app.listen(port, () => console.log(`Server is running on http://localhost:${port}`));