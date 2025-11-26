# Simple Calculator Web App - Tasks

## Dependencies

This feature has the following user story dependencies:
- US1 (Core Arithmetic Operations) must be completed before other stories can fully leverage the backend.
- US2 (Additional Arithmetic Operations) depends on US1's core backend structure.
- US3 (Calculator UI & Basic Interaction) and US4 (Calculation History) depend on the backend API endpoints being available.
- US5 (API Health Check & Robustness) can be developed in parallel with other backend tasks but is crucial for a robust application.

## Parallel Execution

- Backend setup tasks (T003-T006) can be parallelized.
- Frontend UI tasks (T015-T017) can be started as soon as the basic HTML and CSS are laid out, partially in parallel with backend development.
- Unit tests for backend (T006, T011, T014, T024) can be run independently after corresponding implementation.

## Implementation Strategy

We will follow an MVP-first approach, prioritizing core arithmetic functions and basic UI before implementing history and additional operations. Each user story will be implemented and tested incrementally.

---

### Phase 1: Setup

- [ ] T001 Create project directory structure: `frontend/`, `backend/`, `README.md`
- [ ] T002 Set up Python virtual environment for backend in `backend/venv/`

### Phase 2: Foundational Backend

- [ ] T003 Implement Flask app basic setup and CORS in `backend/app.py`
- [ ] T004 Implement `/api/health` endpoint in `backend/app.py`
- [ ] T005 Create `backend/requirements.txt` with `Flask` and `Flask-Cors`
- [ ] T006 Write and pass unit tests for basic Flask setup and `/api/health` in `backend/test_app.py`

### Phase 3: User Story 1 (Core Arithmetic Operations - P1)

**Goal**: As a user, I want to perform basic arithmetic operations (add, subtract, multiply, divide) and handle division by zero.

**Acceptance Criteria**:
- Successfully perform addition, subtraction, multiplication, and division of two numbers.
- Receive an appropriate error message when attempting to divide by zero.

- [ ] T007 [US1] Implement `add` operation in `/api/calc` in `backend/app.py`
- [ ] T008 [US1] Implement `subtract` operation in `/api/calc` in `backend/app.py`
- [ ] T009 [US1] Implement `multiply` operation in `/api/calc` in `backend/app.py`
- [ ] T010 [US1] Implement `divide` operation with divide-by-zero validation in `/api/calc` in `backend/app.py`
- [ ] T011 [US1] Add and pass unit tests for `add`, `subtract`, `multiply`, `divide`, and divide-by-zero in `backend/test_app.py`

### Phase 4: User Story 2 (Additional Arithmetic Operations - P1)

**Goal**: As a user, I want to perform modulo and power operations.

**Acceptance Criteria**:
- Successfully perform modulo operation for two numbers.
- Successfully perform power operation for two numbers.

- [ ] T012 [US2] Implement `modulo` operation with modulo-by-zero validation in `/api/calc` in `backend/app.py`
- [ ] T013 [US2] Implement `power` operation in `/api/calc` in `backend/app.py`
- [ ] T014 [US2] Add and pass unit tests for `modulo` and `power` in `backend/test_app.py`

### Phase 5: User Story 3 (Calculator UI & Basic Interaction - P2)

**Goal**: As a user, I want a clear calculator interface with functional number and operator buttons, and a clear button to reset input.

**Acceptance Criteria**:
- Calculator UI displays numbers and operators correctly.
- Clicking number buttons appends digits to the display.
- Clicking operator buttons sets the operation and prepares for the second operand.
- Clicking "=" sends calculation to backend and displays result or error.
- Clicking "C" clears the display and resets the calculator state.

- [ ] T015 [US3] Create basic HTML structure for calculator in `frontend/index.html`
- [ ] T016 [US3] Apply basic styling to calculator in `frontend/styles.css`
- [ ] T017 [US3] Implement JavaScript to handle number button clicks and update display in `frontend/app.js`
- [ ] T018 [US3] Implement JavaScript to handle operator button clicks and store operation/operands in `frontend/app.js`
- [ ] T019 [US3] Implement JavaScript to send calculation request to backend on `=` click and update display with result/error in `frontend/app.js`
- [ ] T020 [US3] Implement clear button functionality in `frontend/app.js`

### Phase 6: User Story 4 (Calculation History - P2)

**Goal**: As a user, I want to see a history of my last 10 calculations.

**Acceptance Criteria**:
- The history section displays the last 10 performed calculations.
- New calculations are added to the top of the history list, and old ones are removed if the list exceeds 10 items.

- [ ] T021 [US4] Implement JavaScript to store and display last 10 calculations in `frontend/app.js`

### Phase 7: User Story 5 (API Health Check & Robustness - P3)

**Goal**: As a user, I want the backend API to be robust against invalid inputs and the frontend to handle network issues gracefully.

**Acceptance Criteria**:
- Backend `/api/calc` returns a 400 error and a user-friendly message for missing parameters or non-numeric inputs.
- Frontend displays a "Network or server issue" error if the backend API is unreachable.

- [ ] T022 [US5] Ensure backend `api/calc` handles missing/invalid numeric parameters gracefully in `backend/app.py`
- [ ] T023 [US5] Ensure frontend handles network/server errors gracefully in `frontend/app.js`
- [ ] T024 [US5] Add and pass unit tests for invalid parameter handling in `backend/test_app.py`

### Final Phase: Polish & Cross-Cutting Concerns

- [ ] T025 Update `README.md` with comprehensive setup, run, and usage instructions
