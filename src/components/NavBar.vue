<template>
    <div :class="['nav-bar', { 'hidden': isHidden, 'scrolled': hasScrolled }]">
      <div class="nav-wrapper">
        <!-- Hamburger Menu for Mobile -->
        <div class="hamburger-menu" @click="toggleMobileMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
  
        <!-- Logo Section -->
        <div class="name-heading">
          <img src="@/assets/navbar-photo.png" alt="Logo">
        </div>
  
        <!-- Navigation sections -->
        <nav :class="['nav-sections', { 'mobile-visible': showMobileMenu }]">
          <ul class="nav-links">
            <li><a href="#experience-section" @click="closeMobileMenu">Home</a></li>
            <li><a href="#skills" @click="closeMobileMenu">About</a></li>
            <li><a href="#coding" @click="closeMobileMenu">Themes</a></li>
            <li><a href="#projects" @click="closeMobileMenu">Prizes</a></li>
            <li><a href="#certificates" @click="closeMobileMenu">Contact</a></li>
            <li>
              <a
                href="https://www.linkedin.com/in/kayalennian"
                target="_blank"
                class="connect-btn"
                @click="closeMobileMenu"
              >
                Register
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "NavBar",
    data() {
      return {
        isHidden: false,
        lastScrollPosition: 0,
        hasScrolled: false,
        showMobileMenu: false, // Toggles the mobile menu
      };
    },
    methods: {
      handleScroll() {
        const currentScrollPosition = window.pageYOffset;
  
        if (currentScrollPosition > this.lastScrollPosition) {
          this.isHidden = true;
        } else {
          this.isHidden = false;
        }
  
        this.lastScrollPosition = currentScrollPosition;
  
        if (currentScrollPosition > 200) {
          this.hasScrolled = true;
        } else {
          this.hasScrolled = false;
        }
      },
      toggleMobileMenu() {
        this.showMobileMenu = !this.showMobileMenu;
      },
      closeMobileMenu() {
        this.showMobileMenu = false;
      },
    },
    mounted() {
      window.addEventListener("scroll", this.handleScroll);
    },
    beforeUnmount() {
      window.removeEventListener("scroll", this.handleScroll);
    },
  };
  </script>
  
  <style scoped>
  /* General nav-bar styles with glass effect */
  html {
    scroll-behavior: smooth;
  }
  
  .nav-bar {
    background: rgba(255, 255, 255, 0.2); /* Transparent white for glass effect */
    backdrop-filter: blur(10px); /* Blurs the background behind the navbar */
    -webkit-backdrop-filter: blur(10px); /* For Safari support */
    padding: 1px 2px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); /* Softer shadow for a glassy look */
    border: 1px solid rgba(255, 255, 255, 0.3); /* Light border for definition */
    display: flex;
    justify-content: space-between; /* Keep items spaced evenly */
    align-items: center;
    position: fixed; /* Fixed position at the top */
    top: 20px; /* Gap between the nav-bar and the top of the viewport */
    left: 50%; /* Center horizontally */
    transform: translateX(-50%); /* Proper horizontal centering */
    width: 65%; /* Width for laptop/desktop */
    z-index: 1000; /* Ensure it stays on top */
    height: 80px; /* Fixed height for navbar */
    border-radius: 40px; /* Oval shape */
    transition: all 0.3s ease-in-out; /* Smooth transition for floating effect */
  }
  
  /* Class to hide the navbar */
  .nav-bar.hidden {
    top: -100px; /* Move it off the top of the screen */
  }
  
  /* Class to change the navbar background when scrolled */
  .nav-bar.scrolled {
    background-color: #757575; /* Set background color to #757575 when scrolled */
  }
  
  .nav-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 0 20px;
  }
  
  /* Name Heading (Logo Section) */
  .name-heading {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-grow: 0; 
    padding: 50px; /* Center the logo within available space */
  }
  
  .name-heading img {
    max-width: 100%; /* Ensure it doesn't exceed the width of its container */
    max-height: 80px; /* Maintain the original size you provided */
    object-fit: contain;
  }
  
  /* Navigation sections */
  .nav-sections {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-grow: 2;
  }
  
  .nav-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    align-items: center;
  }
  
  .nav-links li {
    margin-left: 20px;
    margin-right: 20px;
  }
  
  .nav-links a {
    text-decoration: none;
    font-family: "Montserrat", sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: white;
    transition: color 0.3s ease, transform 0.3s ease;
  }
  
  .nav-links a:hover {
    color: #1f1f39;
    transform: scale(1.1);
  }
  
  .connect-btn {
    background-color: #000;
    color: white !important;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-family: "Montserrat", sans-serif;
    font-weight: 600;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
  }
  
  .connect-btn:hover {
    background-color: #333;
    transform: scale(1.1);
  }
  
  /* Hamburger menu */
  .hamburger-menu {
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 20px;
    cursor: pointer;
  }
  
  .hamburger-menu span {
    display: block;
    height: 3px;
    background: white;
    border-radius: 2px;
    transition: 0.3s ease;
  }
  
  /* Adjustments for tablet screens (between 768px and 1024px) */
  @media screen and (min-width: 769px) and (max-width: 1024px) {
    .nav-bar {
      width: 80%; /* Adjust navbar width to fit better on tablets */
      height: 90px; /* Slightly increase height to avoid overlap */
      padding: 0 10px; /* Adjust padding for better spacing */
    }
  
    .name-heading img {
      max-height: 70px; /* Adjust max height for the logo */
    }
  
    .nav-links {
      justify-content: space-between; /* Distribute links evenly */
    }
  
    .nav-links li {
      margin-left: 15px; /* Reduce margin between links */
      margin-right: 15px;
    }
  
    .connect-btn {
      padding: 10px 20px; /* Reduce padding for better fit */
      font-size: 14px; /* Adjust font size for button text */
    }
  }
  
  /* Mobile styles */
  @media screen and (max-width: 768px) {
    .hamburger-menu {
      display: flex;
      position: absolute;
      left: 20px;
    }
  
    .nav-sections {
      display: none;
    }
  
    .nav-sections.mobile-visible {
      display: flex;
    }
  
    .nav-links {
      flex-direction: column;
      position: absolute;
      top: 100%;
      left: 0;
      width: 100%;
      background: rgba(0, 0, 0, 0.8);
      padding: 10px 0;
      border-radius: 0 0 20px 20px;
    }
  
    .nav-links li {
      margin: 10px 0;
    }
  
    .nav-links a {
      font-size: 16px;
      text-align: center;
    }
  }
  </style>
  