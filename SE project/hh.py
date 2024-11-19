from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Folder for storing uploaded images

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="8098273siuu",
        database="car_market"
    )

# Route to render the HTML form
@app.route('/list-car', methods=['GET', 'POST'])
def list_car():
    if request.method == 'POST':
        # Retrieve form data
        title = request.form['title']
        brand_name = request.form['BrandName']
        car_model = request.form['Car-Model']
        model_year = request.form['Model(Year)']
        price = request.form['price']
        mileage = request.form['Milage']
        body_type = request.form['Body-Type']
        image = request.files['image']

        # Save image and get the path
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # Insert data into the database
        db = connect_db()
        cursor = db.cursor()
        query = "INSERT INTO Cars (title, brand_name, car_model, model_year, price, mileage, body_type, image_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (title, brand_name, car_model, model_year, price, mileage, body_type, image_path)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('list_car'))  # Redirect to the same page or any success page

    return render_template('list_car.html')  # Render your HTML form

if __name__ == '__main__':
    app.run(debug=True)
