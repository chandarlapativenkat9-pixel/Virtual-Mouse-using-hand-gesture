import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# --- Configuration ---
width_cam, height_cam = 640, 480
frame_reduction = 100  # Frame Reduction (pixels) to reach corners easily
smoothening = 7        # Higher = Smoother cursor, Lower = Faster response

# --- Setup ---
cap = cv2.VideoCapture(0)
cap.set(3, width_cam)
cap.set(4, height_cam)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

width_screen, height_screen = pyautogui.size()

plocX, plocY = 0, 0  # Previous Location
clocX, clocY = 0, 0  # Current Location
last_click_time = 0  # To prevent double clicking

while True:
    success, img = cap.read()
    if not success:
        break
    
    # Flip image for mirror view
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    # Draw Reference Rect (The active area for your hand)
    cv2.rectangle(img, (frame_reduction, frame_reduction), 
                  (width_cam - frame_reduction, height_cam - frame_reduction),
                  (255, 0, 255), 2)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = hand_landmarks.landmark
            
            # Get coordinates of Index (8) and Thumb (4)
            index_x = int(landmarks[8].x * width_cam)
            index_y = int(landmarks[8].y * height_cam)
            thumb_x = int(landmarks[4].x * width_cam)
            thumb_y = int(landmarks[4].y * height_cam)

            # --- 1. Move Mouse (Index Finger Up) ---
            # Only move if inside the reduction frame
            if frame_reduction < index_x < width_cam - frame_reduction and frame_reduction < index_y < height_cam - frame_reduction:
                
                # Convert Coordinates (Interpolation)
                x3 = np.interp(index_x, (frame_reduction, width_cam - frame_reduction), (0, width_screen))
                y3 = np.interp(index_y, (frame_reduction, height_cam - frame_reduction), (0, height_screen))
                
                # Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                
                # Move Mouse
                pyautogui.moveTo(clocX, clocY)
                plocX, plocY = clocX, clocY
                
                # Visual Indicator (Circle on Index)
                cv2.circle(img, (index_x, index_y), 10, (255, 0, 255), cv2.FILLED)

            # --- 2. Clicking Mode (Index + Thumb close) ---
            distance = np.hypot(index_x - thumb_x, index_y - thumb_y)
            
            if distance < 30: # Threshold for click
                cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED) # Green when clicked
                
                # Debouncing (Wait 0.5s before next click)
                if time.time() - last_click_time > 0.5:
                    pyautogui.click()
                    last_click_time = time.time()
                    print("Clicked!")

    # Display FPS
    # cv2.putText(img, f'Virtual Mouse', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    
    cv2.imshow("AI Virtual Mouse", img)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
