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
    }
}