import { useState } from "react";
{/* User Interaction */}

export default function MainPanel({ onCommand, fsmResponse }) {
    const [mode, setMode] = useState("");
    const [command, setCommand] = useState("");

    function handleSubmit(e) {
      e.preventDefault();
      if(!command.trim()) return;

      onCommand({ commandText: command }); // send correct object wrapped 
      setCommand("");
    }

    function handleModeChange(e) {
        const selectedMode = e.target.value.toLowerCase();

        setMode(selectedMode);
        setCommand("") // reset input when switching modes

        // single call to backend to set mode + trigger initial prompt
        // wrap in object so handleUserCommand receives { commandText }
        onCommand({ commandText: selectedMode });
    }

    return (
        <section>
            <div className="text-3xl font-bold text-center m-3">
                <h1>Cortana</h1>
            </div>
            
            <div className="p-6 min-h-[100px]">
                {Array.isArray(fsmResponse) && fsmResponse.length > 0 ? (
                    fsmResponse.map((msg, i) => 
                        <p key={i} className="mb-2">{msg}</p>)
                    ) : (
                        <p className="text-400 font-semibold mr-3 mb-4">Hi Jasmine, I'm Cortana! <br />Awaiting commands...</p>
                    )}
            </div>

            {/* Mode Selection - Dropdown */}
            <div className="mode-selection p-6">
                <label htmlFor="modes" className="text-2xl font-semibold mr-3">Choose a mode:</label>
                <select value={mode} onChange={handleModeChange} className="outline rounded-lg text-center">
                    <option value="choose">Select a mode</option>
                    <option value="contacts">Contact List</option>
                    <option value="inventory">Inventory</option>
                    <option value="schedule">Schedule</option>
                    <option value="todo">To Do List</option>
                </select>
            </div>

            {/* Reiterate the commands once the mode is selected*/}
            {mode === "contacts" && (
                <div className="px-6 text-sm text-gray-500">
                    Commands: add • search • update • delete • main menu
                </div>
            )}

            {mode === "inventory" && (
                <div className="px-6 text-sm text-gray-500">
                    Commands: remember • list • search • update • delete • main menu
                </div>
            )}

            {mode === "schedule" && (
                <div className="">
                    Commands: add • list • search • update • delete • main menu
                </div>
            )}

            {mode === "todo" && (
                <div className="px-6 text-sm text-gray-500">
                    Commands: add • list • update • delete • main menu
                </div>
            )}
            
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
