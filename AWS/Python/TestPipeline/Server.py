from flask import Flask
from flask import Flask, render_template
from DataAnalysis import AnalyzeEC2

a = AnalyzeEC2()
lastFile = a.findLastFile("templates")


app = Flask(__name__)

@app.route("/")
def analysisPage():
    #Finding lastest page
    analysispage = f"{lastFile}"
    # Formating URL/String to avoid templates/
    formatStr = analysispage.replace("templates/","")

    return render_template(formatStr)

if __name__ == "__main__": 

    app.run()