import { requestLogout } from "./api/request.js";

export const logoutNavButton = document.getElementById('logout-nav-button');

if (logoutNavButton) {
  logoutNavButton.onclick = (ev) => {
    ev.preventDefault();
    requestLogout()
      .then(result => {
        if (result.code === 200) window.location.replace('/logout')
        else if (result.code === 400) console.log(result.errors)
        else console.log(result);
      })
      .catch(e => console.log(e));
  };
}
