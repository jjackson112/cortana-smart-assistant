import { useState } from "react";

const [activities, setActivities] = useState([])
const [response, setResponse] = useState("Cortana is ready")

async function handleUserCommand(command) {
    setActivities(prev => [
        ...prev, 
        {
            id: Date.now(),
            action: "user executed",
            entity_type: "command",
            metadata: {name: command},
            timestamp: new Date().toISOString
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
            timestamp: newDate().toISOString
        }
    ])
}
