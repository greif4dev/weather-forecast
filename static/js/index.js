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

const menu = 
  ` 
    <div class="close-btn" onclick="toggleMenu()">×</div>
    <a href="/perfil"><i class="fa-solid fa-user" style="color: #ffffff;"></i>ㅤPerfil</a>
    <a href="#"><i class="fa-solid fa-clock-rotate-left"></i>ㅤHistórico</a>
    <a href="/home"><i class="fa-solid fa-map-location-dot" style="color: #ffffff;"></i>ㅤHome</a>
    <div class="logout">
      <a href="/"><i class="fa-solid fa-right-from-bracket" style="color: #ffffff;"></i>ㅤLogout</a>
    </div>
  <div id="menu-icon" onclick="toggleMenu()">☰</div>`;

document.getElementById('menu').innerHTML = menu;