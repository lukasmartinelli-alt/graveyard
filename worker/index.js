var vm = require('vm');
var util = require('util');

//var natsUrl = process.env.NATS_URL || 'nats://localhost:4222';
//var nats = require('nats').connect({ url: natsUrl });

//nats.subscribe('github.pushevent', function(msg) {
//    console.log('Received a message: ' + msg);
    var userCode = '(function(event) {' +
               '   return event + 1;' +
               '})(event)';
    var sandboxCode = 'var result = ' + userCode;
    var sandbox = { event: 1 };

    vm.runInNewContext(code, sandbox);
    console.log(util.inspect(sandbox));
//});
