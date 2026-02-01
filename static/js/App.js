import { useState } from "react";
import SidePanel from "./SidePanel";
import MainPanel from "./MainPanel";

export default function App() {
    const [response, setResponse] = useState("Cortana is ready");
    const [activities, setActivities] = useState([]);

    async function handleUserCommand(command) {
        setActivities(prev => [
            ...prev,
            {
                id: Date.now(),
                action: "user executed",
                entity_type: "command",
                metadata: { name: command },
                timestamp: new Date().toISOString()
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
                id: Date.now() + 1,
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