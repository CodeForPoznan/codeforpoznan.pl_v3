import styles from './../main.scss';
const INITIAL_FONT_SIZE = styles.fontRootSize;

function resetFontSize(initialFontSize = INITIAL_FONT_SIZE) {
  localStorage.fontSize = initialFontSize;
  document.getElementsByTagName('html')[0].style.fontSize = initialFontSize;
}
function increaseFontSize(multiplier) {
  const initialFontSize = parseFloat(INITIAL_FONT_SIZE);
  const newFontSize = `${initialFontSize * multiplier}px`;

  localStorage.fontSize = newFontSize;
  document.getElementsByTagName('html')[0].style.fontSize = newFontSize;
}

// function getCurrentFontSize() {
// if (localStorage.fontSize) {
//     return parseFloat(localStorage.fontSize)
// }
//   const html = document.getElementsByTagName('html')[0];
//   const htmlStyle = window.getComputedStyle(html);

//   console.log(parseFloat(INITIAL_FONT_SIZE));
//   return parseFloat(htmlStyle.fontSize);
// }

export { resetFontSize, increaseFontSize };
