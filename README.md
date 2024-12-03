# Typing Speed Test App

The **Typing Speed Test App** is a desktop application built with Python's Tkinter module. It allows users to test and improve their typing speed while tracking their progress. Users can log in, select difficulty levels, and compete with their personal high scores.

---

## Features
- **User Management**:
  - Login and create a new user.
  - Tracks high scores for each user.
- **Difficulty Levels**:
  - Choose from multiple difficulty levels with preloaded sample texts.
- **Real-time Feedback**:
  - Highlights correct and incorrect words as you type.
- **Typing Speed Calculation**:
  - Calculates words per minute (WPM) after the test.
- **Data Persistence**:
  - Saves user scores locally for future sessions.

---

## Files in the Project

### 1. `typing_speed_app.py`
This is the main file for the application. It defines the `TypingSpeedApp` class and creates the user interface using Tkinter. The file includes logic for:
- User login and signup.
- Displaying sample text.
- Real-time typing feedback.
- Calculating and displaying typing speed.

### 2. `functions.py`
Contains utility functions for loading and saving user data:
- **`load_user_data`**: Loads user scores from a JSON file (`user_scores.json`).
- **`save_user_data`**: Saves updated user scores to the file.

### 3. `sample_texts.py`
Stores preloaded sample texts for different difficulty levels. Texts are randomly chosen during the test based on the selected level.

### 4. `user_scores.json`
A JSON file used to store user scores persistently. This file is created automatically during the app's first run if it doesn’t already exist.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shrabhay/Typing-Speed-Test-Desktop-App
   cd Typing-Speed-Test-Desktop-App
   ```

2. Install Python (if not already installed):
   * Download Python and follow the instructions for your operating system.

3. Install dependencies:
   * This project uses only the built-in Python modules, so no additional dependencies are required.

4. Run the application:
    ```commandline
    python3 typing_speed_app.py
    ```

---

## How to Use
1. Launch the app and enter a username.
   * If you're a new user, click New User.
   * If you're returning, click Login.

2. Select a difficulty level.

3. Click Start to begin the test.

   * Type the displayed sample text in the typing area.

4. Click Stop when you're done to calculate your typing speed (WPM).

5. Compete against your personal high score!

---

## Project Structure
```text
typing-speed-test-app/
│
├── typing_speed_app.py   # Main application file
├── functions.py          # Utility functions for user data
├── sample_texts.py       # Preloaded sample texts
├── user_scores.json      # User score data (auto-generated)
└── README.md             # Project documentation
```

---

## Future Improvements
* Add a leaderboard to compare scores among users.
* Support for more languages and sample texts.
* Store data in a database for scalability.
* Improve real-time feedback with additional metrics (accuracy, time per word).

---

## License
This project is licensed under the MIT License.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.
