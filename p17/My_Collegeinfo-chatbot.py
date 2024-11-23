import random
import time

# Sample data representing the student's details
student_info = {
    'name': 'John Doe',
    'roll_number': 'CS12345',
    'department': 'Computer Science',
    'year': '3rd Year',
    'college': 'XYZ University'
}

courses = {
    'current_courses': [
        'Data Structures',
        'Operating Systems',
        'Computer Networks',
        'Discrete Mathematics',
        'Database Management Systems'
    ]
}

timetable = {
    'monday': '9:00 AM - Data Structures\n11:00 AM - Operating Systems',
    'tuesday': '9:00 AM - Computer Networks\n2:00 PM - Discrete Mathematics',
    'wednesday': '10:00 AM - Database Management Systems\n1:00 PM - Data Structures',
    'thursday': '9:00 AM - Operating Systems\n11:00 AM - Data Structures',
    'friday': '10:00 AM - Computer Networks\n1:00 PM - Database Management Systems'
}

grades = {
    'Data Structures': 'A',
    'Operating Systems': 'B+',
    'Computer Networks': 'A-',
    'Discrete Mathematics': 'B',
    'Database Management Systems': 'A'
}

# Function to simulate the bot's response
def respond_to_query(query):
    query = query.lower()  # Convert query to lowercase for easier matching

    # Provide student information
    if 'name' in query:
        return f"My name is {student_info['name']}."
    elif 'roll number' in query or 'roll' in query:
        return f"My roll number is {student_info['roll_number']}."
    elif 'department' in query:
        return f"I am in the {student_info['department']} department."
    elif 'year' in query:
        return f"I am currently in my {student_info['year']}."
    elif 'college' in query:
        return f"I study at {student_info['college']}."

    # Provide course information
    elif 'courses' in query or 'subjects' in query:
        return f"I am currently enrolled in the following courses: " + ", ".join(courses['current_courses']) + "."

    # Provide timetable information
    elif 'timetable' in query or 'schedule' in query:
        return f"Here is my weekly timetable:\n" \
               f"Monday: {timetable['monday']}\n" \
               f"Tuesday: {timetable['tuesday']}\n" \
               f"Wednesday: {timetable['wednesday']}\n" \
               f"Thursday: {timetable['thursday']}\n" \
               f"Friday: {timetable['friday']}"

    # Provide grades
    elif 'grades' in query or 'marks' in query:
        return "Here are my grades:\n" + "\n".join([f"{course}: {grade}" for course, grade in grades.items()])

    # Default response for unrecognized queries
    else:
        return "Sorry, I didn't quite understand that. Can you ask something else?"

# Function to simulate the bot's interaction
def chat_with_bot():
    print("Hello! I am your College Information Bot. How can I assist you today?")
    time.sleep(1)  # Wait for a second for a more natural feel
    
    while True:
        query = input("\nYou: ")
        
        if query.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break
        
        # Bot response
        response = respond_to_query(query)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat_with_bot()
