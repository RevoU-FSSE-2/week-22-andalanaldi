import { useParams } from 'react-router-dom'

const ProductDetail = () => {
    const params = useParams();

    return (
        <div>
            This is product detail of IPO Preparations ToDoList Web App page with id: {params?.id}
        </div>
    )
}

export default ProductDetail