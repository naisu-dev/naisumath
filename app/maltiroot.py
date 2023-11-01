## https://gist.github.com/naisu-dev/b0a5b5227ee31b8875694ca818132ac7
## https://replit.com/@naisu-dev/multiroot?s=app

def malti_root(x: int, y: int):
  z = x**(1 / y)
  z = x**(1 / y)
  return round(z)

## print(malti_root(64, 3))

from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
  try:
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    z = x**(1 / y)
    return round(z)
  except:
    return abort(400, "Argument Error")

## https://example.com/?x=27&y=3

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000)
