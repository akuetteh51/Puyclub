import os
import beyonic
from werkzeug.wrappers import response
from form import Form
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)  
app.config['SECRET_KEY']= os.environ['SECRET_KEY']
myapi = os.environ['BEYONIC_ACCESS_KEY']

@app.get("/")
def index():
    form=Form()
    return render_template('index.html',form=form)


#creating payment
@app.route("/payment", methods = ['POST', 'GET'])
def makepayment():
    form=Form()
    if request.method == "POST":
        if form.is_submitted():
            print("Form successfully submitted")
        if form.validate_on_submit():
            reg = form.Registration_No.data
            name = form.Name.data
            level = form.level.data
            email = form.Email.data
            momo =form.MobileMoney.data
            Amount = form.Amount.data
            Contact = form.Contact.data

            name = request.form.get("Name",'default value')
  
                     
        return render_template('success.html')              
    return rrender_template('index.html',form=form)

#list all your transactions
@app.route("/transactions")
def transactions ():
    transactions  = beyonic.Transaction.list()
    return transactions 
 
@app.post('/botmessage')
def botchat():
    # text=request.get_json().get('message')
    # #
    # response=get_response(text)
    # message = {'answer':response}
    # return jsonify(message)
    return 'bot message'

if __name__ == '__main__':
    app.run(debug=True)