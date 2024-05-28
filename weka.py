from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class CKDDecisionTree:
    def predict(self, sc, pe, dm, hemo, sg):
        if sc <= 1.2:
            if pe == 'yes':
                return 'ckd'
            else:
                if dm == 'yes':
                    return 'ckd'
                else:
                    if hemo <= 12.9:
                        return 'ckd'
                    else:
                        if sg == 1.005:
                            return 'notckd'
                        elif sg == 1.01:
                            return 'ckd'
                        elif sg == 1.015:
                            return 'ckd'
                        elif sg == 1.02:
                            return 'notckd'
                        elif sg == 1.025:
                            return 'notckd'
        else:
            return 'ckd'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        sc = float(request.form['sc'])
        pe = request.form['pe']
        dm = request.form['dm']
        hemo = float(request.form['hemo'])
        sg = float(request.form['sg'])

        # Input validation
        if not (0 < sc < 20):
            flash('Serum Creatinine (sc) must be between 0 and 20')
            return redirect(url_for('index'))

        if not (0 < hemo <= 20):
            flash('Hemoglobin (hemo) must be between 0 and 20')
            return redirect(url_for('index'))

        if not (1.005 <= sg <= 1.025):
            flash('Specific Gravity (sg) must be between 1.005 and 1.025')
            return redirect(url_for('index'))

        if pe not in ['yes', 'no']:
            flash('Invalid input for Pedal Edema (pe)')
            return redirect(url_for('index'))

        if dm not in ['yes', 'no']:
            flash('Invalid input for Diabetes Mellitus (dm)')
            return redirect(url_for('index'))

        model = CKDDecisionTree()
        prediction = model.predict(sc, pe, dm, hemo, sg)
        return render_template('index.html', prediction=prediction)

    except ValueError:
        flash('Invalid input. Please enter numeric values where required.')
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
