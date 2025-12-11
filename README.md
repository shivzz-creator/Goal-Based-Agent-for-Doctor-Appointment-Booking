# 🤖 Doctor Appointment Booking Agent (LangChain + OpenAI)

A conversational **goal-based intelligent agent** that automatically books doctor appointments by extracting relevant information from natural conversation.

Built using:
- **LangChain Agents**
- **Tools (custom extract + goal checker)**
- **OpenAI GPT model**
- **Conversation Memory**
- **REACT Agent Framework**

---

## ✨ Features

✔ Collects patient information  
✔ Understands natural language  
✔ Extracts:
- Name  
- Phone Number  
- Doctor/Specialization  
- Preferred Date  
- Preferred Time  

✔ Confirms appointment automatically  
✔ Uses LangChain tool-based reasoning  
✔ Clean, modular, production-ready architecture

---

## 📂 Project Structure

doctor-appointment-agent/
│
├── app.py # main agent loop
├── tools/
│ ├── appointment_tools.py # extract + goal tools
│ └── init.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🚀 Running the Agent

### **1. Clone the repo**
```bash
git clone https://github.com/your-username/doctor-appointment-agent
cd doctor-appointment-agent
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Add your OpenAI key
Create a .env file:

ini
Copy code
OPENAI_API_KEY=your_key_here
4. Run
bash
Copy code
python app.py
🧠 How It Works
The agent uses two custom tools:

🔹 extract_info()
Extracts structured data from user messages using regex.

🔹 check_goal()
Checks whether all five required fields are collected.
If YES → Books the appointment.

🎬 Example Conversation
vbnet
Copy code
🩺 Assistant: Hi! How can I help you today?

👤 User: I want to book an appointment. My name is Rohan.

Assistant: ✔️ Name saved. I still need phone, doctor, date, time.

👤 User: My phone number is 9876543210.

Assistant: ✔️ Phone saved...

👤 User: Dermatologist on 20/01/2025 at 4:30 PM

🎉 Appointment Booked Successfully!
📸 Demo (Add GIF here later)
You can record a terminal GIF using asciinema or OBS.

👨‍⚕️ Future Enhancements
Multi-doctor availability

Email/SMS confirmation

Calendar sync

Integration with hospital APIs

⭐ Like this project?
If this helped you learn LangChain agents, feel free to ⭐ star the repo!

Built with ❤️ by Shivansh Pareek
