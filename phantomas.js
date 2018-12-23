var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36";
page.open('https://www.business-gazeta.ru/article/406831', function(status) {
  if (status !== 'success') {
    console.log('Unable to access network');
  } else {
    var ua = page.evaluate(function() {
       document.getElementById('radio-variant-f164-148252').click();
       var forms = document.getElementsByTagName('form');
       console.log(forms[0]);
       console.log(forms[1]);
       console.log(forms[2]);
       //document.getElementsByClassName("login-form");
    });
    console.log(ua);
  }
  phantom.exit();
});