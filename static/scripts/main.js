window.onload = function(){
    console.log("test test");

    var app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#app',
        data: {
            message: 'Hello Vue!',
            npcs: []
        },
        methods: {
            greet: function(name) {
                console.log('Hello from ' + message + '!')
            }
        }
      });

}