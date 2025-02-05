import pyautogui
import mysql.connector
import time

# MySQL Connection Setup
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # Change to your MySQL server
        user="root",  # Your MySQL username
        password="password",  # Your MySQL password
        database="mouse_events"  # Your database name
    )

def log_mouse_event(event_type, x, y):
    db_connection = create_connection()
    cursor = db_connection.cursor()

    query = "INSERT INTO events (event_type, x, y) VALUES (%s, %s, %s)"
    cursor.execute(query, (event_type, x, y))
    db_connection.commit()
    cursor.close()
    db_connection.close()

def track_mouse():
    previous_position = pyautogui.position()
    while True:
        current_position = pyautogui.position()

        # If the mouse position changes, log it
        if current_position != previous_position:
            x, y = current_position
            print(f"Mouse moved to {x}, {y}")
            log_mouse_event("move", x, y)
            previous_position = current_position

        # Check for mouse clicks
        if pyautogui.mouseInfo().get("left"):
            x, y = current_position
            print(f"Left Click at {x}, {y}")
            log_mouse_event("click", x, y)
            time.sleep(0.2)  # To avoid multiple click logs for the same click

        time.sleep(0.1)  # To reduce CPU usage

if __name__ == "__main__":
    track_mouse()
