# 🖱️ AI Virtual Mouse: Hand Gesture Control

> **Touchless computing using OpenCV & MediaPipe**

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Computer Vision](https://img.shields.io/badge/Library-OpenCV%20%7C%20MediaPipe-green)

## 📖 Overview
The **AI Virtual Mouse** is a Human-Computer Interaction (HCI) application that allows users to control their system cursor using simple hand gestures. By utilizing a standard webcam, the system detects hand landmarks and maps them to mouse actions, eliminating the need for a physical mouse.

This project demonstrates the power of Computer Vision in creating touchless interfaces, which can be highly beneficial for accessibility or sterile environments (like operating rooms).

## 🚀 Key Features
* **Cursor Movement:** Smoothly tracks the index finger tip to move the cursor.
* **Left Click:** Detects a specific gesture (e.g., joining Index & Thumb or dropping the index finger) to perform a click.
* **Right Click:** Recognized via a secondary gesture (e.g., Middle finger extension).
* **Scroll Functionality:** Vertical scrolling enabled by easy hand movements.
* **Frame Rate Display:** Real-time FPS monitoring to check performance.
* **No Hardware Required:** Works with any standard webcam.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **Hand Tracking:** MediaPipe (Google's ML solution)
* **Automation:** PyAutoGUI (For controlling the OS mouse)
* **Math:** NumPy (For coordinate calculation and smoothing)

## 🎮 Gesture Guide
| Action | Hand Gesture |
| :--- | :--- |
| **Move Cursor** | Index Finger Up ☝️ |
| **Left Click** | Index + Middle Finger Up (Distance < Threshold) ✌️ |
| **Right Click** | Index + Middle + Ring Finger Up 🤟 |
| **No Action** | Fist / All fingers closed ✊ |

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/virtual-mouse.git](https://github.com/YourUsername/virtual-mouse.git)
    cd virtual-mouse
    ```

2.  **Install Dependencies**
    You can install all required libraries using pip:
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

## 🧠 How It Works
1.  **Capture:** The webcam captures frames in real-time.
2.  **Detection:** MediaPipe processes the frame to identify 21 hand landmarks.
3.  **Processing:** The coordinates of the **Index Finger Tip (ID 8)** and **Middle Finger Tip (ID 12)** are extracted.
4.  **Mapping:** These coordinates are converted from camera resolution to screen resolution using linear interpolation.
5.  **Action:**
    * If only the Index finger is up $\rightarrow$ **Moving Mode**.
    * If Index and Middle fingers are both up and close together $\rightarrow$ **Clicking Mode**.

## 📸 Screenshots
| Hand Tracking | Clicking Action |
|:---:|:---:|
| ![Tracking](images/tracking_demo.png) | ![Clicking](images/clicking_demo.png) |

## 🔮 Future Scope
* Adding AI Voice Assistant integration (e.g., "Open Chrome").
* Implementing Drag and Drop functionality.
* Virtual Keyboard for typing on screen.

## 👥 Contributors
* **[venkat chandarlapati]** - *Developer*

## 📄 License
This project is licensed under the MIT License.
