var casper = require('casper').create({
    verbose: true,
    logLevel: 'debug'
});


casper.start("https://www.business-gazeta.ru/article/406831", function() {
    console.log('voting page loaded');
    this.waitForSelector('form[action="/polls/vote"]');

    casper.thenEvaluate(function() {
        this.click('input[id="radio-variant-f164-148252"][value="yes"]');
        //casper.wait(4000, function(){echo('2')});
        response = document.querySelector("form[action='/polls/vote']").submit();
        console.log(response);
       
        //document.querySelector('input[id="radio-variant-f164-148252"]').setAttribute('selected', true);
    });

    casper.on('resource.received', function(resp) {
        this.echo(JSON.stringify(resp, null, 4));
    });

    casper.then(function () {
        console.log('clicked ok, new location is ' + this.getCurrentUrl());
        console.log(this.response());
    });


    
});


casper.run(function() {
    console.log('casper run has been entered');
    console.log(this.getCurrentUrl(), this.response()); 
    this.exit();
});