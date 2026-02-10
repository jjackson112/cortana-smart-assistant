import { useState, useEffect } from "react";
{/* User Interaction */}

export default function MainPanel({ onCommand }) {
    const [mode, setMode] = useState(null);
    const [command, setCommand] = useState("");

    useEffect(() => {
        if( mode === "to-do") {
            onCommand("", mode);
        }
    }, [mode]);

    function handleSubmit(e) {
      e.preventDefault();
      if(!command.trim()) return;

      onCommand(command);
      setCommand("");
    }

    return (
        <section>
            <div className="text-3xl font-bold text-center m-3">
                <h1>Cortana</h1>
            </div>

            {/* Mode Selection - Dropdown */}
            <div className="mode-selection p-6">
                <label htmlFor="modes" className="text-2xl font-semibold mr-3">Choose a mode:</label>
                <select value={mode || ""} onChange={(e) => setMode(e.target.value)} className="outline rounded-lg text-center">
                    <option value="choose">Select a mode</option>
                    <option value="contacts">Contact List</option>
                    <option value="inventory">Inventory</option>
                    <option value="schedule">Schedule</option>
                    <option value="to-do">To Do List</option>
                </select>
            </div>
            {/* Command input appears ONLY after mode selection */}
            {mode && (
                <form onSubmit={handleSubmit} className="flex gap-2 p-6">
                    <input
                        value={command}
                        onChange={(e) => setCommand(e.target.value)}
                        placeholder={`Enter ${mode} command...`}
                        className="border rounded px-3 py-2"
                    />
                    <button
                      type="submit"
                      disabled={!command.trim()}
                      className="bg-cyan-500 hover:bg-cyan-700 text-white font-semibold px-4 rounded-full"
                    >
                        Enter
                    </button>
                </form>
            )}
        </section>
  );    
}   
