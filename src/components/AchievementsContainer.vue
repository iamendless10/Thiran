<template>
    <div class="containers-section" ref="containerSection">
      <h1 class="section-heading">Achievements</h1>
      <div class="containers-grid">
        <div
          class="container-card animate__animated"
          v-for="(item, index) in items"
          :key="index"
          :class="getGradientClass(item.amount)"
          :ref="(el) => (cardsRefs[index] = el)"
        >
          <div class="card-header">
            <img :src="item.icon" alt="icon" class="icon" />
            <h2 class="card-title">
              {{ item.title }}
              <span class="amount">{{ item.amount }}</span>
            </h2>
            <h3 class="subheading">{{ item.subheading }}</h3>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AchievementsContainer",
    data() {
      return {
        items: [
          {
            icon: require("../assets/trophy.png"),
            title: "Winner",
            amount: "₹20,000",
            subheading: "Crowned for excellence – where innovation meets reward!",
          },
          {
            icon: require("../assets/trophy.png"),
            title: "1st Runner Up",
            amount: "₹15,000",
            subheading: "A leap towards greatness – recognizing extraordinary achievement!",
          },
          {
            icon: require("../assets/wreath.png"),
            title: "2nd Runner Up",
            amount: "₹10,000",
            subheading: "Celebrating brilliance – innovation that stands out!",
          },
          {
            icon: require("../assets/conference.png"),
            title: "Best Innovator Award",
            amount: "",
            subheading: "For the visionary who changes the game!",
          },
        ],
        cardsRefs: [],
      };
    },
    mounted() {
      this.addScrollAnimations();
    },
    methods: {
      getGradientClass(amount) {
        if (amount.includes("₹20,000")) {
          return "gradient-winner";
        } else if (amount.includes("₹15,000")) {
          return "gradient-runner-up";
        } else if (amount.includes("₹10,000")) {
          return "gradient-third";
        }
        return "gradient-default";
      },
      addScrollAnimations() {
        this.$nextTick(() => {
          const observer = new IntersectionObserver(
            (entries) => {
              entries.forEach((entry) => {
                if (entry.isIntersecting) {
                  entry.target.classList.add("animate__fadeInUp");
                  entry.target.style.opacity = 1;
                } else {
                  entry.target.classList.remove("animate__fadeInUp");
                  entry.target.style.opacity = 0;
                }
              });
            },
            { threshold: 0.3 }
          );
  
          this.cardsRefs.forEach((card) => {
            if (card) {
              card.style.opacity = 0;
              observer.observe(card);
            }
          });
        });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Containers Section */
  .containers-section {
    text-align: center;
    max-width: 93%;
    margin: 0 auto;
  }
  
  /* Section Heading */
  .section-heading {
    font-family: "Montserrat", sans-serif;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #fff;
  }
  
  /* Containers Grid */
  .containers-grid {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 100px;
  }
  
  /* Container Card Styles */
  .container-card {
    color: black;
    width: 250px;
    height: 250px;
    padding: 20px;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    opacity: 0;
  }
  
  /* Hover effect for card */
  .container-card:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7);
  }
  
  /* Gradients for all cards */
  .gradient-winner {
    background: linear-gradient(135deg, #fff5e5, #ffe4b3); /* Soft gold-inspired gradient */
  }
  
  .gradient-runner-up {
    background: linear-gradient(135deg, #f2f2f2, #e0e0e0); /* Subtle silver/white gradient */
  }
  
  .gradient-third {
    background: linear-gradient(135deg, #f4e0d6, #e6ccb2); /* Warm bronze-inspired gradient */
  }
  
  .gradient-default {
    background: linear-gradient(135deg, #f7f7f7, #ececec); /* Neutral light grey gradient */
  }
  
  /* Card Header */
  .card-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  
  /* Icon Styles */
  .icon {
    width: 60px;
    height: 60px;
    margin-bottom: 10px;
  }
  
  /* Card Title Styles */
  .card-title {
    font-family: "Montserrat", sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: black;
    margin-bottom: 10px;
  }
  
  /* Amount Styles (for the new line) */
  .amount {
    display: block;
    font-size: 24px;
    font-weight: 800;
    color: #333;
    margin-top: 5px;
  }
  
  /* Subheading Styles */
  .subheading {
    font-family: "Montserrat", sans-serif;
    font-size: 16px;
    font-weight: 500;
    color: #444444;
  }
  
  /* Entry Animation Classes */
  .animate__fadeInUp {
    animation: fadeInUp 1s ease-in-out;
  }
  
  @keyframes fadeInUp {
    from {
      transform: translateY(20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  </style>
  