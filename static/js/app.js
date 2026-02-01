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
}
