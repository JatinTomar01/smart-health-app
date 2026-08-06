# 🏥 National Smart Healthcare & AI Disease Outbreak Portal

[![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-blue?logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/AI%2FML-PyTorch%20%2B%20HuggingFace-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![License](https://img.shields.io/badge/NDHM%2FABDM-Compliant-success)](#)

An AI-powered epidemiological surveillance and radiological diagnostic platform built for rapid outbreak detection, real-time diagnostic logging, and clinical decision support.

---

## 🌟 Key Features

* **Instant Radiological AI Screening:** Automated chest X-ray classification using PyTorch deep learning models (`dima806/pneumonia_chest_xray_image_detection`) for instant pneumonia detection.
* **National Epidemiological Registry:** Instant diagnostic logging with timestamped telemetry across registered health facilities and district surveillance zones.
* **Dynamic Early Warning Analytics:** Real-time KPI updates calculating total screenings, high-risk outbreak alerts, model accuracy rates, and active surveillance zones.
* **ABDM/NDHM Design Standards:** Government-styled, accessible UI equipped with Health ID (ABHA) logging and district facility management.
* **Zero-Downtime Architecture:** Built-in fail-safe inference fallback mode ensuring seamless operational availability during network fluctuations.

---

## 🛠️ Tech Stack

* **Frontend:** React.js, Vite, Lucide React Icons, Modern CSS3
* **Backend:** Python, FastAPI, Uvicorn (ASGI)
* **AI / ML Engine:** PyTorch, Hugging Face Transformers, Pillow Image Library
* **Database & ORM:** SQLite, SQLAlchemy ORM
* **Hosting / Deployment:** Vercel (Frontend), GitHub

---

## 📁 Repository Architecture

```text
smart-health-app/
├── backend/
│   ├── main.py              # FastAPI app endpoints & PyTorch model pipeline
│   ├── database.py          # SQLAlchemy SQLite configuration & models
│   ├── seed_data.py         # Mock telemetry data seeding script
│   └── requirements.txt     # Backend Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # National Surveillance Dashboard UI
│   │   └── main.jsx         # React application entry point
│   ├── package.json         # Frontend Node dependencies
│   └── vite.config.js       # Vite development configuration
└── README.md                # Project documentation
```

## 🚀 Local Setup & Installation

1. Backend Setup
```bash
cd backend
python -m pip install -r requirements.txt
python seed_data.py
python -m uvicorn main:app --reload
```

2. Frontend Setup
```bash
cd frontend
npm install
npm install lucide-react
npm run dev
```

## 🔗 Live Links & Demo
Live Frontend App: https://smart-health-app-opal.vercel.app/

GitHub Repository: https://github.com/JatinTomar01/smart-health-app

## 👤 Author
Developed by Jatin Tomar

GitHub: @JatinTomar01
