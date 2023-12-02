import { RegisForm as RegisFormProps, RegisResponse } from "../../types"
//Regis
import { RegisForm } from "../../components"
import { BASE_URL } from '../../config/config';

const Regis = () => {

    const onSubmit = async (data: RegisFormProps) => {
        const fetching = await fetch(`${BASE_URL}/auth/register`, {
            //'https://mock-api.arikmpt.com/api/user/register'
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        const response: RegisResponse = await fetching.json()
        if(response) {
            localStorage.setItem('insertedId', response.data.insertedId)
            window.location.replace('/login')
        }
    }

    return (
        <RegisForm onSubmit={onSubmit}/>
    )
}

export default Regis