import ActivityList from "./ActivityList";

export default function SidePanel({ activities }) {
    return (
        <aside className="side-panel">
            {/* Cortana Response Area */}
            <div className="response-area">
                <h2 className="text-2xl font-semibold mb-2">Response</h2>
                <p className="text-cyan-400 font-semibold mb-4">Cortana is ready</p>
                <p id="cortana-reply"></p>
            </div>

            {/* Activity Log */}
            <div className="activity-log-area">
                <h2 className="text-xl font-semibold mb-2">Activity Log</h2>
                <ActivityList activities={activities}/> 
            </div>
        </aside>
    )
}