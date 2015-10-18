$(function() {
    var url = 'http://ghrr.gq:80/events';
    var socket = io(url);

    var commitsPerSecond = 0;
    var commentsPerSecond = 0;
    var watchPerSecond = 0;
    var createPerSecond = 0;


    socket.on('pushevent', function(event) {
      var rand = event.payload.commits.length;
      T("pluck", {freq: 200 + 4 * rand, mul:0.2}).bang().play();
    });

    socket.on('createevent', function(event) {
      createPerSecond += 1;
      T.soundfont.setInstrument(33);
      console.log('create');
      T.soundfont.play(60);
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
