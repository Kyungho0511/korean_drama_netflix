$(document).ready(function () {
  $(".poster").hover(
    function () {
      var randomColor = getRandomColor();
      $(this).css("background-color", randomColor);
    },
    function () {
      $(this).css("background-color", "");
    }
  );

  function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
});
