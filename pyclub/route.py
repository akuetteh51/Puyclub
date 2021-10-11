from flask import Flask,render_template,request
from form import Form
from mom_api import momo_send
app=Flask(__name__)

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
if __name__=='__main__':
   app.run(debug=True)