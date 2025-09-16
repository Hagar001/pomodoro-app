# Pomodoro GUI Application ⏰🍅

A graphical **Pomodoro Timer App** built with **Python, Tkinter, and Pygame**.  
This project is based on "100 Days of Code: The Complete Python Bootcamp by Angela Yu"**, with added features such as **pause/resume functionality** and **sound alerts**.

---

## ✨ Features
- **Start button** → starts the Pomodoro timer.
- **Pause / Resume button** → allows you to pause the timer and resume from where you left off.
- **Reset button** → resets the timer and clears progress.
- **Automatic transitions**:
  - 25 minutes of work (Pomodoro session).
  - 5 minutes of short break after each session.
  - 20 minutes of long break after every **4 Pomodoros**.
- **Checkmarks ✔️** appear at the bottom, tracking completed Pomodoros.
- **Sound alert** (using Pygame) plays when a Pomodoro or break finishes.

---

## 🛠️ Technologies Used
- **Python 3**
- **Tkinter** (GUI framework)
- **Pygame** (for sound playback)
- **Math module** (for countdown mechanism)

---

## 📂 Project Structure

pomodoro/
│── main.py        # Main application script
│── tomato.png         # Tomato image for the timer display
│── music.mp3          # Sound file played at the end of sessions
│── README.md          # Project documentation


---

## 🚀 Installation & Setup
1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/Hagar001/pomodoro-app.git
   cd pomodoro-app
   ```
2. Install required dependencies:
   ```bash
   pip install pygame
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## 🎮 How to Use

1. **Click Start** → begin a Pomodoro (25 minutes).
2. **Work until the timer ends** → a sound plays, and it automatically switches to a break.
3. **Pause/Resume** → if you need to stop the timer temporarily.
4. **Reset** → clears progress and restarts the timer from 00:00.
5. Track your progress with the ✔️ marks after each completed Pomodoro.

---

## 📝 Notes

* Ensure `tomato.png` and `music.mp3` are in the same directory as the script.
* You can replace `music.mp3` with your preferred sound effect.

---

## 📸 Preview
<img width="617" height="494" alt="Capture-pomo0" src="https://github.com/user-attachments/assets/a1f5920f-31fe-4492-8516-02adf4869c4c" />

<img width="618" height="493" alt="Capture-pomo03" src="https://github.com/user-attachments/assets/28079c0e-6b7e-45ad-b0e3-5f11df657e20" />


<img width="615" height="492" alt="Capture-pomo4" src="https://github.com/user-attachments/assets/d5fe39c1-09b9-409d-812e-22137662438e" />

<img width="581" height="490" alt="Capture-pomo7" src="https://github.com/user-attachments/assets/a6287181-eab3-4606-a821-078dd94d26ea" />

## 📚 Credits

* Original project idea from [100 Days of Code: The Complete Python Bootcamp by Angela Yu].
* Extended with **pause/resume functionality** and **sound integration**.
