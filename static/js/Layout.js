import MainPanel from "./MainPanel";
import SidePanel from "./SidePanel";

function Layout () {
    return (
        <div className="app-layout" style={{ display: "flex", height: "100vh" }}>
            <div style={{ flex: 2 }}>{MainPanel}</div>
            <div style={{ flex: 1 }}>{SidePanel}</div>
        </div>
    )
}