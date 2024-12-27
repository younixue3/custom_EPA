// JavaScript to handle loader and page transition
document.addEventListener("DOMContentLoaded", function () {
  const loader = document.getElementById("loader");
  const mainContent = document.getElementById("main-content");

  // Simulate a delay (adjust or remove in production)
  setTimeout(() => {
    loader.style.display = "none"; // Hide the loader
    mainContent.classList.add("show"); // Show the main content with animation
  }, 1000); // Adjust delay as needed
});
// File: landing_page.js
document.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.remove("navbar-transparent");
    navbar.classList.add("bg-light", "navbar-light");
  } else {
    navbar.classList.add("navbar-transparent");
    navbar.classList.remove("bg-light", "navbar-light");
  }
});
