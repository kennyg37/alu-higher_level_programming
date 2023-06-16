$(function() {
    
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      method: 'GET',
      success: function(response) {
    
        var helloTranslation = response.hello;
  
    
        $('div#hello').text(helloTranslation);
      }
    });
});