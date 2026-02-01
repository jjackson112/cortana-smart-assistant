import { useState } from "react";

export default function MainPanel({ onCommand }) {
    const [mode, setMode] = useState(null);
    const [command, setCommand] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    onCommand(command);
    setCommand("");
  }

  return (
    <section className="main-panel">
      <h1>Cortana</h1>

      <form onSubmit={handleSubmit}>
        <input
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          placeholder="Enter command here..."
        />
        <button type="submit">Enter</button>
      </form>
    </section>
  );
}
