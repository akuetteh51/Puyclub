from flask import Flask,render_template,request
from form import Form
import beyonic
# from momo_api import momo_send





app=Flask(__name__)

app.config['SECRET_KEY']='mysecret' 
# myapi = os.environ['BEYONIC_ACCESS_KEY']
@app.route('/')
def index():
    form=Form()
    return render_template('index.html',form=form)


@app.route("/success",methods=['POST'])
def success():
    form=Form()
    
    if request.method == "POST":
        reg = form.Registration_No.data
        name = form.Name.data
        level = form.level.data
        email = form.Email.data
        momo =form.MobileMoney.data
        Amount = form.Amount.data
        Contact = form.Contact.data
        momo_send(Contact,Amount)
    return render_template('success.html')

#     @app.route("/payment", methods = ['POST', 'GET'])
# def makepayment():
#     form=Form()

#     if request.method == "POST":
    #    if form.is_submitted():
    #         print("Form successfully submitted")
    #    if form.validate_on_submit():
        # reg = form.Registration_No.data
        # name = form.Name.data
        # level = form.level.data
        # email = form.Email.data
        # momo =form.MobileMoney.data
        # Amount = form.Amount.data
        # Contact = form.Contact.data
        # name = request.form.data("Name", default_value)
        # currency="BXC"
        # description="NEw money"
        # callback_url='https://nhanaqwahme.pythonanywhere.com/payments/callback',

        # # payment = beyonic.Payment.create(
        #                       phonenumber = Contact,
        #                       Name = name,
        #                       amount = Amount,
        #                       currency = currency,
        #                       description = description,
        #                       callback_url = callback_url
        #                       #metadata={'id': '1234', 'name': 'Lucy'}
        #                       )
        # return 'success' 
    #  return render_template('index.html',form=form)
        # print(Contact)
        # return(momo_send(Contact,Amount))
    # return render_template('success.html')

#list all your transactions
# @app.route("/transactions")
# def transactions ():
#     # transactions  = beyonic.Transaction.list()
    # return transactions
if __name__=='__main__':
   app.run(debug=True)