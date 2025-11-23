# **Software Design Document (SDD)**
## **CPSC Help Desk – MVP Release #1**
### Team Tsunamis – Fall 2025

---

# **1. Introduction**
The CPSC Help Desk application provides Xavier students with quick access to essential academic information.  
For the MVP (Release #1), two core features are implemented:

1. A **Drop Deadline Checker**, which retrieves and displays the last day to drop a course using scraped academic calendar data.
2. A **GPA Calculator**, which allows students to enter grades and credit hours and receive an accurate GPA.

This document describes the overall system design, modules, classes, data flow, use cases, and test plan.

---

# **2. System Overview**
The system provides simple CLI-based tools to support two student-facing functions:

### **Feature 1: Drop Deadline Checker**
- Scrapes academic calendar dates
- Returns the last day to drop a course for the active semester
- Displays the information in a clean text format

### **Feature 2: GPA Calculator**
- Accepts multiple courses
- Converts letter grades to quality points
- Calculates weighted GPA
- Includes validation + error handling
- Includes automated unit tests

---

# **3. System Architecture**

### **3.1 Modules**
| Module | Description |
|--------|-------------|
| `PerformScraping.py` | Scrapes the university academic calendar and returns drop deadlines |
| `gpa_calculator.py` | Contains GPA logic, error handling, conversion functions, and unit tests |
| `driver.py` | Provides a simple menu so students can run Help Desk features |
| `Course.py` (optional) | Represents a course with attributes such as name, number, and semester |

---

### **3.2 Architecture Diagram**

```
+------------------+
|   driver.py      |
+------------------+
       |    |
       |    +------------------------------+
       v                                   v
+-----------------+                +---------------------+
| PerformScraping | ---> data ---> | Drop Deadline Logic |
+-----------------+                +---------------------+
       |
       v
+-----------------+
| gpa_calculator  |
+-----------------+
       |
       v
+-----------------+
| GPA Computation |
+-----------------+
```

---

# **4. User Stories (MVP)**

### **4.1 User Story 1 — Drop Deadline**
**As a student, I want the app to tell me the last day to drop a course so that I don’t miss deadlines.**

### **4.2 User Story 2 — GPA Calculator**
**As a student, I want the app to calculate my GPA so that I understand my academic standing.**

---

# **5. Use Cases**

## **5.1 Use Case: Check Drop Deadline**
**Actor:** Student  
**Preconditions:**
- App is open  
- Scraped calendar data is stored  

**Main Flow:**
1. Student opens the drop deadline page  
2. Student selects the semester  
3. System retrieves the correct drop deadline  
4. System displays the date  

**Exception Flows:**
- If semester not found → System shows “Semester not available”
- If scraping fails → System shows error message  

---

## **5.2 Use Case: GPA Calculator**
**Actor:** Student  
**Preconditions:**
- Student has opened GPA calculator  
- Grade scale is defined  

**Main Flow:**
1. Student enters grade  
2. Student enters credit hours  
3. System validates inputs  
4. System converts letter grade → quality points  
5. System calculates weighted GPA  
6. System displays final GPA  

**Exception Flows:**
- Invalid grade → System rejects it  
- Missing credit hours → Error  
- Total hours = 0 → Cannot compute GPA  

---

# **6. Class & Function Design**

## **6.1 Class: Course**
```
Course
- name: str
- course_number: str
- semester_offered: str
```

## **6.2 GPA Module (`gpa_calculator.py`)**

### Functions:
- `convert_grade_to_points(grade)`
- `calculate_gpa(grades, credit_hours)`
- `run_gpa_calculator()` — interactive CLI
- `TestGpaCalculator` — unit test class

---

# **7. Sequence Diagram (GPA Calculation)**

```
Student → UI: enter grade
UI → Validator: validate grade
Validator → GPA Calculator: convert grade
GPA Calculator → GPA Calculator: sum weights
GPA Calculator → UI: return final GPA
UI → Student: display "Your GPA is 3.64"
```

---

# **8. Data Design**
### **Grade Scale**
| Letter | Points |
|--------|---------|
| A | 4.0 |
| B | 3.0 |
| C | 2.0 |
| D | 1.0 |
| F | 0.0 |

---

# **9. Test Plan**

### Unit tests include:
- Single-course GPA  
- Multi-course weighted GPA  
- Invalid grade (“Z”)  
- Missing/zero credit hours  
- Mismatched list lengths  
- Empty input validation  

All unit tests are implemented using Python’s built-in `unittest`.

---

# **10. File Structure**

```
Tsunamis/
│
├── SDD/
│   └── SDD.md
│
├── cpsc-help-desk/
│   ├── gpa_calculator.py
│   ├── PerformScraping.py
│   ├── driver.py
│   └── Course.py
│
├── README.md
└── ...
```

---

# **11. Release Notes (Release #1 – MVP)**

### **Completed**
- GPA Calculator implemented  
- Drop deadline function implemented  
- Unit tests added  
- Trello user stories + use cases completed  
- SDD created and uploaded  

### **Next Release Goals**
- Add CRN lookup  
- Add schedule planner  
- Add UI (web or mobile)

---

# **End of Document**
