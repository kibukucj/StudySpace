# 📚 Virtual Study Space

_A focused, interactive, and collaborative web platform for your study sessions._

## 🚀 Overview

**Virtual Study Space** is a dynamic web application designed to empower university students with flexible and effective study tools — anywhere, anytime. Whether you're a solo learner aiming for laser focus or someone who thrives in collaborative study groups, this platform is your digital academic sanctuary.

Built with Django and infused with modern web technologies, the platform offers a hybrid of accountability, community, and productivity — all in one intuitive interface.

## 🌟 Key Features

- **🧠 Solo Space with Pomodoro Timer**  
  Optimize your focus using the proven Pomodoro technique with built-in study timers and goal input areas.

- **🎯 Study Goals**  
  Set, track, and achieve academic milestones. Stay motivated with real-time goal tracking and smart reminders.

- **📊 Study Stats**  
  Visualize your productivity through graphs and analytics that track your study hours and progress over time.

- **💬 Community Rooms**  
  Connect with peers through real-time chats and topic-specific rooms. Build your academic tribe and collaborate meaningfully.

- **🃏 Flashcards**  
  Create, manage, and review flashcard decks. Reinforce your memory and ace your revision.

- **🛡️ Secure and Scalable**  
  Built using Django’s robust security features, ensuring your data and sessions remain protected.

## 🛠️ Technologies Used

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Development)  

## 🗂️ Project Structure

```bash
StudySpace/
├── community/       # Handles real-time chats and public rooms
├── flashcard/       # Manages flashcard creation and review
├── goals/           # Study goal tracking
├── studyapp/        # User management & solo study sessions
├── templates/       # HTML templates per module
├── static/          # CSS, JS, media
├── db.sqlite3       # SQLite dev database
├── manage.py        # Django admin utility
└── StudySpace/      # Project settings and routing
```

## 📈 Motivation

Students often struggle with:

- Maintaining study discipline without external structure.
- Finding peers to collaborate with in real-time.
- Managing learning across multiple subjects with limited tracking tools.

**Virtual Study Space** was built to bridge this gap — enhancing productivity and motivation through smart digital environments that blend **accountability**, **community**, and **data insights**.

## 📸 Screenshots

> 🏠 Home Page |
> ![image](https://github.com/user-attachments/assets/571cf063-bda1-4551-b53c-7282ed073a6a)
> ![image](https://github.com/user-attachments/assets/655af170-07e3-4dca-bf30-ebad6e1b2b08)

> 🧘 Solo Study and Goals |
> ![image](https://github.com/user-attachments/assets/7fba6e0f-a4be-4b3d-b7ad-fbc2a2f0af84)
> ![image](https://github.com/user-attachments/assets/8137bfc6-d544-43ce-8cef-eee14cbdb9ad)

> 🗨️ Community Chat |
> ![image](https://github.com/user-attachments/assets/2af27973-462c-4879-b046-575210e839fc)
> ![image](https://github.com/user-attachments/assets/220c1293-cd8a-4955-a24f-3b4e042b0e82)

> 🗃️ Flashcards |
>![image](https://github.com/user-attachments/assets/79cb01fc-8372-413b-b132-d50f3868e00d)

## 📬 Contact & Support

Need help or want to contribute? Reach out via email **cjkibuku@gmail.com**

---

## 🏁 Get Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtualenv (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/studyspace.git
cd studyspace

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Launch the app
python manage.py runserver
```

Then navigate to `http://127.0.0.1:8000/` in your browser!

---

## 💡 Future Enhancements

- 🌐 Real-time video integration for study rooms
- 📱 Mobile app version
- 🧠 AI-powered study assistant
- 🎖️ Achievements and gamification

---

## 👩‍💻 Author

**Kibuku Carole June Wanjiku**  
Bachelor of Science in Computer Science  
University of Nairobi | June 2024
