import { Button, Card, Input, Typography } from "antd"
import { useFormik } from "formik"
import { RegisForm as RegisFormProps } from "../../types"
import { initialValues, validationSchema } from "./regisFormSchema"

interface Props {
    onSubmit: (values: RegisFormProps) => void
}

const RegisForm = ({ onSubmit } : Props) => {

    const handleSubmit = (values: RegisFormProps) => {
        onSubmit(values)
    }

    const formMik = useFormik({
        initialValues: initialValues,
        onSubmit: handleSubmit,
        validationSchema: validationSchema
    })

    return (
        <Card title={"Registration Page"} bordered style={{ width: 350 }}>
            <form onSubmit={formMik.handleSubmit}>
                <div>
                    <Typography.Paragraph>{'Username'}</Typography.Paragraph>
                    <Input name={'Username'}
                        value={formMik.values.username} 
                        onChange={formMik.handleChange('username')}
                        status={formMik.errors.username && 'error'}
                    />
                    {formMik.errors.username && (
                        <Typography.Paragraph>{formMik.errors.username}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'Password'}</Typography.Paragraph>
                    <Input name={'password'}
                        value={formMik.values.password} 
                        onChange={formMik.handleChange('password')}
                        status={formMik.errors.password && 'error'}
                        type={'password'}
                    />
                    {formMik.errors.password && (
                        <Typography.Paragraph>{formMik.errors.password}</Typography.Paragraph>
                    )}
                </div>
                <div>
                    <Typography.Paragraph>{'Role'}</Typography.Paragraph>
                    <Input name={'role'}
                        value={formMik.values.role} 
                        onChange={formMik.handleChange('role')}
                        status={formMik.errors.role && 'error'}
                    />
                    {formMik.errors.role && (
                        <Typography.Paragraph>{formMik.errors.role}</Typography.Paragraph>
                    )}
                </div>
                <Button type={'primary'} htmlType={"submit"}>Submit</Button>
            </form>
        </Card>
    )
}

export default RegisForm