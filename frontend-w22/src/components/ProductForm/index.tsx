import { Button, Card, Input, Typography } from "antd"
import { useFormik } from "formik"
import { Category, CategoryForm as CategoryFormProps } from "../../types"
import { initialValues, validationSchema } from "./productFormSchema"

interface Props {
    onSubmit: (values: CategoryFormProps) => void
    category?: Category
}

const CategoryForm = ({ onSubmit, category } : Props) => {

    const handleSubmit = (values: CategoryFormProps) => {
        onSubmit(values)
    }

    // const mergedInitialValues: CategoryFormProps = {
    //     _id: category ? category._id : '',
    //     clientid: category ? category.clientid : '',
    //     tickercode: category ? category.tickercode : '',
    //     purpose: category ? category.purpose : '',
    //     outstanding: null as number | null,
    //     status: category ? category.status : '',
    //     priority: null as number | null,
    //     deadline: category ? category.deadline : '',
    // };

    const formMik = useFormik({
        initialValues: category ?? initialValues,
        //mergedInitialValues,
        //category ?? initialValues,
        onSubmit: handleSubmit,
        validationSchema: validationSchema
    })

    return (
        <Card title={"IPO Preparation To Do List Form"} bordered style={{ width: 350 }}>
            <form onSubmit={formMik.handleSubmit}>
                <div>
                    <Typography.Paragraph>{'Client ID'}</Typography.Paragraph>
                    <Input 
                        name={'clientid'}
                        value={formMik.values.clientid} 
                        onChange={formMik.handleChange('clientid')}
                        status={formMik.errors.clientid && 'error'}
                    />
                    {formMik.errors.clientid && (
                        <Typography.Paragraph>{formMik.errors.clientid}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'Ticker Code'}</Typography.Paragraph>
                    <Input 
                        name={'tickercode'}
                        value={formMik.values.tickercode} 
                        onChange={formMik.handleChange('tickercode')}
                        status={formMik.errors.tickercode && 'error'}
                    />
                    {formMik.errors.tickercode && (
                        <Typography.Paragraph>{formMik.errors.tickercode}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'IPO Purpose'}</Typography.Paragraph>
                    <Input 
                        name={'purpose'}
                        value={formMik.values.purpose} 
                        onChange={formMik.handleChange('purpose')}
                        status={formMik.errors.purpose && 'error'}
                    />
                    {formMik.errors.purpose && (
                        <Typography.Paragraph>{formMik.errors.purpose}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'Outstanding Stock'}</Typography.Paragraph>
                    <Input 
                        name={'outstanding'}
                        value={formMik.values.outstanding} 
                        onChange={formMik.handleChange('outstanding')}
                        status={formMik.errors.outstanding && 'error'}
                    />
                    {formMik.errors.outstanding && (
                        <Typography.Paragraph>{formMik.errors.outstanding}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'IPO To Do List Status'}</Typography.Paragraph>
                    <Input 
                        name={'status'}
                        value={formMik.values.status} 
                        onChange={formMik.handleChange('status')}
                        status={formMik.errors.status && 'error'}
                    />
                    {formMik.errors.status && (
                        <Typography.Paragraph style={{ color: "red" }}>{formMik.errors.status}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'Priority Level'}</Typography.Paragraph>
                    <Input 
                        name={'priority'}
                        value={formMik.values.priority} 
                        onChange={formMik.handleChange('priority')}
                        status={formMik.errors.priority && 'error'}
                    />
                    {formMik.errors.priority && (
                        <Typography.Paragraph>{formMik.errors.priority}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'IPO Deadline'}</Typography.Paragraph>
                    <Input 
                        name={'deadline'}
                        value={formMik.values.deadline} 
                        onChange={formMik.handleChange('deadline')}
                        status={formMik.errors.deadline && 'error'}
                    />
                    {formMik.errors.deadline && (
                        <Typography.Paragraph>{formMik.errors.deadline}</Typography.Paragraph>
                    )}
                </div>
                <Button type={'primary'} htmlType={"submit"}>Submit</Button>
            </form>
        </Card>
    )
}

export default CategoryForm