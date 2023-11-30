
from flask import Flask, render_template, redirect, flash, jsonify
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "ihaveasecret"

connect_db(app)
db.create_all()


@app.route('/')
def show_all_pets():
    """Render home page"""
    if __name__ == '__main__':
        app.run()
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Displays and Handles submission of New Pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} Added!")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
    else:
        return render_template('edit_pet_form.html', form=form)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return pet info in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)

