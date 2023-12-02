import { Menu } from 'antd';
import type { MenuProps } from 'antd';
import { useNavigate } from 'react-router-dom';

const items: MenuProps['items'] = [
    {
        label: 'Home',
        key: '/'
    },
    {
        label: 'ToDoList',
        key: '/product'
    },
    {
        label: 'ClientProfile',
        key: '/profile'
    },
    {
        label: 'Log Out',
        key: '/login'
    },
]

const Navbar = () => {

    const navigate = useNavigate();

    const onClick: MenuProps['onClick'] = (e) => {
        navigate(e.key)
    };

    return (
        <Menu onClick={onClick} items={items} mode={'horizontal'}/>
    )
}

export default Navbar