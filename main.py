from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/fibonacci/",methods=["GET"])
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
## https://example.com/fibonacci/?x=1&y=1&count=10

@app.route("/aliquot/",methods=["GET"])
def main():
    try:
      x = int(request.args.get("x"))
      z = [i for i in range(1, x+1) if x % i ==0]
      if len(z) == 2:
        return z
      else:
        answer = [x]
        while True:
          if len(z) == 2:
            answer.append(1)
            return answer
            break
          else:
            del z[len(z)-1]
            sumz = sum(z)
            z = [i for i in range(1, sum(z)+1) if sum(z) % i ==0]
            answer.append(sumz)
            if answer[len(answer)-1] == answer[len(answer)-2]:
              return [x]
              break
    except:
      return abort(400,"Argument Error")
## https://example.com/aliquot/?x=12

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000)
