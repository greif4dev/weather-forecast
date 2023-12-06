function toggleMenu() {
    var menu = document.getElementById("menu");
    var menuIcon = document.getElementById("menu-icon");

    if (menu.style.right === "0px") {
      menu.style.right = "-250px";
      menuIcon.style.display = "block";
    } else {
      menu.style.right = "0";
      menuIcon.style.display = "none";
    }
  }