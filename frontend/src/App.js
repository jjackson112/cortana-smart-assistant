import { useState, useEffect } from "react";
import SidePanel from "./components/SidePanel";
import MainPanel from "./components/MainPanel";
{/* Hold state and pass props down - Structure */}

// Helper to normalize API responses into arrays
const normalizeToArray = (val) => (Array.isArray(val) ? val : val ? [val] : []);

export default function App() {
  const [semanticResponse, setSemanticResponse] = useState([]); // semantic memory
  const [activities, setActivities] = useState([]); // activity log
  const [commands, setCommands] = useState([]);
  const [fsmState, setFsmState] = useState({ mode:null, state: null });
  const [fsmResponse, setFsmResponse] = useState([]); // FSM logic
  
  const API_BASE = "https://cortana-ahop.onrender.com";

  useEffect(() => {
  const timestamp = new Date().toISOString();
    setActivities([
      {
        id: crypto.randomUUID(),
        action: "system ready",
        entity_type: "system",
        metadata: { message: "Cortana is ready" },
        timestamp
      }
    ]);
  }, []);

  // Semantic Memory
  async function handleSemanticMemory(userInput) {
    const timestamp = new Date().toISOString();
    try {
      const res = await fetch(`${API_BASE}/api/semantic`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userInput })
      });
      const data = await res.json();

      const semantic = normalizeToArray(data.response);
      setSemanticResponse(semantic);
      setCommands(data.commands || []);

      setActivities(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          action: "semantic memory replied",
          entity_type: "message",
          metadata: { message: semantic },
          timestamp
        }
      ]);
    } catch (err) {
      setSemanticResponse("Failed semantic memory")

      setActivities(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          action: "error",
          entity_type: "message",
          metadata: { message: err.message },
          timestamp
        }
      ]);
    }
  }

  // FSM assistant logic
  async function handleUserCommand({ commandText }) {
    const timestamp = new Date().toISOString();

    setActivities(prev => [
      ...prev,
      {
        id: crypto.randomUUID(),
        action: "user executed",
        entity_type: "command",
        metadata: { command: commandText },
        timestamp
      }
    ]);

    try {
      // auto-detect if the commandText is a mode name
      const modeNames = ["contacts", "inventory", "schedule", "todo"];
      let payload;

      if (modeNames.includes(commandText.toLowerCase())) {
        // initialize mode if user typed mode name
        payload = { input_text: commandText.toLowerCase(), state: { mode: null, state: null } };
      } else {
        // otherwise use current FSM state
        payload = { input_text: commandText, state: fsmState };
      }

      const res = await fetch(`${API_BASE}/api/assistant`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      setFsmState(data.state); // FSM state updated

      // update commands if they exist
      if (data.commands) {
        setCommands(normalizeToArray(data.commands));
      }

      // Merge messages and response if both exist
      const mergedResponse = [
        ...normalizeToArray(data.messages),
        ...normalizeToArray(data.response),
      ];
      setFsmResponse(mergedResponse);

      setActivities(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          action: "Cortana replied",
          entity_type: "message",
          metadata: { message: mergedResponse },
          timestamp: new Date().toISOString()
        }
      ]);
    } catch (err) {
      setFsmResponse("Something went wrong.");

      setActivities(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          action: "error",
          entity_type: "system",
          metadata: { message: err.message },
          timestamp: new Date().toISOString()
        }
      ]);
    }
}

    return (
        <div className="grid grid-cols-[2fr_1fr] h-screen">
            {/* MainPanel shows FSM replies and commands */}
            <MainPanel onCommand={handleUserCommand} commands={commands} fsmResponse={fsmResponse} />
            
            {/* SidePanel shows unified activity log and semantic memory */}
            <SidePanel semanticResponse={semanticResponse} handleSemanticMemory={handleSemanticMemory} activities={activities} />
        </div>
    )
}