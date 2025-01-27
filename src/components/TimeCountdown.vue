<template>
    <div class="landing-page" ref="observerTarget">
      <transition name="fade-in" appear>
        <div v-if="isVisible" class="countdown">
          <h2 class="greeting">COUNTDOWN</h2>
          <p class="title">Countdown Until the Event. Register Now</p>
          <div class="countdown-timer">
            <div v-for="(time, unit) in timeUnits" :key="unit" class="time-box">
              <div class="time-value">{{ time }}</div>
              <div class="time-label">{{ unit }}</div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </template>
  
  <script>
  export default {
    name: "TimeCountdown",
    data() {
      return {
        targetDate: new Date("2025-02-15T23:59:59"), // Event date
        timeUnits: {
          Days: 0,
          Hours: 0,
          Minutes: 0,
          Seconds: 0,
        },
        isVisible: false,
      };
    },
    mounted() {
      this.setupObserver();
      this.calculateTime();
      setInterval(this.calculateTime, 1000);
    },
    methods: {
      calculateTime() {
        const now = new Date();
        const difference = this.targetDate - now;
  
        if (difference > 0) {
          this.timeUnits.Days = Math.floor(difference / (1000 * 60 * 60 * 24));
          this.timeUnits.Hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
          this.timeUnits.Minutes = Math.floor((difference / 1000 / 60) % 60);
          this.timeUnits.Seconds = Math.floor((difference / 1000) % 60);
        } else {
          this.timeUnits = {
            Days: 0,
            Hours: 0,
            Minutes: 0,
            Seconds: 0,
          };
        }
      },
      setupObserver() {
        const observer = new IntersectionObserver(
          ([entry]) => {
            if (entry.isIntersecting) {
              this.isVisible = true;
            } else {
              this.isVisible = false;
            }
          },
          { threshold: 0.3 }
        );
        observer.observe(this.$refs.observerTarget);
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@400;600;700&display=swap');
  
  /* General Styles */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  
  
  .landing-page {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
    padding: 20px;
    overflow: hidden;
  }
  
  /* Countdown Styles */
  .greeting,
  .title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #333333;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }
  
  .countdown-timer {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap; /* Enables wrapping on small screens */
  }
  
  .time-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #ffffff;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    padding: 20px;
    border-radius: 20px;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    transform: translateY(30px);
    opacity: 0;
    animation: slideUp 0.8s forwards;
    animation-delay: var(--delay, 0s);
    flex-basis: 100px; /* Minimum width for boxes */
    flex-grow: 1;
    max-width: 120px;
  }
  
  .time-box:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  
  .time-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: #0984e3;
    margin-bottom: 10px;
  }
  
  .time-label {
    font-size: 1.2rem;
    color: #636e72;
  }
  
  /* Staggered Animation */
  .time-box:nth-child(1) {
    --delay: 0.2s;
  }
  .time-box:nth-child(2) {
    --delay: 0.4s;
  }
  .time-box:nth-child(3) {
    --delay: 0.6s;
  }
  .time-box:nth-child(4) {
    --delay: 0.8s;
  }
  
  /* Animation Styles */
  @keyframes slideUp {
    0% {
      transform: translateY(30px);
      opacity: 0;
    }
    100% {
      transform: translateY(0);
      opacity: 1;
    }
  }
  
  .fade-in-enter-active,
  .fade-in-leave-active {
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  .fade-in-enter-from,
  .fade-in-leave-to {
    opacity: 0;
    transform: translateY(20px);
  }
  
  /* Responsive Styles */
  @media screen and (max-width: 768px) {
    .countdown-timer {
      gap: 10px;
    }
  
    .time-box {
      flex-basis: 80px;
      max-width: 100px;
      padding: 15px;
    }
  
    .time-value {
      font-size: 1.8rem;
    }
  
    .time-label {
      font-size: 1rem;
    }
  
    .greeting,
    .title {
      font-size: 1.8rem;
    }
  }
  </style>
  