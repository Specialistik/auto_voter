casper.start("https://www.business-gazeta.ru/article/406831", function() {

    casper.thenEvaluate(function(term) {
        this.click('input[id="radio-variant-f164-148252"][value="yes"]');
        //document.querySelector('input[id="radio-variant-f164-148252"]').setAttribute('selected', true);
    });

  this.evaluate(function(){
    //trigger click event on submit button
    document.querySelector('input[type="submit"]').click();
  });
});