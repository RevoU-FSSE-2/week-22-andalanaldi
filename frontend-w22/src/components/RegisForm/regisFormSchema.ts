import * as yup from 'yup'

export const initialValues = {
    username: '',
    password: '',
    role: ''
}

export const validationSchema = yup.object({
    username: yup.string().required(),
    password: yup.string()
                 .required()
                 .min(8, 'Password is too short - should be 8 characters at least.')
                 .matches(/^(?=.*\d)(?=.*[a-zA-Z]).+$/, 'Password can only contain latin letters & numbers.'),
    role: yup.string().required(),
})  

// export const initialValues = {
//     name: '',
//     email   : '',
//     password: ''
// }

// export const validationSchema = yup.object({
//     name: yup.string().required(),
//     email   : yup.string().email().required(),
//     password: yup.string()
//                  .required()
//                  .min(8, 'Password is too short - should be 8 characters at least.')
//                 //  .matches(/^(?=.*\d)(?=.*[a-zA-Z]).+$/, 'Password can only contain latin letters & numbers.')
// })  