import { useMemo } from 'react';
import { Navigate, Outlet, useLocation } from 'react-router-dom'
import { Navbar } from '../../components';

const PublicLayout = () => {

    const token = localStorage.getItem('token');

    const location = useLocation();

    const isAuth = useMemo(
        () => {
            if(location.pathname) {
                return !!token
            }
            
        },
        [location.pathname, token]
    )

    if(isAuth) {
        return (
            <div>
                <Navbar />
                <Outlet />
                <div>Footer</div>
            </div>
        )
    }

    return <Navigate to="/login" />
}

export default PublicLayout