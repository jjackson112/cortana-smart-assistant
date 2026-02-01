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
    <section className="main-panel grid grid-cols-[2fr_1fr] h-screen">
        <div className="ext-3xl font-bold text-center m-3">
            <h1>Cortana</h1>
        </div>

        {/* Dropdown */}
        <div className="mode-selection">
            <select id="modes" class="outline rounded-lg text-center">
                <option value="" disabled selected></option>
                <option value="contacts">Contact List</option>
                <option value="inventory">Inventory</option>
                <option value="schedule">Schedule</option>
                <option value="to-do">To Do List</option>
                <option value="exit">Exit</option>
            </select>
            <button 
                onClick={handleSubmit}
                className="bg-cyan-500 hover:bg-cyan-700 text-white font-semibold py-2 px-3 ml-3 rounded-full"
                >
                Enter</button>
        </div>

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
