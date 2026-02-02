import { useState } from "react";
import SidePanel from "./components/SidePanel";
import MainPanel from "./components/MainPanel";
{/* Hold state and pass props down - Structure */}

export default function App() {
  const [response, setResponse] = useState("Cortana is ready");
  const [activities, setActivities] = useState([]);

  async function handleUserCommand({ mode, command }) {
    const timestamp = new Date().toISOString();

    setActivities(prev => [
      ...prev,
      {
        id: crypto.randomUUID(),
        action: "user executed",
        entity_type: "command",
        metadata: { mode, command },
        timestamp
      }
    ]);

    try {
      const res = await fetch("/api/command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mode, command })
      });

      const data = await res.json();

      setResponse(data.response);

      setActivities(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          action: "Cortana replied",
          entity_type: "message",
          metadata: { message: data.response },
          timestamp: new Date().toISOString()
        }
      ]);
    } catch (err) {
      setResponse("Something went wrong.");

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
            <MainPanel onCommand={handleUserCommand} />
            <SidePanel response={response} activities={activities} />
        </div>
    )
}