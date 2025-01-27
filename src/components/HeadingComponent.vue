<template>
    <section id="projects">
      <div class="text-container">
        <h1>
          Explore the <span class="yellow-text">Themes!</span>
        </h1>
        <div class="para-container">
          <p>
            Explore the Themes of our hackathons, where innovation meets real-world challenges. Each theme reflects a unique domain in technology, offering opportunities to apply cutting-edge solutions to pressing problems. From AI and machine learning to sustainability and cybersecurity, these themes inspire creativity and push the boundaries of what's possible. Join us as we explore how diverse ideas and technical expertise can create impactful change across various fields.        </p>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "HeadingComponent",
    mounted() {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("animate");
            } else {
              entry.target.classList.remove("animate"); // Reset animation for re-entry
            }
          });
        },
        { threshold: 0.3 }
      );
  
      observer.observe(this.$el.querySelector(".text-container"));
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&display=swap');
  
  /* Styling */
  .text-container {
    font-family: "Montserrat", sans-serif;
    max-width: 83%;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  
    /* Starting state for animation */
    opacity: 0;
    transform: scale(0.8) rotateX(-15deg) translateY(30px);
    transition: opacity 1.2s ease, transform 1.2s cubic-bezier(0.23, 1, 0.32, 1);
  }
  
  .text-container.animate {
    /* Final state for animation */
    opacity: 1;
    transform: scale(1) rotateX(0deg) translateY(0);
  }
  
  .text-container h1 {
    font-size: 2.5rem;
    font-weight: 800;
    color: #333;
    margin-bottom: 20px;
    line-height: 1.3;
  }
  
  .yellow-text {
    color: #f9d342;
  }
  
  .para-container p {
    font-size: 1rem;
    line-height: 1.75;
    color: black;
  }
  
  /* Responsiveness */
  @media (max-width: 768px) {
    .text-container {
      max-width: 90%;
      padding: 15px;
    }
  
    .text-container h1 {
      font-size: 2rem;
      text-align: center;
    }
  
    .para-container p {
      font-size: 0.9rem;
      line-height: 1.6;
      text-align: justify;
    }
  }
  
  @media (max-width: 480px) {
    .text-container h1 {
      font-size: 1.5rem;
    }
  
    .para-container p {
      font-size: 0.85rem;
      line-height: 1.5;
    }
  }
  </style>
  