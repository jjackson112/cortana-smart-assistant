function formatActivity({ action, entity_type, metadata }) {
  if (metadata?.name) {
    return `${action} ${entity_type}: ${metadata.name}`
  }
  return `${action} ${entity_type}`
}

export default function ActivityItem({ activity }) {
  return (
    <li>
      <strong>{formatActivity(activity)}</strong>
      <div>
        {new Date(activity.timestamp).toLocaleString()}
      </div>
    </li>
  )
}
