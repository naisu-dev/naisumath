## https://gist.github.com/naisu-dev/843d4ab597325731a285d3d60e1504e0
## https://replit.com/@naisu-dev/fibonacci-sequence?s=app

def fibonacci(x :int,y: int,count: int):
  z = [x, y]
  for i in range(count):
    z.append(z[i] + z[i+1])
  return z

## print(fibonacci(1, 10, 10))

from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/",methods=["GET"])
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
