import ActivityItem from "./ActivityItem"
/*array data model */

export default function ActivityList({ activities }) {
  // Show only most recent 8 activity logs 
  const displayActivities = [...activities].slice(-8).reverse();

  if (!activities.length) {
    return <p>No activity yet.</p>
  }

  return (
    <ul className="activity-list">
      {displayActivities.map((activity) => (
        <ActivityItem key={activity.id} activity={activity} />
      ))}
    </ul>
  )
}
