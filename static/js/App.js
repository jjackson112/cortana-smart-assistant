import { useState } from "react";
import MainPanel from "./MainPanel";
import SidePanel from "./SidePanel";

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
        ])

        const res = await fetch("/api/command", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ command })
        })
        const data = await res.json()

        setResponse(data.response)

        setActivities(prev => [
            ...prev,
            {
                id: crypto.randomUUID(),
                action: "Cortana replied",
                entity_type: "message",
                metadata: { name: data.response },
                timestamp: new Date().toISOString()
            }
        ])
    }

    return (
        <div className="layout">
            <MainPanel onCommand={handleUserCommand} />
            <SidePanel response={response} activities={activities} />
        </div>
    )
}