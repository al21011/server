from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 21011

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./human.html')

@app.route('/human',methods=['POST'])
def update_human():
    time = request.form["time"]
    human = request.form["human"]
    try:
        f = open(file_path, "w")
        f.write(time + "," + human)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/human',methods=['GET'])
def get_human():
    try:
        f = open(file_path,'r')
        for row in f:
            human = row
    except Exception as e:
        print(e)
    finally:
        f.close()
        return human
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port_num)