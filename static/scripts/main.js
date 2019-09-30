var app;
window.onload = function(){
    console.log("test test");

    app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#app',
        data: {
            message: 'Hello Vue!',
            npcs: ['safafsafasf']
        },
        methods: {
            greet: function(name) {
                console.log('Hello from ' + message + '!')
            }
        }
      });

}