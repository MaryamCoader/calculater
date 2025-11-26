import subprocess
import time
import webbrowser
import sys
import platform
import http.client
import os

# --- Configuration ---
BACKEND_PORT = 5000
BACKEND_HOST = "127.0.0.1"
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"
HEALTH_CHECK_ENDPOINT = f"/api/health"
FRONTEND_HTML_PATH = os.path.join("frontend", "index.html")

# --- Helper Functions ---
def get_python_executable():
    """Determines the correct Python executable for the backend venv based on OS."""
    venv_path = os.path.join("backend", "venv")
    if platform.system() == "Windows":
        return os.path.join(venv_path, "Scripts", "python.exe")
    else: # Linux, macOS
        return os.path.join(venv_path, "bin", "python")

def main():
    print("Starting auto-start sequence...")
    backend_process = None
    try:
        # --- T003: Start Backend Process ---
        print(f"Attempting to start backend at {BACKEND_URL}...")
        python_executable = get_python_executable()
        
        # Ensure the venv Python exists
        if not os.path.exists(python_executable):
            print(f"Error: Python executable not found at '{python_executable}'")
            print("Please ensure you have created and activated the virtual environment in the 'backend' directory and installed dependencies.")
            sys.exit(1)

        backend_process = subprocess.Popen(
            [python_executable, os.path.join("backend", "app.py")],
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE,  # Capture stderr
            text=True # Decode stdout/stderr as text
        )
        print(f"Backend process started (PID: {backend_process.pid}).")
        
        # --- T004-T006: Backend Health Check ---
        print(f"Waiting for backend to become healthy at {BACKEND_URL}{HEALTH_CHECK_ENDPOINT}...")
        max_attempts = 20
        for attempt in range(1, max_attempts + 1):
            try:
                conn = http.client.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=1)
                conn.request("GET", HEALTH_CHECK_ENDPOINT)
                response = conn.getresponse()
                if response.status == 200:
                    data = response.read().decode('utf-8')
                    if '"status": "ok"' in data:
                        print(f"Backend is healthy after {attempt} attempts.")
                        break
                else:
                    print(f"Attempt {attempt}/{max_attempts}: Backend returned status {response.status}")
                conn.close()
            except ConnectionRefusedError:
                print(f"Attempt {attempt}/{max_attempts}: Connection refused, backend not ready yet...")
            except http.client.CannotSendRequest:
                 print(f"Attempt {attempt}/{max_attempts}: Backend not ready or connection issue...")
            except Exception as e:
                print(f"Attempt {attempt}/{max_attempts}: An unexpected error occurred during health check: {e}")
            
            time.sleep(1) # T005
            if attempt == max_attempts:
                print("Backend did not become healthy within the expected time. Exiting.")
                sys.exit(1)

        # --- T007-T008: Open Frontend in Browser ---
        print("Backend is ready. Opening frontend in browser...")
        frontend_path = os.path.abspath(FRONTEND_HTML_PATH)
        webbrowser.open_new_tab(f"file://{frontend_path}")
        print(f"Opened frontend: file://{frontend_path}")

        print("\nProject is running. Press Ctrl+C to stop.")
        # Keep the main script alive while the backend runs
        # This will allow Ctrl+C to be caught by the outer try-finally
        while backend_process.poll() is None:
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Shutting down...")
    finally: # T009-T011: Clean Shutdown
        if backend_process and backend_process.poll() is None:
            print("Terminating backend process...")
            backend_process.terminate()
            try:
                backend_process.wait(timeout=5) # Give it 5 seconds to terminate
                print("Backend process terminated.")
            except subprocess.TimeoutExpired:
                print("Backend process did not terminate gracefully, forcing kill.")
                backend_process.kill()
        elif backend_process:
            print("Backend process already exited.")
        
        # Optional: Display backend output if it exited unexpectedly
        if backend_process and backend_process.returncode != 0:
            stdout, stderr = backend_process.communicate()
            if stdout:
                print("\n--- Backend Stdout ---")
                print(stdout.strip())
            if stderr:
                print("\n--- Backend Stderr ---")
                print(stderr.strip())
        print("Auto-start sequence finished.")

if __name__ == "__main__":
    main()
