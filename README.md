# 🌉 SignBridge
*"Every sign deserves to be understood."* 

Proposed real-time Indian Sign Language (ISL) to text experience for video calls, powered by intelligent context cards. Built for **Kritical Hacks 2026**.

---

## 📌 01 • The Problem & Research Foundation
* **The Accessibility Gap:** Over **330 million** hard-of-hearing people worldwide—including **63+ million in India**—face severe communication barriers in daily education, telehealth, and professional video calls. This is worsened by a massive shortage of certified ISL interpreters (only ~300 certified interpreters across India) and a total lack of built-in video-call translation tools.
* **Research Base:** Built upon the **ISLTranslate (ACL 2023)** dataset, leveraging 31,222 sentence/phrase pairs across 11,655 vocabulary words to ensure accurate structural modeling.

---

## 💡 02 • Innovation & Idea
* **Beyond Literal Translation:** Traditional tools only convert signs into static text. **SignBridge** introduces an active conversational layer by combining computer vision with live web intelligence.
* **Smart Contextual Awareness:** While translating Indian Sign Language live over a video stream, the system understands context and triggers real-time assistant cards so that conversations remain smooth, contextual, and uninterrupted.

---

## 🌍 03 • Impact & Usefulness
* **Real-World Utility:** Solves an urgent, everyday inclusion problem for millions of individuals in remote learning, corporate meetings, and emergency medical consultations.
* **High Realism & Scalability:** Designed to plug directly into existing WebRTC-based video streaming pipelines (FastAPI backend and browser-based WebSockets), making it lightweight and practical for modern web browsers without requiring heavy local hardware upgrades.

---

## 🔌 04 • TinyFish API Integration
* **How TinyFish is Used:** TinyFish serves as the core intelligent engine of SignBridge. When a key sign or query (e.g., *"Medical Assistance"* or specific terminology) is captured during a live video call, the backend automatically queries the **TinyFish API** to fetch trusted public web context and background data.
* **Live Context Cards:** These fetched insights are instantly rendered as concise UI cards on the video call interface, helping participants bridge comprehension gaps instantly.
* **Future Scaling:** Leverages agentic search pipelines to recommend learning resources and automate post-call action items (such as booking appointments or summarizing call transcripts).

---

## 🚀 05 • Proposed Experience & Tech Stack
* **AI / ML Core:** Python, PyTorch/TensorFlow, MediaPipe Holistic (extracting 75 keypoints per frame from pose and both hands). Staged roadmap transitioning from a lightweight baseline to a Pose-SLT Transformer model.
* **Backend & Streaming:** FastAPI, WebSockets, WebRTC, OpenCV.
* **Frontend:** HTML5, JavaScript (Webcam stream capture and real-time JSON response rendering).

---

## 💼 06 • Business & Revenue Model (Market Research & Economics)
* **Market Opportunity:** With the rapid growth of remote work and digital education in India, the demand for accessible workplace technology is surging. Human ISL interpreters typically charge **₹1,000 to ₹2,000 ($12–$24) per hour**, making continuous interpretation financially prohibitive for everyday students and small businesses.
* **Tiered Pricing Strategy:**
  * **Freemium Plan (Individuals):** Free basic translation for up to 30 minutes per day to drive organic adoption.
  * **SignBridge Pro (Power Users):** **₹499 (~$6) / month** for unlimited personal video calls, faster translation speed, and advanced TinyFish context cards.
  * **Enterprise & Institutional API (Schools, Hospitals, Corporates):** **₹15,000 (~$180) / month** per organization for dedicated compliance-ready server deployments, secure Zoom/Meet plugin integration, and custom vocabulary training.

---

## 🗺️ 07 • Roadmap
* **Phase 1 (MVP - Current):** Local FastAPI WebSocket streaming backend, OpenCV prototype, and TinyFish API context card integration.
* **Phase 2:** Sentence-level translation, text-to-speech output, and regional Indian language support.
* **Phase 3:** Native browser extensions and direct plugins for Zoom, Google Meet, and Microsoft Teams.

---

## 📢 Social Announcement & Community
Curious about how we built **SignBridge** as a team (**Tech Titans**)? Check out our team announcement and journey shared on LinkedIn:

👉 *[Read our LinkedIn Post about SignBridge - (https://www.linkedin.com/feed/update/urn:li:activity:7519106618513580034/)**

*Built with passion by Team Tech Titans for accessible communication.*

## 💻 Running the Local Prototype
To test the live webcam stream and tracking prototype locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/madhumeena171208-sketch/SignBridge.git](https://github.com/madhumeena171208-sketch/SignBridge.git)
   cd SignBridge
