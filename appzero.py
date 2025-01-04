from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def josephus(n, k, step):
    a = np.arange(n) + 1
    c = 0
    result = []  # Properly indented

    if step == '0':
        result.append(f"step {c}: {a.tolist()}")

    while n > 1:
        if n > k - 1:
            c1 = k - 1
            while c1 < n:
                a[c1] = 0
                c1 += k

            for i in a:
                if i != 0:
                    a = np.append(a, i)

            zero = np.where(a == 0)
            last = np.max(zero)
            a = a[last + 1:]
            a = np.array(list(dict.fromkeys(a)))
            n = len(a)

            if step == '0':
                c += 1
                result.append(f"step {c}: {a.tolist()}")

        elif n <= k - 1:
            c2 = k - n - 1
            while c2 > n - 1:
                c2 = c2 - n

            a[c2] = 0
            for i in a:
                if i != 0:
                    a = np.append(a, i)

            zero = np.where(a == 0)
            last = np.max(zero)
            a = a[last + 1:]
            a = np.array(list(dict.fromkeys(a)))
            n = len(a)

            if step == '0':
                c += 1
                result.append(f"step {c}: {a.tolist()}")

    return a[-1], result

@app.route('/', methods=['GET', 'POST'])
def inputs():
    survivor = None
    steps = None
    
    if request.method == 'POST':
        try:
            n = int(request.form['n'])
            k = int(request.form['k'])
            step = request.form['step']

            survivor, steps = josephus(n, k, step)

        except Exception as e:
            return render_template('index.html', survivor=survivor, steps=steps)

    return render_template('index.html', survivor=None, steps=None)

if __name__ == '__main__':
    app.run(debug=True)

