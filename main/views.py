from datetime import date
from main import db
from flask import (
    Flask,
    render_template,
    request,
    redirect
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', reviews=db.select_reviews())


@app.route('/review', methods=['POST'])
def review():
    """Додавлення нового відгуку в базу"""
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        date_time = date.today().strftime("%d.%m.%Y")
        db.insert_new_review(name=name, text=text, date=date_time)
    return redirect('/')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/angiography-lower-extremities')
def angiography_lower_extremities():
    """Ангіографія нижніх кінцівок"""
    return render_template('subcategories/angiography_lower_extremities.html')


@app.route('/ema')
def ema():
    """Емболізація маткових артерій (ЕМА)"""
    return render_template('subcategories/ema.html')


@app.route('/varicocele-embolization')
def varicocele_embolization():
    """Емболізація варікоцеле"""
    return render_template('subcategories/varicocele_embolization.html')


@app.route('/balloon-angioplasty-vessels')
def balloon_angioplasty_vessels():
    """Балонна ангіопластика судин"""
    return render_template('subcategories/balloon_angioplasty_vessels.html')


@app.route('/embolization-prostate-arteries')
def embolization_prostate_arteries():
    """Емболізація артерій простати"""
    return render_template('subcategories/embolization_prostate_arteries.html')


@app.route('/coronary-angiography-heart-pain')
def coronary_angiography_heart_pain():
    """Коронарографія при болях в серці"""
    return render_template('subcategories/coronary_angiography_heart_pain.html')


@app.route('/angiography-cerebral-vessels')
def angiography_cerebral_vessels():
    """Ангіографія судин головного мозку"""
    return render_template('subcategories/angiography_cerebral_vessels.html')


@app.route('/diagnostics/coronary-ventriculography')
def coronary_ventriculography():
    """Коронаровентрикулографія"""
    return render_template('diagnostics/сoronary_ventriculography.html')


@app.route('/diagnostics/cerebral-angiography')
def cerebral_angiography():
    """Церебральна ангіографія"""
    return render_template('diagnostics/cerebral_angiography.html')


@app.route('/diagnostics/aortography')
def aortography():
    """Аортографія"""
    return render_template('diagnostics/aortography.html')


@app.route('/diagnostics/arteriography-carotid-arteries')
def arteriography_carotid_arteries():
    """Артеріографія сонних артерій"""
    return render_template('diagnostics/arteriography_carotid_arteries.html')


@app.route('/diagnostics/arteriography-renal-arteries')
def arteriography_renal_arteries():
    """Артеріографія ниркових артерій"""
    return render_template('diagnostics/arteriography_renal_arteries.html')


@app.route('/diagnostics/arteriography-hepatic-artery')
def arteriography_hepatic_artery():
    """Артеріографія печінкової артерії"""
    return render_template('diagnostics/arteriography_hepatic_artery.html')


@app.route('/diagnostics/arteriography-splenic-artery')
def arteriography_splenic_artery():
    """Артеріографія селезінкової артерії"""
    return render_template('diagnostics/arteriography_splenic_artery.html')


@app.route('/diagnostics/arteriography-lower-and-upper-extremities')
def arteriography_lower_and_upper_extremities():
    """Артеріографія нижніх і верхніх кінцівок"""
    return render_template('diagnostics/arteriography_lower_and_upper_extremities.html')


@app.route('/diagnostics/pelvic-arteriography')
def pelvic_arteriography():
    """Тазова артеріографія"""
    return render_template('diagnostics/pelvic_arteriography.html')


@app.route('/diagnostics/phlebography-veins-extremities')
def phlebography_veins_extremities():
    """Флебографія вен кінцівок"""
    return render_template('diagnostics/phlebography_veins_extremities.html')


@app.route('/diagnostics/angiopulmonography')
def angiopulmonography():
    """Ангіопульмонографія"""
    return render_template('diagnostics/angiopulmonography.html')


@app.route('/diagnostics/phlebography-seminal-vein')
def phlebography_seminal_vein():
    """Флебографія сім’яної select_reviews()вени"""
    return render_template('diagnostics/phlebography_seminal_vein.html')
