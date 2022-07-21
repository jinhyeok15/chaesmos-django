import { HOST, requestLogout } from "./api/request.js";

export const logoutNavButton = document.getElementById('logout-nav-button');

if (logoutNavButton) {
  logoutNavButton.onclick = (event) => {
    event.preventDefault();
    requestLogout();
    location.replace(`${HOST}/login`)
  };
}
