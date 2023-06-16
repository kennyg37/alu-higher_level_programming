$('DIV#add_item').click(function() {
  var LiElement = $("<li>Item</li>");
  $('UL.my_list').append(LiElement);  
})