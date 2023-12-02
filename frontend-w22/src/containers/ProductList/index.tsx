import { ColumnsType } from 'antd/es/table';
import { useEffect, useState  } from 'react';
//useRef
import { ProductList as ProductListComponent } from '../../components'
import { GetCategoryResponse, headers, Category } from '../../types';
//headers, getAuthHeaders,
import { Button } from 'antd'
import { useNavigate } from 'react-router-dom';
import { BASE_URL } from '../../config/config';

const ProductList = () => {

    const [categories, setCategories] = useState<Category[]>([]);
    const navigate = useNavigate();
    
    const getCategoryList = async () => {
        // const authHeaders = getAuthHeaders();
        const token = localStorage.getItem('token');
        console.log("token:", token);
        try {
            const fetching = await fetch(`${BASE_URL}/ipo`, {headers})
            // `https://mock-api.arikmpt.com/api/category`
            // headers: {  
            //     'Content-Type': 'application/json', 
            //     Authorization: `Bearer ${'token'}`
            // },
            const response: GetCategoryResponse = await fetching.json();
            setCategories(response.data ?? []); 
        } catch (error) {
            alert(error);
        }
    }


    // Create a ref for handleNavigate
    // const handleNavigateRef = useRef<(path: string) => void>((path: string) => {
    //     navigate(path);
    // });

    // Extract the function from the ref
    // const handleNavigate = handleNavigateRef.current;

    useEffect(
        () => {
            getCategoryList()
        }, 
        []
    )

    // useEffect(() => {

        // const token = localStorage.getItem('authToken');
        // if(!token) {
        //     handleNavigate('/Product'); 
        //     return;
        // }
        //     getCategoryList();
        // }, [handleNavigate]);

    const removeProduct = async (id: string | undefined) => {
        try {
            const token = localStorage.getItem('token');
            console.log("token:", token);
            const fetching = await fetch(`${BASE_URL}/ipo/delete/${id}`, {
                method: 'DELETE',
                headers: { 
                //     'Content-Type': 'application/json', 
                    Authorization: `Bearer ${token}`
                //     // 'authToken'
                // 34506582-54ef-4997-ad9b-1d05b716023c
                },
            })

            // const response = await fetching.json()

            if(fetching.ok) {
                //cara pertama panggil api lagi
                // getProductList()

                //cara kedua
                setCategories((categories) => categories.filter((category) => category._id !== id))
            }
        } catch (error) {
            alert(error)
        }
    }

    const columns: ColumnsType<Category> = [
        {
            title: 'ID',
            dataIndex: '_id',
            key: '_id',
        },
        {
            title: 'Client ID',
            dataIndex: 'clientid',
            key: 'clientid', 
        },
        {
            title: 'Ticker Code',
            dataIndex: 'tickercode',
            key: 'tickercode', 
        },
        {
            title: 'Outstanding Stock',
            dataIndex: 'outstanding',
            key: 'outstanding', 
        },
        {
            title: 'Priority',
            dataIndex: 'priority',
            key: 'priority', 
        },
        {
            title: 'Status',
            dataIndex: 'status',
            key: 'status', 
        },
        {
            title: 'Deadline',
            dataIndex: 'deadline',
            key: 'deadline', 
        },
        {
            title: 'Action',
            key: 'action',
            render: (_, record) => (
              <>
                <Button type={'default'} onClick={() => navigate(`/product/${record._id}`)}>Detail</Button>
                <Button type={'primary'} onClick={() => navigate(`/product/edit/${record._id}`)}>Update</Button>
                <Button type={'primary'} onClick={() => navigate(`/product/approval/${record._id}`)}>Approval/BrokerOnly</Button>
                <Button type={'primary'} color={'red'} onClick={() => removeProduct(record._id)} style={{ marginLeft: "0.3rem" }}>Delete</Button>
              </>
            ),
        },
    ];

    return (
        <>
            <h3>Product List</h3>
            <Button type={'primary'} onClick={() => navigate('/product/new')}>Add New ToDoList</Button>
            <ProductListComponent columns={columns} data={categories}/>
        </>
    )
}

export default ProductList