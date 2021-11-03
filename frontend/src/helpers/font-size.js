import styles from './../main.scss';

const INITIAL_FONT_SIZE = styles.fontRootSize;
const DESKTOP_BREAKPOINT = parseFloat(styles.desktopBreakpoint);

function adjustFontSize() {
  const screenWidth = window.innerWidth > 0 ? window.innerWidth : screen.width;
  const fontLarge = parseFloat(INITIAL_FONT_SIZE) * 1.2;
  const currentFontSize = parseFloat(
    document.getElementsByTagName('html')[0].style.fontSize
  );

  if (screenWidth >= DESKTOP_BREAKPOINT && currentFontSize != fontLarge) {
    document.getElementsByTagName('html')[0].style.fontSize = `${fontLarge}px`;
  } else if (
    screenWidth < DESKTOP_BREAKPOINT &&
    currentFontSize != parseFloat(INITIAL_FONT_SIZE)
  ) {
    document.getElementsByTagName('html')[0].style.fontSize = INITIAL_FONT_SIZE;
  }
}

export { adjustFontSize };
