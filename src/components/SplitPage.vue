<template>
    <div class="split-page">
      <!-- Left Side -->
      <div class="left-side">
        <transition name="fade-in" appear>
          <div class="content" v-if="isVisible">
            <!-- Heading with Bounce Animation -->
            <h1 class="heading">
              About <span class="highlight">AI</span> - <span class="highlight">Innovate!</span>
            </h1>
  
            <!-- Description with Fade and Scale Animation -->
            <p class="description" style="text-align: justify; padding: 0 -50px;">
              AI Innovate, hosted by the Department of (AIML) and (AIDS), is a thrilling hackathon designed to spark creativity and drive innovation in AI. This vibrant event unites bright minds to solve real-world challenges, develop groundbreaking solutions, and demonstrate the transformative potential of AI. Be part of this journey to learn, create, and shape the future of technology!          </p>
  
            <!-- Social Media Icons with Rotating Hover Effect -->
            <div class="social-icons">
              <a href="https://www.linkedin.com/school/srieshwar/posts/?feedView=all" target="_blank">
                <img src="@/assets/linkedin.png" alt="LinkedIn" class="icon" />
              </a>
              <!-- <a href="https://www.github.com/iamendless10" target="_blank">
                <img src="@/assets/github.png" alt="GitHub" class="icon" />
              </a>
              <a href="https://twitter.com/kayalennian" target="_blank">
                <img src="@/assets/twitter.png" alt="Twitter" class="icon" />
              </a> -->
              <a href="https://www.instagram.com/srieshwar_thiran" target="_blank">
                <img src="@/assets/instagram.png" alt="Instagram" class="icon" />
              </a>
            </div>
  
            <!-- Glowing and Hover Animated Get Connect Button -->
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdcgkB0mtHS3PEorSgL2U0_K7PJ7Ot03n8NX9WVAl6VlsATFA/viewform">
              <button class="connect-btn">
                Register Now!
                <span class="btn-icon">✨</span>
              </button>
            </a>
          </div>
        </transition>
      </div>
  
      <!-- Right Side -->
      <div class="right-side">
        <transition name="slide" appear>
          <img
            v-if="isVisible"
            src="../assets/image-5.png"
            alt="Placeholder Image"
            class="right-image hover-glow"
          />
        </transition>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SplitPage",
    data() {
      return {
        isVisible: false,
      };
    },
    mounted() {
      this.setUpScrollAnimation();
    },
    methods: {
      setUpScrollAnimation() {
        const observer = new IntersectionObserver(
          ([entry]) => {
            this.isVisible = entry.isIntersecting;
          },
          { threshold: 0.5 }
        );
  
        const element = this.$el;
        observer.observe(element);
      },
    },
  };
  </script>
  
  <style scoped>
  /* Container to split the page */
  .split-page {
    display: flex;
    width: 100%;
    height: 100vh;
    margin-top: 2%;
    overflow: hidden;
  }
  
  /* Left side styling */
  .left-side {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }
  
  /* Content inside the left side */
  .content {
    max-width: 600px;
    text-align: left;
  }
  
  /* Heading styling */
  .heading {
    font-family: "Montserrat", sans-serif;
    font-size: 36px;
    font-weight: 800;
    color: #333;
    margin-bottom: 20px;
    line-height: 1.3;
    animation: bounceIn 1s ease;
  }
  
  /* Highlighted text */
  .highlight {
    color: #f9d342;
  }
  
  /* Description animation */
  .description {
    font-family: "Montserrat", sans-serif;
    font-size: 16px;
    font-weight: 400;
    color: #555;
    margin-bottom: 30px;
    word-spacing: 4px;
    animation: fadeInScale 1.2s ease;
  }
  
  /* Social media icons */
  .social-icons {
    display: flex;
    justify-content: flex-start;
    gap: 20px;
    margin-bottom: 30px;
  }
  
  /* Icon animation */
  .social-icons a img {
    width: 30px;
    height: 30px;
  }
  
  .social-icons a:hover {
    transform: rotate(15deg);
    transition: transform 0.3s ease, color 0.3s ease;
  }
  
  /* Button glow effect */
  .connect-btn {
    background-color: #000;
    color: #fff;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-family: "Montserrat", sans-serif;
    font-weight: 600;
    border-radius: 30px;
    cursor: pointer;
    box-shadow: 0 0 10px #f9d342, 0 0 20px #f9d342;
    animation: glowPulse 2s infinite;
    position: relative;
  }
  
  .connect-btn:hover {
    background-color: #333;
    transform: scale(1.05);
  }
  
  .connect-btn .btn-icon {
    position: absolute;
    right: -15px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 18px;
    animation: sparkle 1.5s infinite;
  }
  
  /* Right side styling */
  .right-side {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }
  
  /* Image hover effect */
  .right-image {
    width: 100%;
    max-width: 600px;
    height: auto;
    border-radius: 10px;
    animation: float 3s infinite ease-in-out;
  }
  
  .hover-glow {
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    transition: box-shadow 0.3s ease;
  }
  
  .hover-glow:hover {
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.6);
  }
  
  /* Keyframe Animations */
  @keyframes bounceIn {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-30px);
    }
    60% {
      transform: translateY(-15px);
    }
  }
  
  @keyframes fadeInScale {
    0% {
      opacity: 0;
      transform: scale(0.9);
    }
    100% {
      opacity: 1;
      transform: scale(1);
    }
  }
  
  @keyframes glowPulse {
    0% {
      box-shadow: 0 0 10px #f9d342;
    }
    50% {
      box-shadow: 0 0 20px #f9d342;
    }
    100% {
      box-shadow: 0 0 10px #f9d342;
    }
  }
  
  @keyframes float {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-15px);
    }
    100% {
      transform: translateY(0);
    }
  }
  
  @keyframes sparkle {
    0%, 100% {
      transform: scale(1);
      opacity: 1;
    }
    50% {
      transform: scale(1.3);
      opacity: 0.6;
    }
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .split-page {
      flex-direction: column;
    }
    .content {
      max-width: 90%;
      text-align: center;
    }
    .heading {
      font-size: 1.5rem;
    }
    .description {
      font-size: 0.9rem;
    }
    .social-icons {
      justify-content: center;
    }
    .right-image {
      max-width: 90%;
      height: auto;
    }
  }
  
  @media (max-width: 480px) {
    .heading {
      font-size: 1.2rem;
    }
    .description {
      font-size: 0.8rem;
    }
    .connect-btn {
      padding: 8px 16px;
      font-size: 0.9rem;
    }
    .social-icons a img {
      width: 20px;
      height: 20px;
    }
  }
  </style>
  