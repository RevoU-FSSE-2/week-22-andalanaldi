import { Outlet } from "react-router-dom"

const AnotherLayout = () => {

    return (
        <div>
            <div>Another Layout</div>
            <Outlet/>
        </div>
    )
}

export default AnotherLayout