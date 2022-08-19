import { requestLogout } from "./api/request.js";

export const logoutNavButton = document.getElementById('logout-nav-button');
const navLogo = document.getElementById('nav-logo');

const responsiveSet = () => {
  if (window.innerWidth < 640) {
    navLogo.innerText = '홈';
  } else {
    navLogo.innerText = '신비한 우체국';
  }
}

window.onresize = responsiveSet;
window.onload = responsiveSet;

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
