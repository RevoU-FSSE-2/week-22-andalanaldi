export interface GetProductResponse {
    products: Product[];
    total: number;
    skip: number;
    limit: number;
}

export interface Product {
    id: number;
    title: string;
    status: boolean;
}

export type CategoryForm = Omit<Category,'id'>

// export interface Category extends CategoryForm {
//     id: string | undefined;
// }

// export type ProductForm = Omit<Product,'id'>

export interface LoginForm {
    username: string;
    password: string;
}

export interface LoginResponse {
    // email: string;
    // firstName: string;
    // lastName: string;
    // username: string;
    token: string;
}

export interface RegisForm {
    username: string;
    password: string;
    role: string;
}

export interface RegisResponse {
    message: string;
    data: {
        acknowledged: boolean;
        insertedId: string; 
    };
}

// export interface Regis {
//     acknowledged: boolean;
//     insertedId: string;
// }
// interface message {
//     message : string;
// }

// interface token {
//     token : string;
// }

export interface LoginResponse2 {
    message: string;
    data: string;
}

export const headers = {
    Authorization: `bearer ${localStorage.getItem('token')}`
}

// export const getAuthHeaders = () => {
//     const token = localStorage.getItem('token');
//     return {
//       Authorization: `bearer ${token}`,
//       'Content-Type': 'application/json',
//     };
//   };
  

export interface GetCategoryResponse {
    message: string;
    data: Category[];
}
// status, priority, deadline 
export interface Category {
    _id: string | undefined;
    clientid: string;
    tickercode: string;
    purpose: string;
    outstanding: number | undefined;
    status: string
    priority: number | undefined;
    deadline: string;
}

// export interface RegisForm {
//     name: string;
//     email   : string;
//     password: string;
// }

// export interface RegisResponse {
//     id: string;
//     name: string;
//     email: string;
//     password: string;
//     updated_at: string;
//     created_at: string;
// }

// interface token {
//     token : string;
// }

// export interface LoginResponse2 {
//     data: token;
//
// export interface GetCategoryResponse {
//     data: Category[];
//     current_page: number;
//     total_item: number;
//     total_page: number;
// }

// export interface Category {
//     id: string | undefined;
//     name: string;
//     is_active: boolean;
// }