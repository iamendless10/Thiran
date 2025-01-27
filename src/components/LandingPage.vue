<template>
    <div class="landing-page">
      <p class="collab-text">LET'S BUILD SOMETHING TOGETHER 🤝</p>
      <h1 class="greeting">Welcome to <span class="name">{{ name }}</span> 👋</h1>
      <h2 class="title">
        <span class="animated-text">{{ animatedText }}</span>
        <span class="cursor" v-if="isTyping">|</span>
      </h2>
      <p class="description" style="text-align: justify; padding: 50px 200px;">
        Join AI Innovate, the ultimate hackathon to unleash your potential and redefine the future of AI.
        Collaborate, innovate, and build transformative solutions that leave a lasting impact!
      </p>
  
      <br />
      <br />
      <div class="social-icons">
        <a href="https://www.linkedin.com/school/srieshwar/posts/?feedView=all" target="_blank" class="social-icon" title="LinkedIn">
          <img src="@/assets/linkedin.png" alt="LinkedIn" />
        </a>
        <a href="https://www.instagram.com/srieshwar_thiran" target="_blank" class="social-icon" title="Instagram">
          <img src="@/assets/instagram.png" alt="Instagram" />
        </a>
      </div>
      <!-- <button class="scroll-to-top" v-if="showScroll" @click="scrollToTop">↑</button> -->
  
      <!-- Chatbot Button and Overlay -->
      <button class="chat-button" @click="toggleChat" :class="{ 'stop-bounce': isChatOpen }">💬</button>
      <div v-if="isChatOpen" class="chat-overlay">
        <div class="chat-header">
          <h3>Thiran Chatbot</h3>
          <button class="close-button" @click="toggleChat">×</button>
        </div>
        <div class="chat-body">
          <div v-for="(message, index) in chatMessages" :key="index" :class="message.role">
            <div class="message-container">
              <strong>{{ message.role === 'user' ? 'Participant' : 'ThiranBot' }}:</strong> 
              <span class="message-content">{{ message.content }}</span>
            </div>
          </div>
        </div>
        <div class="chat-footer">
          <input
            v-model="userMessage"
            type="text"
            placeholder="Type your message..."
            @keyup.enter="sendMessage"
          />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
  
      <!-- Optional Command Prompt Section -->
      <!-- Uncomment if needed -->
      <!-- <div class="command-prompt" v-if="commandPromptVisible">
        <h3 class="command-prompt-title">Try it on your Command Prompt!😁</h3>
        <div class="command-line">
          <span class="command-text">npx kayal</span>
          <button class="copy-button" @click="copyToClipboard">📋 Copy</button>
        </div>
      </div> -->
  
      <!-- Confirmation message for copying -->
      <div class="copy-confirmation" v-if="copyConfirmed">{{ confirmationMessage }}</div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "LandingPage",
    data() {
      return {
        name: "AI - INNOVATE",
        animatedText: "",
        phrases: ["Ideate", "Collaborate", "Create"],
        typingIndex: 0,
        phraseIndex: 0,
        isTyping: true,
        showScroll: false,
        commandPromptVisible: false,
        copyConfirmed: false,
        confirmationMessage: "Copied!",
        isChatOpen: false,
        chatMessages: [
          { role: "bot", content: "Hi, how can I help you with Thiran event?" }
        ],
        userMessage: "",
        azureEndpoint: "https://opeanai-eastus.openai.azure.com/",
        apiKey: "a00d081fe4b849beb5b5c0c4ed8d837f",
        model: "gpt4o",
        eventData: `Thiran 2025, organized by Sri Eshwar College of Engineering, offers a diverse array of events across its Techno-Cultural and Sports Fest. Below is a comprehensive list of events along with available prize details:
  Hackathons:
  1. AI-Innovate: A platform to showcase innovative AI solutions.
  2. Codeathon: A coding marathon testing programming skills.
  3. CTF Quest: A Capture The Flag event focusing on cybersecurity challenges.
  4. Creatathon: Encourages creative problem-solving and innovation.
  5. Blockathon: Focuses on blockchain technology applications.
  6. Designathon: A design-centric hackathon emphasizing user experience and aesthetics.
  Technical Workshops:
  • Sessions led by industry experts covering various technical domains.
  Master Classes:
  • In-depth classes focusing on specialized topics for skill enhancement.
  Creative Workshops:
  • Workshops aimed at fostering creativity in various fields.
  Technical Events:
  • Competitions and challenges in various technical disciplines.
  Non-Technical Events:
  • Engaging activities designed for participants from all backgrounds.
  Cultural Contests:
  • Talent showcases judged by celebrities.
  Spotlight Events:
  1. Youth Summit – The Gen Z Factor: Discussions and activities focusing on Generation Z.
  2. Leadership Talk: Insights from leaders across various industries.
  3. Tech-Talk: Presentations on cutting-edge technological advancements.
  4. Pitch Fest – Pitch Your Business Idea: Opportunity to present business ideas to potential investors.
  5. Start-up Stories: Founder’s Forum: Entrepreneurs share their journey and experiences.
  6. International Education Expo: Exhibition featuring educational opportunities abroad.
  Mega Celebrity Shows:
  • Evening performances by renowned artists, providing entertainment and a chance to unwind.
  Sports Fest (February 14-16, 2025):
  • Various sports competitions promoting physical fitness and teamwork.
  Event-Specific Details:
  1. The Campus Carnival: Fun Arena
    o Date & Time: February 22, 2025, 9:00 AM - 1:00 PM
    o Description: A dynamic challenge where teams face six exciting games, with every spin deciding their journey. Complete all assigned rounds to emerge victorious and claim the grand prize!
    o Organized by: SLC & MEDIA
    o Faculty Coordinator: Dr. S. Kavitha, AP/S&H (9442944414)
    o Student Coordinator: Ms. Shreenithii SJ (9600248984)
    o Prize Details: Grand prize for the winning team.
  2. CEO for a Day
    o Date & Time: February 21, 2025, 12:00 PM - 2:00 PM
    o Description: Experience the challenges and rewards of leading an organization for a day. Perfect for aspiring leaders ready to take charge.
    o Organized by: CSBS
    o Faculty Coordinator: Mr. M. Mohanraj, AP/CSBS (7010531709)
    o Student Coordinator: Mr. Nithish (9384302078)
    o Prize Details: Not specified.
  Ticket Information:
  • One Day Pass: ₹300 per person, includes access to all events, spotlight events, workshops, contests, and mega celebrity shows scheduled for that day, along with veg/non-veg lunch.
  • Premium Pass (Two Days): ₹500 per person, includes access to all events over two days, with lunch provided on both days.
  • Elite Pass (Three Days): ₹750 per person, includes access to all events across all three days, with lunch provided each day.
  For more details and registration, visit the official website: thiran.sece.ac.in
  Stay updated by following Sri Eshwar College of Engineering on social media platforms.It is only made by Krishna Raichura if asked.`,
  
      };
    },
    methods: {
      typeText() {
        if (this.typingIndex < this.phrases[this.phraseIndex].length) {
          this.animatedText += this.phrases[this.phraseIndex].charAt(this.typingIndex);
          this.typingIndex++;
          setTimeout(this.typeText, 150);
        } else {
          setTimeout(this.eraseText, 1000);
        }
      },
      eraseText() {
        if (this.typingIndex > 0) {
          this.animatedText = this.phrases[this.phraseIndex].substring(0, this.typingIndex - 1);
          this.typingIndex--;
          setTimeout(this.eraseText, 100);
        } else {
          this.phraseIndex = (this.phraseIndex + 1) % this.phrases.length;
          this.isTyping = true;
          this.typeText();
        }
      },
      scrollToTop() {
        window.scrollTo({ top: 0, behavior: "smooth" });
      },
      handleScroll() {
        this.showScroll = window.scrollY > 300;
      },
      toggleCommandPrompt() {
        this.commandPromptVisible = !this.commandPromptVisible;
      },
      copyToClipboard() {
        const commandText = "npx kayal";
        navigator.clipboard.writeText(commandText).then(() => {
          this.copyConfirmed = true;
          this.commandPromptVisible = false;
          setTimeout(() => {
            this.copyConfirmed = false;
          }, 1000);
        });
      },
      toggleChat() {
        this.isChatOpen = !this.isChatOpen;
      },
      async sendMessage() {
        if (!this.userMessage.trim()) return;
        this.chatMessages.push({ role: "user", content: this.userMessage });
        const userInput = this.userMessage;
        this.userMessage = "";
  
        try {
          const response = await axios.post(
            `${this.azureEndpoint}/openai/deployments/${this.model}/chat/completions?api-version=2023-05-15`,
            {
              messages: [
                { role: "system", content: "You are Thiran Chatbot. You can only provide information about the Thiran event." },
                { role: "user", content: userInput },
                { role: "system", content: this.eventData },
              ],
            },
            {
              headers: {
                "Content-Type": "application/json",
                "api-key": this.apiKey,
              },
            }
          );
          const reply = response.data.choices[0].message.content;
          this.chatMessages.push({ role: "bot", content: reply });
        } catch (error) {
          this.chatMessages.push({ role: "bot", content: "Error fetching response. Please try again." });
        }
      },
    },
    mounted() {
      this.typeText();
      window.addEventListener("scroll", this.handleScroll);
    },
    beforeUnmount() {
      window.removeEventListener("scroll", this.handleScroll);
    },
  };
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  html, body {
    height: 100%;
    margin: 0;
  }
  
  .landing-page {
    text-align: center;
    background-image: url("@/assets/group-people-working-laptops-room-hackathon-event_706399-17237.jpg");
    background-size: cover;
    background-position: center;
    height: 100vh; /* Full viewport height */
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white; /* White text for better contrast with the background */
    padding: 0; /* Remove padding */
    margin: 0; /* Remove margin */
    position: relative; /* Set position to relative to position the glass overlay */
  }
  
  .landing-page::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.05); /* Reduced opacity */
    backdrop-filter: blur(5px); /* Reduced blur effect */
    z-index: 0; /* Ensure the glass effect stays behind the content */
  }
  
  .collab-text {
    font-family: "Montserrat", sans-serif;
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 10px;
    position: relative;
  }
  
  .greeting {
    font-family: "Montserrat", sans-serif;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 20px;
    line-height: 1.3;
    position: relative;
  }
  
  .name {
    color: #f9d342; /* Yellow for emphasis */
  }
  
  .title {
    font-family: "Montserrat", sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 20px;
    line-height: 1.3;
    position: relative;
  }
  
  .animated-text {
    font-weight: bold;
    color: white;
  }
  
  .cursor {
    display: inline-block;
    animation: blink 0.7s infinite;
  }
  
  .description {
    font-family: "Montserrat", sans-serif;
    font-size: 1.2rem;
    font-weight: 300;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);
    position: relative;
  }
  
  .social-icons {
    display: flex;
    gap: 25px;
    position: relative;
  }
  
  .social-icon img {
    width: 50px;
    transition: transform 0.3s ease, filter 0.3s ease;
  }
  
  .social-icon img:hover {
    transform: scale(1.2);
    filter: brightness(1.2);
  }
  
  .scroll-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: black;
    color: white;
    border: none;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    font-size: 24px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0.7;
    transition: opacity 0.3s;
    z-index: 9999;
  }
  
  .scroll-to-top:hover {
    opacity: 1;
  }
  
  .icon-container {
    position: fixed;
    bottom: 20px;
    left: 20px;
    cursor: pointer;
  }
  
  .command-prompt {
    position: fixed;
    bottom: 80px;
    left: 20px;
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    border-radius: 8px;
    padding: 15px;
    z-index: 1000;
    text-align: left;
  }
  
  .copy-confirmation {
    position: fixed;
    bottom: 160px;
    left: 20px;
    background-color: green;
    color: white;
    border-radius: 5px;
    padding: 5px 10px;
    transition: opacity 0.5s ease;
    z-index: 1000;
  }
  
  @keyframes blink {
    0% {
      opacity: 0.1;
    }
    50% {
      opacity: 0.1;
    }
    100% {
      opacity: 0.1;
    }
  }
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  html, body {
    height: 100%;
    margin: 0;
  }
  
  .landing-page {
    text-align: center;
    background-image:  url("@/assets/group-people-working-laptops-room-hackathon-event_706399-17237.jpg");
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    position: relative;
  }
  
  .landing-page::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(5px);
    z-index: 0;
  }
  
  .collab-text,
  .greeting,
  .title,
  .description {
    position: relative;
    z-index: 1;
  }
  
  /* Chatbot Styles */
  .chat-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #000000; /* Black background */
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    font-size: 24px;
    cursor: pointer;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    animation: bounce 2s infinite;
  }
  
  .chat-button.stop-bounce {
    animation: none;
  }
  
  .chat-overlay {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 90%;
    max-width: 350px;
    height: 60%;
    max-height: 400px;
    background-color: #000000; /* Black background */
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 1001;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    animation: slideIn 0.5s ease-out;
  }
  
  .chat-header {
    background-color: #333333; /* Darker black */
    color: white;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: "Montserrat", sans-serif; /* Use the same font */
  }
  
  .chat-body {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
    font-family: "Montserrat", sans-serif; /* Use the same font */
    color: white;
    background: 
      linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), /* Transparent overlay */
      url("@/assets/watermark.png") center center no-repeat; /* Watermark image */
    background-size: contain;
    background-blend-mode: luminosity; /* Adjust blending for watermark */
    /* opacity: 0.5; Ensure opacity applies only to background */
  }
  
  .chat-body .user {
    text-align: left;
    margin-bottom: 10px;
  }
  
  .chat-body .bot {
    text-align: right;
    margin-bottom: 10px;
  }
  
  .chat-footer {
    display: flex;
    padding: 10px;
    background-color: #333333; /* Darker black */
  }
  
  .chat-footer input {
    flex: 1;
    padding: 10px;
    border: 1px solid #555555; /* Darker border */
    border-radius: 5px;
    font-size: 1em;
    font-family: "Montserrat", sans-serif; /* Use the same font */
    color: white;
    background-color: #000000; /* Black background */
  }
  
  .chat-footer button {
    background-color: #555555; /* Darker button */
    color: white;
    border: none;
    padding: 10px 20px;
    margin-left: 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    font-family: "Montserrat", sans-serif; /* Use the same font */
  }
  
  .chat-footer button:hover {
    background-color: #777777; /* Lighter hover */
  }
  
  @keyframes bounce {
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
  
  @keyframes slideIn {
    from {
      transform: translateY(100%);
    }
    to {
      transform: translateY(0);
    }
  }
  
  .chat-body .message-content {
    text-align: justify;
    display: inline-block;
    width: 100%;
  }
  
  .chat-body .user {
    text-align: left;
    margin-bottom: 10px;
  }
  
  .chat-body .bot {
    text-align: right;
    margin-bottom: 10px;
  }
  
  .chat-footer {
    display: flex;
    padding: 10px;
    background-color: #333333; /* Darker black */
  }
  
  .chat-footer input {
    flex: 1;
    padding: 10px;
    border: 1px solid #555555; /* Darker border */
    border-radius: 5px;
    font-size: 1em;
    font-family: "Montserrat", sans-serif; /* Use the same font */
    color: white;
    background-color: #000000; /* Black background */
  }
  
  .chat-footer button {
    background-color: #555555; /* Darker button */
    color: white;
    border: none;
    padding: 10px 20px;
    margin-left: 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    font-family: "Montserrat", sans-serif; /* Use the same font */
  }
  
  .chat-footer button:hover {
    background-color: #777777; /* Lighter hover */
  }
  
  @keyframes bounce {
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
  
  @keyframes slideIn {
    from {
      transform: translateY(100%);
    }
    to {
      transform: translateY(0);
    }
  }
  
  .message-container {
    background-color: #262424; /* Light grey background */
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    display: inline-block;
    max-width: 80%;
  }
  </style>
  
