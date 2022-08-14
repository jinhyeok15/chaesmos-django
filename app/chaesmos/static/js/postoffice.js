import { requestWriteSolution } from "./api/request.js";

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

// read-write
let letterPage = 1;

const letters = document.getElementsByClassName('letter');

const letterButtonNext = document.getElementById('letter-button-next');
const letterButtonBack = document.getElementById('letter-button-back');

const solutionWriteSubmit = document.getElementById('solution-write-submit');

const noData = document.getElementById('letter-no-data');

window.onload = ()=>{
  if (letters.length!==0) {
    letters[letterPage-1].classList.remove('hidden');
  }
  else {
    letterButtonBack.classList.add("hidden");
    letterButtonNext.classList.add("hidden");
    noData.classList.remove("hidden");
    solutionWriteSubmit.disabled = true;
  }
  if (letters.length===1) {
    letterButtonNext.disabled = true;
  }
};

const letterList = JSON.parse(document.getElementById('letter-list').textContent)['letters'];

letterButtonBack.addEventListener('click', e=>{
  if (letterPage===letters.length) {
    letterButtonNext.disabled = false;
  }
  letters[letterPage-1].classList.add('hidden');
  letterPage--;
  if (letterPage===1) {
    letterButtonBack.disabled = true;
  }
  letters[letterPage-1].classList.remove('hidden');
});

letterButtonNext.addEventListener('click', e=>{
  if (letterPage===1) {
    letterButtonBack.disabled = false;
  }
  letters[letterPage-1].classList.add('hidden');
  letterPage++;
  if (letterPage===letters.length) {
    letterButtonNext.disabled = true;
  }
  letters[letterPage-1].classList.remove('hidden');
});

solutionWriteSubmit.addEventListener('click', e=>{
  e.preventDefault();

  const data = {
    letter: letterList[letterPage-1].id,
    main: document.getElementById('write-letter-text').value
  }

  requestWriteSolution(data)
    .then(result => {
      if (result.code === 200) window.location.replace('/success');
    })
    .catch(e => console.log(e));
});
