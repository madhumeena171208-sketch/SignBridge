import cv2
import sys

def run_sign_tracker():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("🚀 SignBridge Video Stream Started (OpenCV Mode). Press 'q' to exit.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break

        # Flip the frame horizontally for a selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Add an overlay text for the hackathon MVP demo
        cv2.putText(
            frame, 
            "SignBridge MVP - Live Camera feed active", 
            (30, 40), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, 
            (0, 255, 0), 
            2
        )

        # Show live window
        cv2.imshow('SignBridge - Live ISL Tracker', frame)

        # Press 'q' to quit the window
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_sign_tracker()