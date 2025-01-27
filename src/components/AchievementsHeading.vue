<template>
    <div class="text-container">
      <h1>Prize Pool Worth of <span class="highlight">₹45,000</span></h1>
      <div class="para-container">
        <p>
  
          Our hackathon offers an exciting prize pool, recognizing innovative AI and ML solutions. Compete for amazing rewards while making a real impact!      </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AchievementsHeading",
  };
  </script>
  
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&display=swap");
  
  .text-container {
    font-family: "Montserrat", sans-serif;
    max-width: 83%;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    animation: fadeIn 1.5s ease-in-out;
    transition: transform 0.3s;
  }
  
  .text-container:hover {
    transform: scale(1.02);
  }
  
  .text-container h1 {
    font-size: 3vw; /* Responsive font size */
    font-weight: 800;
    color: #333;
    margin-bottom: 20px;
    line-height: 1.3;
    text-align: center;
    animation: slideInFromTop 1s ease-out;
  }
  
  .highlight {
    color: #f9d342;
  }
  
  .para-container p {
    max-width: 90%;
    font-size: 1.2rem;
    line-height: 1.8;
    color: #333;
    text-align: center;
    margin: 0 auto;
    animation: fadeIn 2s ease-in;
  }
  
  /* Media queries for responsiveness */
  @media (max-width: 1024px) {
    .text-container h1 {
      font-size: 5vw;
    }
  
    .para-container p {
      font-size: 1rem;
    }
  }
  
  @media (max-width: 768px) {
    .text-container {
      padding: 15px;
    }
  
    .text-container h1 {
      font-size: 6vw;
    }
  
    .para-container p {
      font-size: 0.9rem;
    }
  }
  
  @media (max-width: 480px) {
    .text-container {
      padding: 10px;
    }
  
    .text-container h1 {
      font-size: 7vw;
    }
  
    .para-container p {
      font-size: 0.8rem;
      line-height: 1.5;
    }
  }
  
  /* Animations */
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  
  @keyframes slideInFromTop {
    from {
      transform: translateY(-50px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  </style>
  