from flask import Flask
import datetime
app=Flask(__name__)

@app.route("/")
def rakesh3():
    current_time=datetime.datetime.now()
    print(current_time)  
    return "The time is %s" %current_time
if __name__=='__main__':
    app.run(debug=True)