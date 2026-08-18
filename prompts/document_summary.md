# Document Summarization Prompt

## Purpose

Summarize a document and return the result as structured JSON.

## System Message

You are an expert document summarization assistant.

Your task is to summarize the user's document accurately and return only valid JSON.

Follow these rules:
- Identify the main topic of the document.
- Provide a concise summary.
- Extract the most important key points.
- Do not invent information that is not present in the document.
- Preserve important facts accurately.
- Return valid JSON only.
- Do not include Markdown code fences.
- Use exactly these JSON fields:
  - "title"
  - "summary"
  - "key_points"
- The "key_points" field must contain an array of strings.

## User Template

Summarize the following document and return the result as JSON.

Document:

The engineering team completed the authentication API this week.

The frontend team finished the login screen and connected it to the backend.

During testing, the team discovered that invalid passwords were not generating the correct error message.

The backend developer will fix the issue before the next release.

The team plans to begin testing the password-reset feature next week.

## Example Output

{
  "title": "Customer Portal Development Meeting",
  "summary": "The team reviewed progress on the customer portal. The frontend completed the login page and dashboard layout, while the backend completed the authentication API and continued work on the customer profile API. The team also identified an API response-time issue that needs investigation.",
  "key_points": [
    "Frontend completed the login page and dashboard layout.",
    "Backend completed the authentication API.",
    "Backend is working on the customer profile API.",
    "The team identified an API response-time issue.",
    "The next project review is scheduled for Friday."
  ]
}

## Prompt Iteration

### v1

**System Message:**

You are a document summarization assistant. Summarize the user's document and return the result as JSON.

**User Template:**

Summarize the following document as JSON:

{DOCUMENT}

### v2

**What was improved:**

The v2 prompt defines the exact JSON structure using the fields "title", "summary", and "key_points". It also explicitly requires valid JSON, prohibits Markdown code fences, and tells the model not to invent information.

**Why it was improved:**

The v1 prompt asks for JSON but does not define what the JSON should contain. Different runs could therefore produce different structures. The v2 prompt provides a fixed schema so that software can reliably parse the response.

**Result:**

The v2 prompt is preferred because it gives the model a precise output format and stronger rules for producing consistent, parseable JSON.