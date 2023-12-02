import * as yup from 'yup'

export const initialValues = {
    _id: '',
    // why _id should be included 
    clientid: '',
    tickercode: '', 
    purpose: '', 
    outstanding: undefined,
    //null 
    status: '',
    priority: undefined,
    //null 
    deadline: '',
}

export const validationSchema = yup.object({
    clientid: yup.string().required('Client ID is required'),
    tickercode: yup.string().required('Ticker code is required'),
    purpose: yup.string().required('Purpose is required'),
    outstanding: yup.number().typeError('Outstanding must be a number').nullable(),
    status: yup.string().required('Status is required'),
    priority: yup.number().typeError('Priority must be a number').nullable(),
    deadline: yup
      .string()
      .required('Deadline is required')
      .matches(/^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$/, 'Invalid ISO8601 date format')
      .test('is-future', 'Deadline must be in the future', (value) => {
        const currentDate = new Date();
        const deadlineDate = new Date(value);
        return deadlineDate > currentDate;
      }),
})