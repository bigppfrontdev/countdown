const sio = io('http://127.0.0.1:5000/');

sio.on('connect', () => {
  console.log('connected');
});

sio.on('disconnect', () => {
  console.log('disconnected');
});