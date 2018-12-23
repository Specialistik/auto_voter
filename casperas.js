casper.start("https://www.business-gazeta.ru/article/406831", function() {

    casper.thenEvaluate(function(term) {
        this.click('input[id="radio-variant-f164-148252"][value="yes"]');
        //document.querySelector('input[id="radio-variant-f164-148252"]').setAttribute('selected', true);
    });

    document.querySelector(
//searches and fills the form with id="loginForm"
/*
  this.fill('form#loginForm', {
    'login':    'admin',
    'password':    '12345678'
   }, true);
*/
  this.evaluate(function(){
    //trigger click event on submit button
    document.querySelector('input[type="submit"]').click();
  });
});