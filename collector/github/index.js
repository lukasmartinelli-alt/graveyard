

var ghrrUrl = process.env.GHRR_URL || 'http://ghrr.gq:80/events';
var natsUrl = process.env.NATS_URL || 'nats://localhost:4222';

var socket = require('socket.io-client')(ghrrUrl);
var nats = require('nats').connect({ url: natsUrl });

nats.on('error', function(event) {
    console.log(event);
});

socket.on('pushevent', function(event){
    console.log('Push: %s', event.repo.name);
    nats.publish('github.pushevent', event);
});
