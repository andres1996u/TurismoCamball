'use strict';

/**
 * Navbar toggle functionality
 */
const overlay = document.querySelector("[data-overlay]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const navToggleHandler = () => {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
};

// Adding event listeners for navbar toggle
[navOpenBtn, navCloseBtn, overlay, ...navLinks].forEach(elem => {
  elem.addEventListener("click", navToggleHandler);
});

/**
 * Header sticky and "Go to Top" button functionality
 */
const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", () => {
  const isScrolled = window.scrollY >= 200;
  header.classList.toggle("active", isScrolled);
  goTopBtn.classList.toggle("active", isScrolled);
});

/**
 * Button actions for saving and fetching destinations
 */
document.getElementById('save-btn')?.addEventListener('click', () => {
  const data = {
    name: 'Termales San Vicente',
    location: 'Risaralda, Colombia',
    description: 'Un lugar para relajarse en aguas termales.'
  };

  fetch('/save', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => alert(data.message))
  .catch(error => console.error('Error:', error));
});

document.getElementById('fetch-btn')?.addEventListener('click', () => {
  fetch('/get_destinations')
    .then(response => response.json())
    .then(data => {
      const content = document.getElementById('content');
      if (content) {
        content.innerHTML = data.map(destination => `
          <div>
            <h3>${destination.name}</h3>
            <p>${destination.description}</p>
          </div>
        `).join('');
      }
    })
    .catch(error => console.error('Error:', error));
});
