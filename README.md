# SignBridge
# 🌉 SignBridge
> **"Every sign deserves to be understood."** Proposed real-time Indian Sign Language (ISL) to text experience for video calls[cite: 1]. Built for **Kritical Hacks 2026**[cite: 1].

---

## 📌 01 • The Problem & Research Foundation
* **The Gap:** 330M+ hard-of-hearing people worldwide (63M+ in India) face communication barriers due to a severe shortage of certified ISL interpreters (~300 in India) and a lack of built-in video-call translation[cite: 1].
* **Research Base:** Built upon the *ISLTranslate (ACL 2023)* dataset featuring **31,222** sentence/phrase pairs across **11,655** vocabulary words[cite: 1].

---

## 🚀 02 • Proposed Experience & Tech Stack
SignBridge converts video feed landmarks into readable captions live during a call[cite: 1].
* **AI / ML:** Python, PyTorch/TensorFlow, MediaPipe Holistic (**75 keypoints per frame** across hands, pose, and face)[cite: 1]. Staged roadmap from a lightweight **LSTM/MLP** baseline to a **Pose-SLT Transformer**[cite: 1].
* **Backend & Calling:** FastAPI, WebSockets, WebRTC, OpenCV[cite: 1].

---

## 🔌 03 • TinyFish API Integration
* **Context Cards (MVP):** Automatically searches and fetches trusted public web context to display concise info cards during live conversations[cite: 1].
* **Future Scaling:** Leverages agent APIs for learning resource pipelines and post-call actions (like appointment booking)[cite: 1].

---

## 💼 04 • Business & Roadmap
* **Revenue Model:** Freemium model for individuals; paid deployments for educational and workplace institutions; enterprise API plans[cite: 1].
* **Roadmap:** 
  * *Phase 1 (MVP):* Two-user call with limited common ISL words and fingerspelling[cite: 1].
  * *Phase 2 & 3:* Sentence-level translation, text-to-speech, regional languages, and Zoom/Meet integrations[cite: 1].

---

