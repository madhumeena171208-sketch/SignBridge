# SignBridge
# 🌉 SignBridge
> **"Every sign deserves to be understood."** Proposed real-time Indian Sign Language (ISL) to text experience for video calls. Built for **Kritical Hacks 2026**

---

## 📌 01 • The Problem & Research Foundation
* **The Gap:** 330M+ hard-of-hearing people worldwide (63M+ in India) face communication barriers due to a severe shortage of certified ISL interpreters (~300 in India) and a lack of built-in video-call translation.
* **Research Base:** Built upon the *ISLTranslate (ACL 2023)* dataset featuring **31,222** sentence/phrase pairs across **11,655** vocabulary words.

---

## 🚀 02 • Proposed Experience & Tech Stack
SignBridge converts video feed landmarks into readable captions live during a call.
* **AI / ML:** Python, PyTorch/TensorFlow,MediaPipe Holistic (75 keypoints per frame from pose and both hands). Staged roadmap from a lightweight **LSTM/MLP** baseline to a **Pose-SLT Transformer**.
* **Backend & Calling:** FastAPI, WebSockets, WebRTC, OpenCV.

---

## 🔌 03 • TinyFish API Integration
* **Context Cards (MVP):** Automatically searches and fetches trusted public web context to display concise info cards during live conversations.
* **Future Scaling:** Leverages agent APIs for learning resource pipelines and post-call actions (like appointment booking).

---

## 💼 04 • Business & Roadmap
* **Revenue Model:** Freemium model for individuals; paid deployments for educational and workplace institutions; enterprise API plans.
* **Roadmap:** 
  * *Phase 1 (MVP):* Two-user call with limited common ISL words and fingerspelling.
  * *Phase 2 & 3:* Sentence-level translation, text-to-speech, regional languages, and Zoom/Meet integrations.

---
### 💻 Running the Local OpenCV Prototype
To test the live webcam stream and tracking prototype locally:

1. **Navigate to the backend folder:**
   ```bash
   cd backend
