# Day 7 — Prompt Library

This folder contains the prompt library created for Assignment 7.

The prompts are designed to be reusable and include clear system instructions, user templates, placeholders, and example inputs and outputs.

## Prompts

### 1. Resume Bullet Generation

**File:** `resume_bullet.md`

Converts plain-text job history into concise, achievement-focused resume bullet points.

**Placeholder:**

`{JOB_HISTORY}`

---

### 2. Document Summarization

**File:** `document_summary.md`

Summarizes a document and returns the result as structured JSON.

**Placeholder:**

`{DOCUMENT}`

**JSON fields:**

- `title`
- `summary`
- `key_points`

The prompt was tested three consecutive times to verify that it produces valid JSON output.

---

### 3. Action Item Extraction

**File:** `action_items.md`

Extracts actionable tasks from meeting notes and identifies the owner and deadline when they are provided.

**Placeholder:**

`{MEETING_NOTES}`

**Output fields:**

- `task`
- `owner`
- `deadline`

---

### 4. Error Message Rewriting

**File:** `error_rewrite.md`

Rewrites technical software error messages into simple, friendly messages that are understandable to end users.

**Placeholder:**

`{ERROR_MESSAGE}`

---

### 5. Code Review Assistant

**File:** `code_review.md`

Reviews software code for important bugs and improvement opportunities and returns a structured review.

**Placeholder:**

`{CODE}`

**Output fields:**

- `issues`
- `overall_assessment`

Each issue contains:

- `problem`
- `why_it_matters`
- `suggestion`

## Prompt Design

Each prompt contains:

- Purpose
- System Message
- User Template
- Placeholder
- Example Input
- Example Output

The first two prompts also contain a v1 → v2 iteration note explaining how the prompts were improved.

## Testing

All five prompts were tested with example inputs.

The document summarization prompt was tested three consecutive times to verify that its output remained valid JSON.