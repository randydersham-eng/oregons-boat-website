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

  // Play Movie Button Click Handler
  const playBtn = document.getElementById('play-movie-btn');
  const videoIframe = document.querySelector('.video-container iframe');

  if (playBtn && videoIframe) {
    playBtn.addEventListener('click', () => {
      // Smoothly scroll the video into view
      videoIframe.scrollIntoView({ behavior: 'smooth', block: 'center' });

      // Trigger Vimeo play via postMessage
      try {
        videoIframe.contentWindow.postMessage(JSON.stringify({ method: 'play' }), '*');
      } catch (e) {
        console.log('Vimeo postMessage error:', e);
      }

      // Append autoplay parameter to iframe src if not present
      let currentSrc = videoIframe.getAttribute('src');
      if (!currentSrc.includes('autoplay=1')) {
        const separator = currentSrc.includes('?') ? '&' : '?';
        videoIframe.setAttribute('src', currentSrc + separator + 'autoplay=1');
      }
    });
  }
});
