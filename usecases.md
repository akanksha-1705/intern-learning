# 10 AI Use Cases in Engineering

## 1. AI Code Generation and Refactoring

**Description:** AI can generate new code from a natural-language requirement and improve or refactor existing code.

**AI capability:** Code

**Input → Output:**
- **Input:** A requirement such as "Create a Python function that validates an email address."
- **Output:** A Python function that validates email addresses, along with suggested improvements and edge cases.

**Internship-domain relevance:** Yes

---

## 2. Automated Code Review

**Description:** AI can review source code and identify bugs, security problems, style issues, and maintainability concerns.

**AI capability:** Code

**Input → Output:**
- **Input:** A pull request containing modified Python files.
- **Output:** Review comments identifying potential problems, their severity, and suggested code changes.

**Internship-domain relevance:** Yes

---

## 3. Bug and Incident Log Analysis

**Description:** AI can analyze application logs and error messages to identify likely causes of software failures.

**AI capability:** Text

**Input → Output:**
- **Input:** An application log containing HTTP 500 errors, timestamps, stack traces, and database errors.
- **Output:** A list of probable causes, relevant log entries, and recommended debugging steps.

**Internship-domain relevance:** No

---

## 4. Technical Documentation Generation

**Description:** AI can generate technical documentation from source code, APIs, and project configuration.

**AI capability:** Text

**Input → Output:**
- **Input:** A FastAPI project containing API routes, models, and Python functions.
- **Output:** Documentation describing endpoints, parameters, responses, and example API requests.

**Internship-domain relevance:** Yes

---

## 5. Automated Test-Case Generation

**Description:** AI can generate unit and integration tests from application code and functional requirements.

**AI capability:** Code

**Input → Output:**
- **Input:** A Python function that validates user registration data.
- **Output:** Pytest test cases covering valid input, invalid input, missing fields, and edge cases.

**Internship-domain relevance:** No

---

## 6. Requirements Extraction

**Description:** AI can extract structured requirements from unstructured project documents.

**AI capability:** Extraction

**Input → Output:**
- **Input:** A software requirements document containing several pages of functional and technical requirements.
- **Output:** A structured list of features, user roles, acceptance criteria, dependencies, and constraints.

**Internship-domain relevance:** No

---

## 7. UI and Accessibility Analysis

**Description:** AI vision models can inspect application screenshots and identify possible UI and accessibility problems.

**AI capability:** Vision

**Input → Output:**
- **Input:** A screenshot of a web application's login page.
- **Output:** Identified issues such as low contrast, unclear navigation, missing labels, or poorly aligned elements.

**Internship-domain relevance:** No

---

## 8. Engineering Knowledge Assistant

**Description:** An AI assistant can help engineers find information across technical documentation, repositories, and internal knowledge sources.

**AI capability:** Agent

**Input → Output:**
- **Input:** An engineer asks, "How do we configure authentication for the staging API?"
- **Output:** A step-by-step answer based on the relevant technical documentation and project files.

**Internship-domain relevance:** No

---

## 9. Customer Support Ticket Classification

**Description:** AI can classify incoming support requests and extract important information for engineering teams.

**AI capability:** Extraction

**Input → Output:**
- **Input:** A customer ticket saying that the application crashes when uploading a PDF larger than 10 MB.
- **Output:** Category = "File Upload", priority = "High", affected feature = "PDF Upload", and extracted reproduction details.

**Internship-domain relevance:** No

---

## 10. Deployment and DevOps Incident Assistant

**Description:** An AI agent can help engineers investigate failed builds and deployment incidents.

**AI capability:** Agent

**Input → Output:**
- **Input:** A failed CI/CD pipeline containing build logs, test failures, and deployment information.
- **Output:** A probable failure cause, the relevant failed steps, and suggested remediation actions.

**Internship-domain relevance:** No

---

# Use Case I Would Build First

## Engineering Knowledge Assistant

I would build the Engineering Knowledge Assistant first because it can help developers find answers quickly without manually searching through large amounts of technical documentation. It would also be a practical way to learn retrieval, LLMs, and agent-style workflows.

A first version could allow an engineer to ask a question and receive an answer based on the team's technical documentation and project files.