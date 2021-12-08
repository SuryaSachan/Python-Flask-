from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "hi there!"
 

if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 8080,debug=True)

# build : docker run --network host -v $PWD:/testsrc -it flask:latest
# build : docker run --network host -v(volume) $PWD:/testsrc -it(iterator) <image name>:<version>