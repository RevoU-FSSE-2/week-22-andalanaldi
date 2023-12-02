import { CategoryForm as CategoryFormProps, Category  } from "../../types"
import { CategoryForm } from "../../components"
import { useNavigate, useParams } from "react-router-dom"
import { useCallback, useEffect, useState } from "react";
import { headers } from '../../types';
// import { getAuthHeaders } from '../../types';
import { BASE_URL } from '../../config/config';

const ProductNew = () => {

    const navigate = useNavigate()
    const [category, setCategory] = useState<Category>()

    const { id } = useParams();
    
    const token = localStorage.getItem('token');
    console.log("token:", token);

    const getCategory = useCallback(
        async () => {
            const fetching = await fetch(`${BASE_URL}/ipo`, {headers})
            const response: Category = await fetching.json();
            console.log(response);
            setCategory(response)
        },
        []
        //id
    )

    useEffect(
        () => {
            getCategory()
        },
        [getCategory]
    )

    const onSubmit = async (values: CategoryFormProps) => {
        try {

            const productAdd : Category = {
                _id : id,
                clientid : values.clientid,
                tickercode: values.tickercode,
                purpose: values.purpose,
                outstanding: values.outstanding,
                status : values.status,
                priority: values.priority,
                deadline: values.deadline
            }

            const token = localStorage.getItem('token');
            console.log("token:", token);

            // const authHeaders = getAuthHeaders();
            const fetching = await fetch(`${BASE_URL}/ipo/new`, {
                method: 'POST',
                headers: 
                { 
                    // ...authHeaders,
                    'Content-Type': 'application/json', 
                    Authorization: `Bearer ${token}`
                    // 'authToken'
                    // eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImM5OTNlMmU3LWRiMzMtNGY3Mi04N2IzLWU4ODFhYjdkZjNlYSIsImlhdCI6MTY5NTczMzgwNiwiZXhwIjoxNjk1NzU1NDA2fQ.mJuCVBzjiHmjKtE-V623lQ2FVg4vTRYeqzBmELadgUk
                },
                body: JSON.stringify(
                    productAdd
                    ),
            })
            const response = await fetching.json();
            console.log(response);
            navigate('/product')
        } catch (error) {
            alert(error)
        }
    }

    return (
        <CategoryForm onSubmit={onSubmit} category={category}/>
    )
}

export default ProductNew