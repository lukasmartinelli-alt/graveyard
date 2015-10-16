$(function() {
    var url = 'http://ghrr.gq:80/events';
    var socket = io(url);

    var commitsPerSecond = 0;
    var commentsPerSecond = 0;
    var watchPerSecond = 0;
    var createPerSecond = 0;


    socket.on('pushevent', function(event) {
      var freqModifier = event.payload.commits.length;
      T("pluck", {freq: 300 + 4 * freqModifier, mul:0.5}).bang().play();
    });

    socket.on('createevent', function(event) {
      createPerSecond += 1;
    });

    socket.on('watchevent', function(event) {
      watchPerSecond += 1;
    });

    socket.on('issuecommentevent', function(event) {
      commentsPerSecond += 1;
    });

    window.setInterval(function() {
      commitsPerSecond = 0;
      commentsPerSecond = 0;
    }, 1000);

    window.setInterval(function() {

      watchPerSecond = 0;
      createPerSecond = 0;
    }, 2000);
});
