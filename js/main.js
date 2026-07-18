document.addEventListener('DOMContentLoaded', () => {
  // Mobile Hamburger Toggle
  const burgerMenu = document.querySelector('.burger-menu');
  const body = document.body;

  if (burgerMenu) {
    burgerMenu.addEventListener('click', () => {
      body.classList.toggle('menu-open');
    });
  }

  // Close menu on mobile when clicking any link
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      body.classList.remove('menu-open');
    });
  });

  // Dynamic Active Page Link Highlighter
  const currentPath = window.location.pathname;
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    // Match root page or specific pathnames
    if (
      currentPath === linkPath || 
      (linkPath === 'index.html' && (currentPath === '/' || currentPath.endsWith('/index.html') || currentPath === '')) ||
      (currentPath.includes(linkPath) && linkPath !== 'index.html')
    ) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    } else {
      link.classList.remove('active');
      link.removeAttribute('aria-current');
    }
  });
});
