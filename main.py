from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/fibonacci",methods=["GET"])
def main():
    try:
      x = int(request.args.get("x"))
      y = int(request.args.get("y"))
      count = int(request.args.get("count"))
      z = [x, y]
      for i in range(count):
        z.append(z[i] + z[i+1])
      return z
    except:
      return abort(400,"Argument Error")
## https://example.com/?x=1&y=1&count=10

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000)
