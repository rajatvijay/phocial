(function() {
  if(window.myBookmarklet !== undefined) {
    myBookmarklet();
  }
  else {
    var script= document.createElement('script');
    script.setAttribute('src', 'http://phocial.in/static/js/bookmarklet.js?r='
      + Math.floor(Math.random()*999999999999999999999999999));
    document.body.appendChild(script);
  }
})();
