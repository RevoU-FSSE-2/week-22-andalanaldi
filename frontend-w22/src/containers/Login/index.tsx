import { LoginForm as LoginFormProps, LoginResponse2 } from "../../types"
import { LoginForm } from "../../components"
import { BASE_URL } from '../../config/config';

const Login = () => {

    const onSubmit = async (data: LoginFormProps) => {
        const fetching = await fetch(`${BASE_URL}/auth/login`, {
            //'https://mock-api.arikmpt.com/api/user/login'
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }) // ini berhasil
        const response: LoginResponse2 = await fetching.json() // bakal gagal -> response = null, solusi ?
        if(fetching.ok) {
            //response
            localStorage.setItem('token', response.data)
        //     // 'token'
        //     // eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM5OTNlMmU3LWRiMzMtNGY3Mi04N2IzLWU4ODFhYjdkZjNlYSIsImlhdCI6MTY5NTczMzgwNiwiZXhwIjoxNjk1NzU1NDA2fQ.mJuCVBzjiHmjKtE-V623lQ2FVg4vTRYeqzBmELadgUk
            window.location.replace('/') 
        // } those part above is for advance assignment, a part below is for intermediate assignment 
        // if (fetching.ok) {
        //     // localStorage.setItem('token', response.data.token)
        //     window.location.replace('/')
        }
        fetching.status
    }

    return (
        <LoginForm onSubmit={onSubmit}/>
    )
}

export default Login
// const onSubmit = async (data: LoginFormProps) => {
//     try {
//         const fetching = await fetch(`${BASE_URL}/auth/login`, {
//             //'https://mock-api.arikmpt.com/api/user/login'
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(data)
//         }); // ini berhasil
//         if (fetching.ok) {
//             const response: LoginResponse2 = await fetching.json();
//             localStorage.setItem('token', response.data.token);
//             window.location.replace('/');
//         } else {
//             const errorData = await fetching.json(); // You can parse error response here
//             console.error('Login failed:', errorData);
//             // fetching.status
//         }
//     } catch (error) {
//         console.error('An error occurred during login:', error);
//     }
// };

// const Login = () => {
//     return (
//         <LoginForm onSubmit={onSubmit} />
//     );
// };

// export default Login;
