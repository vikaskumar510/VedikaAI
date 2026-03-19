# VedikaAI

## Project Overview

VedikaAI is a full-stack AI-powered project that integrates a React frontend with a Python Flask backend. This project aims to leverage AI technologies to provide innovative solutions.

## Folder Structure

```
VedikaAI/
│
├── frontend/               # React + TypeScript frontend
│   ├── public/             # Public assets
│   ├── src/                # Source files
│   │   ├── components/      # React components
│   │   ├── hooks/           # Custom hooks for React
│   │   ├── pages/           # Application pages
│   │   └── utils/           # Utility functions
│   └── package.json         # Frontend dependencies
│
├── backend/                # Python Flask backend
│   ├── app/                # Application files
│   │   ├── models/          # Database models
│   │   ├── routes/          # API routes
│   │   ├── services/        # Logic for AI integration
│   │   └── requirements.txt  # Backend dependencies
│   └── run.py               # Entry point for the Flask app
│
├── ai_logic/               # AI logic integration
│   ├── model/               # Trained models
│   ├── preprocess/          # Data preprocessing scripts
│   └── utils/               # AI utility functions
│
├── database/               # Database files
│   └── migrations/          # Database migrations
│
├── offline_support/         # Offline support files
│   └── service_worker.js    # Service worker for offline capabilities
│
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites
- Node.js (v14 or later)
- Python (v3.6 or later)
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vikaskumar510/VedikaAI.git
   cd VedikaAI
   ```

2. Setup the frontend:
   ```bash
   cd frontend
   npm install
   ```

3. Setup the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

### Running the application
- Start the frontend:
   ```bash
   cd frontend
   npm start
   ```

- Start the backend:
   ```bash
   cd backend
   python run.py
   ```

### Author
- Vikas Kumar - [GitHub](https://github.com/vikaskumar510)  

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.