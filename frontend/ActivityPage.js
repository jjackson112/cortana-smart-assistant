import { useEffect, useState } from "react"
import ActivityList from "./ActivityList"

export default function ActivityPage() {
  const [activities, setActivities] = useState([])

  useEffect(() => {
    fetch("/api/activity")
      .then(res => res.json())
      .then(data => setActivities(data.data))
  }, [])

  return (
    <div>
      <h1>Activity</h1>
      <ActivityList activities={activities} />
    </div>
  )
}
