var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36";
page.open('https://www.business-gazeta.ru/article/406831', function(status) {
    console.log('like things began to happen');
  if (status !== 'success') {
    console.log('Unable to access network');
  } else {
    var ua = page.evaluate(function() {
        console.log('page has been evaluated')
       var radiobutton = document.getElementById('radio-variant-f164-148252').click();
       console.log(radiobutton);
       var forms = document.getElementsByTagName('form');
       console.log(forms[0].innerText);
       console.log(forms[1].innerText);
       console.log(forms[2].innerText);
       return;
       //document.getElementsByClassName("login-form");
    });
    console.log(ua);
  }
  phantom.exit();
});