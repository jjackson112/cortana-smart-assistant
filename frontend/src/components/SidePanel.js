import ActivityList from "./ActivityList";
{/* Output */}

export default function SidePanel({ semanticResponse = [], activities = [] }) {
  // Decide what to display in the response area
  const displayMessages = semanticResponse.length > 0 ? semanticResponse : ["Cortana is ready"];

  return (
    <aside className="side-panel bg-slate-50 p-4 h-full flex flex-col">
      
      {/* Semantic Memory / Cortana Response Area */}
      <div className="response-area mb-6">
        <h2 className="text-2xl font-semibold mb-2">Response</h2>
        <div className="cortana-reply text-cyan-400 font-semibold space-y-1">
          {displayMessages.map((msg, i) => (
            <p key={i}>{msg}</p>
          ))}
        </div>
      </div>

      {/* Activity Log */}
      <div className="activity-log-area flex-1 overflow-y-auto">
        <h2 className="text-xl font-semibold mb-2">Activity Log</h2>
        <ActivityList activities={activities} /> 
      </div>
    </aside>
  );
}