import * as yup from 'yup'

export const initialValues = {
    username: '',
    password: ''
}

export const validationSchema = yup.object({
    username: yup.string().required(),
    password: yup.string()
                 .required()
                 .min(8, 'Password is too short - should be 8 characters at least.')
                //  .matches(/^(?=.*\d)(?=.*[a-zA-Z]).+$/, 'Password can only contain latin letters & numbers.')
})
// email: yup.string().email().required(),