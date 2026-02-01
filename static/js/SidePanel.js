import ActivityList from "./ActivityList";

export default function SidePanel({ response, activities }) {
    return (
        <aside className="side-panel">
            {/* Cortana Response Area */}
            <div className="response-area">
                <h2 className="text-2xl font-semibold mb-2">Response</h2>
                <p className="cortana-reply text-cyan-400 font-semibold mb-4">{response || "Cortana is ready"}</p>
            </div>

            {/* Activity Log */}
            <div className="activity-log-area">
                <h2 className="text-xl font-semibold mb-2">Activity Log</h2>
                <ActivityList activities={activities || []} /> 
            </div>
        </aside>
    )
}