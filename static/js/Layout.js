import MainPanel from "./MainPanel";
import SidePanel from "./SidePanel";

function Layout () => {
    return (
        <div className="grid grid-cols-[2fr_1fr] h-screen">
            <MainPanel />
            <SidePanel />
        </div>
    )
}