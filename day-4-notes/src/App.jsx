import { useState } from "react";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);
  const [input, setInput] = useState("");

  function addNote() {
    const trimmedInput = input.trim();

    if (trimmedInput === "") {
      return;
    }

    const newNote = {
      id: Date.now(),
      text: trimmedInput,
    };

    setNotes((currentNotes) => [...currentNotes, newNote]);
    setInput("");
  }

  function deleteNote(id) {
    setNotes((currentNotes) =>
      currentNotes.filter((note) => note.id !== id)
    );
  }

  function handleKeyDown(event) {
    if (event.key === "Enter") {
      addNote();
    }
  }

  return (
    <div className="app">
      <div className="notes-container">
        <h1>My Notes</h1>

        <div className="input-section">
          <input
            type="text"
            placeholder="Enter your note..."
            value={input}
            onChange={(event) => setInput(event.target.value)}
            onKeyDown={handleKeyDown}
          />

          <button onClick={addNote}>Add</button>
        </div>

        <div className="notes-list">
          {notes.length === 0 ? (
            <p className="empty-message">
              No notes yet. Add your first note!
            </p>
          ) : (
            notes.map((note, index) => (
              <div className="note" key={note.id}>
                <div className="note-content">
                  <span className="note-number">{index + 1}.</span>
                  <span>{note.text}</span>
                </div>

                <button
                  className="delete-button"
                  onClick={() => deleteNote(note.id)}
                >
                  Delete
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;