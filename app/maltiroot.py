def maltiroot(x:int, y:int):
  z = x**(1/y)
  return round(z)

## print(maltiroot(64, 3))

from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    try:
      x = int(request.args.get("x"))
      y = int(request.args.get("y"))
      z = x**(1/y)
      return round(z)
    except:
      return abort(400,"Argument Error")
## https://example.com/?x=27&y=3

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000)
