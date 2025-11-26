# Calculator Web App - Next Steps: Add Auto-Start Mode

## Recommendation

Implement a top-level Python script, `run.py`, to automate the startup sequence of both the Flask backend and the static frontend. This script will ensure the backend is fully operational before launching the frontend in the system's default web browser and will manage a clean shutdown of the backend process upon termination. This provides a "one-command run" experience for the entire project.

## Task Breakdown

### Phase 1: Create Auto-Start Script Structure

**Goal**: Establish the basic structure of the `run.py` script, including necessary imports and initial process management setup.
**Acceptance Criteria**:
- A new file `run.py` exists in the project root.
- The `run.py` script contains imports for `subprocess`, `time`, `webbrowser`, `sys`, and `platform`.
- The script can be executed without immediate errors (though it won't perform any actions yet).

- [x] T001 Create `run.py` in the project root with basic Python script structure and required imports: `subprocess`, `time`, `webbrowser`, `sys`, `platform`, `http.client` (for health checks).
  *   **File**: `run.py`

### Phase 2: Start Backend Process

**Goal**: Modify `run.py` to launch the Flask backend in a separate, non-blocking process, ensuring the correct Python executable from the virtual environment is used.
**Acceptance Criteria**:
- Executing `run.py` initiates the Flask backend process successfully (verified by checking `http://127.0.0.1:5000` manually or by observing terminal output from the backend).
- The `run.py` script itself does not block, allowing subsequent operations like the health check.

- [x] T002 Implement logic in `run.py` to determine the correct Python executable path for the backend's virtual environment based on the detected operating system (`sys.platform`).
  *   **File**: `run.py`
- [x] T003 Use `subprocess.Popen` in `run.py` to start `backend/app.py` in the background, using the determined Python executable and capturing the process object.
  *   **File**: `run.py`

### Phase 3: Backend Health Check

**Goal**: Implement a robust mechanism in `run.py` to poll the backend's `/api/health` endpoint until it responds successfully, indicating the backend is ready.
**Acceptance Criteria**:
- `run.py` waits and continuously checks `http://127.0.0.1:5000/api/health` at regular intervals.
- The script only proceeds to open the frontend after receiving a `{"status": "ok"}` JSON response from the health endpoint.
- Polling includes a reasonable timeout and retry mechanism (e.g., up to 20 attempts with 1-second delays) to gracefully handle backend startup delays.

- [x] T004 Implement a loop in `run.py` to repeatedly attempt an HTTP GET request to `http://127.0.0.1:5000/api/health` using `http.client`.
  *   **File**: `run.py`
- [x] T005 Add `time.sleep()` for a short delay (e.g., 1 second) between health check attempts to prevent resource exhaustion and allow backend startup.
  *   **File**: `run.py`
- [x] T006 Implement error handling (e.g., `try-except`) for `ConnectionRefusedError` and other potential network issues during health checks.
  *   **File**: `run.py`

### Phase 4: Open Frontend in Browser

**Goal**: Once the backend is confirmed running, `run.py` should automatically launch the calculator frontend in the user's default web browser.
**Acceptance Criteria**:
- The system's default web browser automatically opens to the local file path of `frontend/index.html` after the backend is confirmed ready.

- [x] T007 Construct the absolute file URL for `frontend/index.html`.
  *   **File**: `run.py`
- [x] T008 Use `webbrowser.open_new_tab()` in `run.py` to open the constructed URL in the default browser.
  *   **File**: `run.py`

### Phase 5: Clean Shutdown on Ctrl+C

**Goal**: Ensure the backend process is terminated gracefully when `run.py` is stopped (e.g., by the user pressing `Ctrl+C`).
**Acceptance Criteria**:
- Pressing `Ctrl+C` in the terminal running `run.py` triggers a shutdown sequence that terminates both `run.py` and the child Flask backend process.
- No orphaned Flask processes remain after `run.py` exits.

- [x] T009 Implement a `try...finally` block around the main execution logic in `run.py` to guarantee cleanup actions.
  *   **File**: `run.py`
- [x] T010 Within the `finally` block, call `backend_process.terminate()` to send a termination signal to the Flask backend.
  *   **File**: `run.py`
- [x] T011 Add `backend_process.wait()` in the `finally` block to wait for the backend process to fully exit before `run.py` completes.
  *   **File**: `run.py`
- [x] T012 Add informative print statements in `run.py` to indicate startup progress, successful launch, and graceful shutdown.
  *   **File**: `run.py`

### Phase 6: Update Documentation

**Goal**: Provide clear instructions in the `README.md` for using the new "One-Command Run Mode".
**Acceptance Criteria**:
- The `README.md` includes a new section detailing how to prepare the environment and use `python run.py`.
- The instructions are clear and easy to follow.

- [x] T013 Update `README.md` with a new section titled "One-Command Run Mode" explaining how to execute `python run.py` from the project root.
  *   **File**: `README.md`
- [x] T014 Ensure the `README.md` also clearly mentions that the virtual environment for the backend needs to be set up first, and `pip install -r backend/requirements.txt` needs to be run once.
  *   **File**: `README.md`

### Optional Stretch Tasks

**Goal**: Enhance the robustness, usability, and feedback of the auto-start script.
**Acceptance Criteria**:
- The script provides more detailed output for troubleshooting.
- Users can customize key parameters via command-line arguments.

- [ ] S001 Implement proper logging for `run.py` instead of simple print statements, writing to a log file or providing more verbose console output.
  *   **File**: `run.py`
- [ ] S002 Add command-line argument parsing (e.g., using `argparse`) to `run.py` for configuring the backend port, health check timeout, or frontend file path.
  *   **File**: `run.py`
