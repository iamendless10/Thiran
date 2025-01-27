<template>
    <section id="project">
      <div class="full-image-container">
        <!-- First Image Container -->
        <div class="image-container">
          <img :src="mainImage.src" :alt="mainImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Artificial Intelligence</h2>
            </div>
          </div>
        </div>
  
        <!-- Second Image Container -->
        <div class="image-container">
          <img :src="secondImage.src" :alt="secondImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Internet of Things</h2>
            </div>
          </div>
        </div>
  
        <!-- Third Image Container -->
        <div class="image-container">
          <img :src="thirdImage.src" :alt="thirdImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Health-Tech</h2>
            </div>
          </div>
        </div>
  
        <!-- Fourth Image Container -->
        <div class="image-container">
          <img :src="fourthImage.src" :alt="fourthImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Agri-Tech</h2>
            </div>
          </div>
        </div>
  
        <!-- Fifth Image Container -->
        <div class="image-container">
          <img :src="fifthImage.src" :alt="fifthImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Sustainability</h2>
            </div>
          </div>
        </div>
  
        <!-- Sixth Image Container -->
        <div class="image-container">
          <img :src="sixthImage.src" :alt="sixthImage.alt" class="blur-image" />
          <div class="overlay">
            <div class="content">
              <h2 class="heading">Open Innovation</h2>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "ProjectsComponent",
    data() {
      return {
        mainImage: {
          src: require("../assets/ai.jpg"),
          alt: "Artificial Intelligence Image"
        },
        secondImage: {
          src: require("../assets/iot.jpg"),
          alt: "Internet of Things Image"
        },
        thirdImage: {
          src: require("../assets/health.jpg"),
          alt: "Health-Tech Image"
        },
        fourthImage: {
          src: require("../assets/agri.jpg"),
          alt: "Agri-Tech Image"
        },
        fifthImage: {
          src: require("../assets/sus.jpg"),
          alt: "Sustainability Image"
        },
        sixthImage: {
          src: require("../assets/bulb.jpg"),
          alt: "Open Innovation Image"
        }
      };
    }
  };
  </script>
  
  <style scoped>
  /* Full Image Container */
  .full-image-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 20px;
    margin: 0 auto;
    padding: 20px;
  }
  
  /* Image container */
  .image-container {
    position: relative;
    flex: 1 1 calc(33.333% - 20px);
    max-width: calc(33.333% - 20px);
    height: 200px;
    border-radius: 15px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  /* Hover effect */
  .image-container:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  }
  
  /* Overlay */
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 1;
    transition: opacity 0.3s ease;
  }
  
  /* Show overlay on hover */
  .image-container:hover .overlay {
    opacity: 1;
  }
  
  /* Blur effect on images */
  .blur-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: blur(2px);
    transition: filter 0.3s ease;
  }
  
  /* Remove blur effect on hover */
  .image-container:hover .blur-image {
    filter: blur(0);
  }
  
  /* Content inside overlay */
  .content {
    text-align: center;
    color: white;
  }
  
  /* Heading styles */
  .heading {
    font-family: "Montserrat", sans-serif;
    font-size: 25px;
    font-weight: 700;
    color: #fff;
  }
  
  /* Media Queries */
  @media (max-width: 1024px) {
    .image-container {
      flex: 1 1 calc(33.333% - 20px);
      max-width: calc(33.333% - 20px);
      height: 180px;
    }
  }
  
  @media (max-width: 768px) {
    .image-container {
      flex: 1 1 calc(50% - 20px);
      max-width: calc(50% - 20px);
      height: 160px;
    }
  }
  
  @media (max-width: 480px) {
    .image-container {
      flex: 1 1 calc(100% - 20px);
      max-width: calc(100% - 20px);
      height: 150px;
    }
  }
  </style>
  