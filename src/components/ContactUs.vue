<template>
    <div class="contact-container" ref="contactSection">
      <h1 class="contact-heading">CONTACT US</h1>
      <p class="contact-description">
        Have questions or want to connect? Feel free to reach out!
      </p>
  
      <div class="contact-content">
        <!-- Google Map Section -->
        <div class="map-container" ref="map">
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3916.7232852267545!2d77.060075!3d10.826633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTDCsDQ5JzMzLjkiTiA3N8KwMDMnMzYuMiJF!5e0!3m2!1sen!2sin!4v1678131632243!5m2!1sen!2sin"
            width="100%"
            height="300"
            style="border:0; border-radius: 10px;"
            allowfullscreen=""
            loading="lazy"
          ></iframe>
        </div>
  
        <!-- Coordinators Section -->
        <div class="coordinator-container" ref="coordinator">
          <h2 class="contact-heading">Staff Coordinator</h2>
          <p class="contact-description"><strong>Name:</strong> Mr.Sathish Kumar</p>
          <p class="contact-description"><strong>Contact:</strong> +91 98765 43210</p>
  
          <h2 class="contact-heading">Student Coordinator</h2>
          <p class="contact-description"><strong>Name:</strong> Kayal Ennian</p>
          <p class="contact-description"><strong>Contact:</strong> +91 90258 29115</p>
          <p class="contact-description"><strong>Name:</strong> Kayal Ennian</p>
          <p class="contact-description"><strong>Contact:</strong> +91 90258 29115</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ContactUs",
    mounted() {
      const observerOptions = {
        root: null,
        threshold: 0.1,
      };
  
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("animate");
            if (entry.target.classList.contains("map-container")) {
              this.animateMap();
            }
          } else {
            entry.target.classList.remove("animate");
          }
        });
      }, observerOptions);
  
      this.$refs.contactSection
        .querySelectorAll(".map-container, .coordinator-container")
        .forEach((element) => observer.observe(element));
    },
    methods: {
      animateMap() {
        const mapElement = this.$refs.map.querySelector("iframe");
        mapElement.style.transform = "scale(0.5)";
        setTimeout(() => {
          mapElement.style.transition = "transform 1s ease-in-out";
          mapElement.style.transform = "scale(1)";
        }, 100);
      },
    },
  };
  </script>
  
  <style scoped>
  .contact-container {
    text-align: center;
    margin: 50px auto;
    max-width: 100%;
    padding: 20px;
    overflow-x: hidden;
  }
  
  .contact-heading {
    font-family: "Montserrat", sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #333;
    margin-bottom: 10px;
  }
  
  .contact-description {
    font-family: "Montserrat", sans-serif;
    max-width: 80%;
    font-size: 1rem;
    line-height: 1.5;
    color: #555;
    margin: 0 auto 20px;
  }
  
  .contact-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    gap: 20px;
  }
  
  .map-container {
    flex: 1;
    min-width: 280px;
    max-width: 600px;
    transform: scale(0);
    opacity: 0;
  }
  
  .coordinator-container {
    flex: 1;
    min-width: 280px;
    max-width: 600px;
    background-color: #f9f9f9;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transform: translateY(50px);
    opacity: 0;
  }
  
  /* Animation Trigger */
  .map-container.animate,
  .coordinator-container.animate {
    opacity: 1;
    transform: scale(1) translateY(0);
    transition: all 1s ease;
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .contact-description {
      font-size: 0.9rem;
    }
  
    .contact-heading {
      font-size: 1.5rem;
    }
  
    .contact-content {
      gap: 15px;
    }
  }
  
  @media (max-width: 480px) {
    .contact-description {
      font-size: 0.8rem;
    }
  
    .contact-heading {
      font-size: 1.25rem;
    }
  
    .coordinator-container {
      padding: 15px;
    }
  }
  </style>
  