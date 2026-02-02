import ActivityItem from "./ActivityItem"
/*array data model */

export default function ActivityList({ activities }) {
  if (!activities.length) {
    return <p>No activity yet.</p>
  }

  return (
    <ul className="activity-list">
      {activities.map(a => (
        <ActivityItem key={a.id} activity={a} />
      ))}
    </ul>
  )
}
