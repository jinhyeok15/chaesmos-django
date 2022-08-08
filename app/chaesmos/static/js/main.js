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

// postoffice
const postofficeBackgroundWrapper = document.getElementById('postoffice-background-wrapper');
const solWrite = document.getElementById('sol-write');

const postofficeMailbox = document.getElementById('postoffice-mailbox');
const postofficeMailboxButton = document.getElementById('postoffice-mailbox-button');

let postofficeMailboxButtonClickState = false;

postofficeMailboxButton.addEventListener('click', e => {
  if (!postofficeMailboxButtonClickState) {
    postofficeMailboxButtonClickState = true;
    postofficeMailbox.classList.add("hidden");
    solWrite.classList.remove("hidden");
  }
});

postofficeBackgroundWrapper.addEventListener('click', e => {
  if (postofficeMailboxButtonClickState) {
    postofficeMailbox.classList.remove("hidden");
    postofficeMailboxButtonClickState = false;
    solWrite.classList.add("hidden");
  }
});
