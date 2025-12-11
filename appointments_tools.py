import re

# GLOBAL DATA STORE
appointment_data = {
    "name": None,
    "phone": None,
    "doctor": None,
    "date": None,
    "time": None
}

def extract_info(text: str) -> str:
    name_match = re.search(r"(?:my name is|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", text, re.IGNORECASE)
    phone_match = re.search(r"\b\d{10}\b", text)
    doctor_match = re.search(r"(?:doctor|dr|specialist|dermatologist|cardiologist|dentist)\s+([A-Za-z ]+)", text, re.IGNORECASE)
    date_match = re.search(r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{4})\b", text)
    time_match = re.search(r"\b(?:\d{1,2}:\d{2}\s?(?:AM|PM|am|pm))\b", text)

    response = []

    if name_match:
        appointment_data["name"] = name_match.group(1).title()
        response.append("✔️ Name saved.")

    if phone_match:
        appointment_data["phone"] = phone_match.group(0)
        response.append("✔️ Phone number saved.")

    if doctor_match:
        appointment_data["doctor"] = doctor_match.group(1).strip().title()
        response.append("✔️ Doctor/specialization saved.")

    if date_match:
        appointment_data["date"] = date_match.group(0)
        response.append("✔️ Appointment date saved.")

    if time_match:
        appointment_data["time"] = time_match.group(0)
        response.append("✔️ Time saved.")

    if not response:
        return "❓ I couldn't extract any appointment information. Please try again."

    return " ".join(response) + " Let me see what else I need."


def check_goal(_: str) -> str:
    missing = [k for k, v in appointment_data.items() if not v]

    if not missing:
        return (
            f"🎉 Appointment Booked Successfully!\n\n"
            f"👤 *Name:* {appointment_data['name']}\n"
            f"📞 *Phone:* {appointment_data['phone']}\n"
            f"🩺 *Doctor:* {appointment_data['doctor']}\n"
            f"📅 *Date:* {appointment_data['date']}\n"
            f"⏰ *Time:* {appointment_data['time']}\n\n"
            "Your appointment is confirmed ✔️"
        )
    else:
        return f"⏳ I still need: {', '.join(missing)}."
