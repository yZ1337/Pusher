const express = require('express');
const Pusher = require('pusher');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Initialize Pusher with your credentials
const pusher = new Pusher({
  appId: '1806190',
  key: 'b466625a5dad96340d2a',
  secret: '36bbb1cd7506c37d7e69',
  cluster: 'eu',
  useTLS: true
});

app.use(bodyParser.json());

// Endpoint to trigger an event
app.post('/trigger-event', (req, res) => {
  const { channel, event, message } = req.body;
  pusher.trigger(channel, event, { message: message });
  res.send('Event triggered');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
