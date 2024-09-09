from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField, DecimalField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for Mumbai areas
areas_data = {
     "Andheri": { "latitude": 19.1197, "longitude": 72.8464 },
            "Bandra": { "latitude": 19.0544, "longitude": 72.8400 },
            "Colaba": { "latitude": 18.9067, "longitude": 72.8147 },
            "Dadar": { "latitude": 19.0176, "longitude": 72.8467 },
            "Fort": { "latitude": 18.9338, "longitude": 72.8356 },
            "Girgaon": { "latitude": 18.9543, "longitude": 72.8127 },
            "Goregaon": { "latitude": 19.1551, "longitude": 72.8493 },
            "Juhu": { "latitude": 19.1024, "longitude": 72.8267 },
            "Kalyan": { "latitude": 19.2437, "longitude": 73.1355 },
            "Kandivali": { "latitude": 19.2047, "longitude": 72.8526 },
            "Kurla": { "latitude": 19.0728, "longitude": 72.8795 },
            "Lower Parel": { "latitude": 18.9934, "longitude": 72.8303 },
            "Malad": { "latitude": 19.1860, "longitude": 72.8485 },
            "Marine Lines": { "latitude": 18.9445, "longitude": 72.8231 },
            "Matunga": { "latitude": 19.0256, "longitude": 72.8570 },
            "Mulund": { "latitude": 19.1726, "longitude": 72.9565 },
            "Nagpada": { "latitude": 18.9647, "longitude": 72.8255 },
            "Navi Mumbai": { "latitude": 19.0330, "longitude": 73.0297 },
            "Powai": { "latitude": 19.1171, "longitude": 72.9050 },
            "Sion": { "latitude": 19.0400, "longitude": 72.8646 },
            "Thane": { "latitude": 19.2183, "longitude": 72.9781 },
            "Vashi": { "latitude": 19.0771, "longitude": 72.9986 },
            "Vile Parle": { "latitude": 19.1013, "longitude": 72.8437 },
            "Worli": { "latitude": 19.0167, "longitude": 72.8167 },
            "Wadala": { "latitude": 19.0198, "longitude": 72.8542 },
            "Santacruz": { "latitude": 19.0808, "longitude": 72.8417 },
            "Ghatkopar": { "latitude": 19.0860, "longitude": 72.9081 },
            "Chembur": { "latitude": 19.0622, "longitude": 72.8976 },
            "Borivali": { "latitude": 19.2307, "longitude": 72.8567 },
            "Versova": { "latitude": 19.1330, "longitude": 72.8146 },
            "Byculla": { "latitude": 18.9784, "longitude": 72.8320 },
            "Charni Road": { "latitude": 18.9501, "longitude": 72.8190 },
            "Churchgate": { "latitude": 18.9324, "longitude": 72.8265 },
            "Cuffe Parade": { "latitude": 18.9070, "longitude": 72.8083 },
            "Dahisar": { "latitude": 19.2578, "longitude": 72.8591 },
            "Elphinstone": { "latitude": 18.9922, "longitude": 72.8258 },
            "Gorgaon": { "latitude": 19.1688, "longitude": 72.8456 },
            "Grant Road": { "latitude": 18.9650, "longitude": 72.8137 },
            "Jogeshwari": { "latitude": 19.1316, "longitude": 72.8424 },
            "Kalbadevi": { "latitude": 18.9478, "longitude": 72.8307 },
            "Khar": { "latitude": 19.0663, "longitude": 72.8394 },
            "King's Circle": { "latitude": 19.0331, "longitude": 72.8562 },
            "Mahim": { "latitude": 19.0413, "longitude": 72.8413 },
            "Mankhurd": { "latitude": 19.0507, "longitude": 72.9363 },
            "Mazgaon": { "latitude": 18.9672, "longitude": 72.8453 },
            "Mumbai Central": { "latitude": 18.9712, "longitude": 72.8197 },
            "Parel": { "latitude": 18.9930, "longitude": 72.8372 },
            "Prabhadevi": { "latitude": 19.0166, "longitude": 72.8258 },
            "Sakinaka": { "latitude": 19.1014, "longitude": 72.8855 },
            "Sewri": { "latitude": 18.9886, "longitude": 72.8617 },
            "Tardeo": { "latitude": 18.9714, "longitude": 72.8134 },
            "Vikhroli": { "latitude": 19.1015, "longitude": 72.9306 },
            "Walkeshwar": { "latitude": "18.9536", "longitude": 72.7963 },
            "Breach Candy": { "latitude": 18.9716, "longitude": 72.8070 },
            "Bhayandar": { "latitude": 19.3012, "longitude": 72.8511 },
            "Bhuleshwar": { "latitude": 18.9512, "longitude": 72.8297 },
            "Charkop": { "latitude": 19.2100, "longitude": 72.8410 },
            "Dharavi": { "latitude": 19.0418, "longitude": 72.8571 },
            "Dongri": { "latitude": 18.9667, "longitude": 72.8373 },
            "Gansoli": { "latitude": 19.1272, "longitude": 73.0086 },
            "Govandi": { "latitude": 19.0432, "longitude": 72.9234 },
            "Kanjurmarg": { "latitude": 19.1253, "longitude": 72.9369 },
            "Khopoli": { "latitude": 18.7840, "longitude": 73.3455 },
            "Lokhandwala": { "latitude": 19.1401, "longitude": 72.8327},
            "Mahalaxmi": { "latitude": 18.9832, "longitude": 72.8225 },
            "Mantralaya": { "latitude": 18.9266, "longitude": 72.8235 },
            "Marol": { "latitude": 19.1114, "longitude": 72.8763 },
            "Mazagaon": { "latitude": "18.9672", "longitude": 72.8453 },
            "Mulund West": { "latitude": 19.1730, "longitude": 72.9481 },
            "Nepean Sea Road": { "latitude": 18.9556, "longitude": 72.7987 },
            "Peddar Road": { "latitude": 18.9704, "longitude": 72.8071 },
            "Sandhurst Road": { "latitude": 18.9568, "longitude": 72.8378 },
            "Sewree": { "latitude": 18.9886, "longitude": 72.8617 },
            "Sion East": { "latitude": 19.0371, "longitude": 72.8637 },
            "Trombay": { "latitude": 19.0167, "longitude": 72.9184 },
            "Vakola": { "latitude": 19.0884, "longitude": 72.8566 },
            "Vikhroli West": { "latitude": 19.1054, "longitude": 72.9145 },
            "Vile Parle East": { "latitude": 19.0998, "longitude": 72.8535 },
            "Vile Parle West": { "latitude": 19.1006, "longitude": 72.8412 },
            "Worli Sea Face": { "latitude": 19.0083, "longitude": 72.8150 },
            "Worli Naka": { "latitude": 19.0100, "longitude": 72.8200 },
            "Airoli": { "latitude": 19.1526, "longitude": 72.9966 },
            "Antop Hill": { "latitude": 19.0216, "longitude": 72.8685 },
            "August Kranti Maidan": { "latitude": 18.9656, "longitude": 72.8110 }
    
}

class AdminForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    city = SelectField('City', choices=[('Mumbai', 'Mumbai')], default='Mumbai', render_kw={'readonly': True})
    area = SelectField('Area', choices=[(area, area) for area in areas_data.keys()], validators=[InputRequired()])
    latitude = FloatField('Latitude', validators=[InputRequired()], render_kw={'readonly': True})
    longitude = FloatField('Longitude', validators=[InputRequired()], render_kw={'readonly': True})
    submit = SubmitField('Submit')

class PredictionForm(FlaskForm):
    area = SelectField('Area', choices=[(area, area) for area in areas_data.keys()], validators=[InputRequired()])
    monsoon_intensity = DecimalField('Monsoon Intensity', validators=[InputRequired(), NumberRange(min=0)], places=2)
    deforestation = DecimalField('Deforestation', validators=[InputRequired(), NumberRange(min=0)], places=2)
    climate_change = DecimalField('Climate Change', validators=[InputRequired(), NumberRange(min=0)], places=2)
    siltation = DecimalField('Siltation', validators=[InputRequired(), NumberRange(min=0)], places=2)
    agricultural_practices = DecimalField('Agricultural Practices', validators=[InputRequired(), NumberRange(min=0)], places=2)
    drainage_systems = DecimalField('Drainage Systems', validators=[InputRequired(), NumberRange(min=0)], places=2)
    coastal_vulnerability = DecimalField('Coastal Vulnerability', validators=[InputRequired(), NumberRange(min=0)], places=2)
    landslides = DecimalField('Landslides', validators=[InputRequired(), NumberRange(min=0)], places=2)
    population_score = DecimalField('Population Score', validators=[InputRequired(), NumberRange(min=0)], places=2)
    inadequate_planning = DecimalField('Inadequate Planning', validators=[InputRequired(), NumberRange(min=0)], places=2)
    submit = SubmitField('Predict')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AdminForm()

    if request.method == 'POST' and form.validate():
        selected_area = form.area.data
        form.latitude.data = areas_data[selected_area]['latitude']
        form.longitude.data = areas_data[selected_area]['longitude']
        
        flash('Form submitted successfully!')
        # Handle form submission logic here (e.g., save data to a database)
    
    return render_template('index.html', form=form)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictionForm()
    
    if form.validate_on_submit():
        # Handle prediction logic here
        flash('Prediction submitted successfully!')
        return redirect(url_for('index'))
        
    return render_template('prediction.html', form=form)

@app.route('/get_latlon', methods=['POST'])
def get_latlon():
    area = request.form.get('area')
    if area in areas_data:
        latlon = areas_data[area]
        return jsonify(latitude=latlon['latitude'], longitude=latlon['longitude'])
    return jsonify(error="Area not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
