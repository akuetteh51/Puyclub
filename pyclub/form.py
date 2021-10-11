from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired,Required


class Form(FlaskForm):
    Name = StringField('Name:', validators=[DataRequired("PLease Enter your Name.")],render_kw={"placeholder": "Name","class":"form-control"})
    Registration_No=StringField('Registration no:',validators=[DataRequired("PLease Enter your Name.")],render_kw={"placeholder": "PS/CSC/18/0000","class":"form-control"})
    Contact=StringField('Contact',validators=[DataRequired("PLease Enter your Contact.")],render_kw={"placeholder": "Contact","class":"form-control"})
    myChoices = ['100','200','300','400'] # number of choices
    level = SelectField('Level', choices=myChoices, validators=[Required()],render_kw={"class":"form-control"})
    
    Amount= StringField('Amount:',validators=[DataRequired("PLease Enter Amount.")],render_kw={"placeholder": "10","class":"form-control"})
    Email = StringField('Email:', validators=[DataRequired("PLease Enter your E-mail.")],render_kw={"placeholder": "@stu.ucc.edu.gh","class":"form-control"})
    submit = SubmitField('pay',render_kw={"class":"btn btn-primary"})
    myChoice = ['MTN','AirtelTigo','Vodafone'] # number of choices
    MobileMoney = SelectField('Momo', choices=myChoice, validators=[Required()],render_kw={"class":"form-control"})



# print(Form.data())