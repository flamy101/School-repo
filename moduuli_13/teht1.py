from flask import Flask

app = Flask(__name__)

def is_prime(num: int):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route("/prime/<int:num>", methods=["GET"])
def prime_num(num: int):
    res = {
            "Number": num,
            "isPrime": is_prime(num)
    }
    return [res]

if __name__ == "__main__":
    app.run(port=3000, debug=True)