# Simple Calculator Web App

This is a simple calculator web application with a vanilla JavaScript frontend and a Python Flask backend.

## Features

-   **Frontend**: HTML, CSS, and vanilla JavaScript for a responsive user interface.
-   **Backend**: Python Flask handles arithmetic operations.
-   **Operations**: Add, Subtract, Multiply, Divide, Modulo, Power.
-   **Input Validation**: Numbers check, divide-by-zero handling.
-   **Clear Button**: Resets the current calculation.
-   **History**: Displays the last 10 calculation results on the frontend.
-   **Error Handling**: User-friendly error messages.
-   **API Endpoints**:
    -   `POST /api/calc`: Performs calculations.
    -   `GET /api/health`: Health check endpoint.
-   **CORS**: Enabled for frontend-backend communication.

## Project Structure

```
.
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── test_app.py
└── README.md
```

## Setup and Run Instructions

Follow these steps to set up and run the application locally.

### 1. Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create a Python virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    -   **Windows (Command Prompt):** `.\venv\Scripts\activate.bat`
    -   **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
    -   **macOS/Linux:** `source venv/bin/activate`
4.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the Flask backend server:
    ```bash
    python app.py
    ```
    The backend will start on `http://127.0.0.1:5000`.

### 2. Frontend Setup

The frontend is a static web application. You can simply open the `index.html` file in your web browser.

1.  Navigate back to the project root directory:
    ```bash
    cd ..
    ```
2.  Open `frontend/index.html` in your preferred web browser.

    Alternatively, if you have a local web server (e.g., `http-server` for Node.js, or Python's built-in simple server), you can serve the `frontend` directory:
    ```bash
    # From project root
    # For Python 3:
    python -m http.server 8000 --directory frontend
    # Then open http://localhost:8000 in your browser
    ```
    This approach is often better to avoid CORS issues when serving static files directly from the filesystem, though CORS is already handled by the Flask backend.

## Running Tests (Backend)

To run the backend unit tests:

1.  Ensure your virtual environment is activated (follow steps 1-3 in "Backend Setup").
2.  Navigate to the `backend` directory.
    ```bash
    cd backend
    ```
3.  Run the tests:
    ```bash
    python -m unittest test_app.py
    ```

## Usage

1.  **Enter Numbers**: Click the number buttons to input your first number.
2.  **Select Operation**: Click an operator button (+, -, *, /, %, ^).
3.  **Enter Second Number**: Input the second number.
4.  **Get Result**: Click the "=" button to perform the calculation.
5.  **Clear**: Use the "C" button to clear the current display.
6.  **History**: The last 10 calculations will be shown in the history section.
7.  **Error Messages**: Invalid inputs or operations (like division by zero) will display an error message.

## One-Command Run Mode (Auto-Start)

For a simplified startup, you can use the `run.py` script. This script will automatically start the Flask backend, wait for it to be ready, and then open the frontend in your default web browser.

**Prerequisites:**
11. Ensure you have completed the "1. Backend Setup" steps once to create the virtual environment and install dependencies in the `backend/` directory.

**To Run:**

1.  Navigate to the project's root directory:
    ```bash
    cd /path/to/your/calculater/calculater
    ```
2.  Execute the `run.py` script:
    ```bash
    python run.py
    ```
    The script will print status messages, indicating when the backend is starting, checking its health, and opening the frontend.
3.  To stop the application, press `Ctrl+C` in the terminal where `run.py` is running. The script will gracefully shut down the Flask backend.

