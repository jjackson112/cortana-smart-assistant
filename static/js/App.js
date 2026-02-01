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
    }
}