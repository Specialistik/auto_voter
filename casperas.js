casper.start("https://www.business-gazeta.ru/article/406831", function() {
    this.waitForSelector('form[action="/polls/vote"]');
});

casper.thenEvaluate(function() {
    this.click('input[id="radio-variant-f164-148252"][value="yes"]');
    //document.querySelector('input[id="radio-variant-f164-148252"]').setAttribute('selected', true);
});

casper.thenEvaluate(function(){
//trigger click event on submit button
    document.querySelector('input[type="submit"]').click();
});

casper.run();