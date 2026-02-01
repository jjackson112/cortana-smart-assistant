import ActivityItem from "./ActivityItem"

export default function ActivityList({ activities }) {
  if (!activities.length) {
    return <p>No activity yet.</p>
  }

  return (
    <ul>
      {activities.map(a => (
        <ActivityItem key={a.id} activity={a} />
      ))}
    </ul>
  )
}
