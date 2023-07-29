from flask import Flask,render_template, request, url_for
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from tensorflow.keras.utils import img_to_array, load_img
from keras.applications.vgg19 import VGG19
from PIL import Image 
import os

# Define the list of class names
class_names = ["Apple - Apple_scab",
        "Apple - Black rot",
        "Apple - Cedar apple rust",
        "Apple - healthy",
        "Background without leaves",
        "Blueberry - healthy",
        "Cherry - Powdery mildew",
        "Cherry - healthy",
        "Corn - Cercospora leaf spot Gray leaf spot",
        "Corn - Common rust",
        "Corn - Northern Leaf Blight",
        "Corn - healthy",
        "Grape - Black rot",
        "Grape - Esca (Black Measles)",
        "Grape - Leaf blight (Isariopsis Leaf Spot)",
        "Grape - healthy",
        "Orange - Haunglongbing (Citrus greening)",
        "Peach - Bacterial spot",
        "Peach - healthy",
        "Pepper bell - Bacterial spot",
        "Pepper bell - healthy",
        "Potato - Early blight",
        "Potato - Late blight",
        "Potato - healthy",
        "Raspberry - healthy",
        "Soybean - healthy",
        "Squash - Powdery mildew",
        "Strawberry - Leaf scorch",
        "Strawberry - healthy",
        "Tomato - Bacterial spot",
        "Tomato - Early blight",
        "Tomato - healthy",
        "Tomato - Late blight",
        "Tomato - Leaf Mold",
        "Tomato - Septoria leaf spot",
        "Tomato - Spider mites Two-spotted spider mite",
        "Tomato - Target Spot",
        "Tomato - Tomato mosaic virus",
        "Tomato - Tomato Yellow Leaf Curl Virus"]

# Load the VGG19 model
vgg19_model = VGG19(include_top=False, input_shape=(256, 256, 3))

# Freeze the pre-trained layers
for layer in vgg19_model.layers:
    layer.trainable = False

# Add new classification layers on top of the VGG19 model
model = tf.keras.models.Sequential([
    vgg19_model,
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units= 39, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(class_names), activation="softmax")
])

# Load the pre-trained weights for the new classification layers
model= load_model("E:\\coding\\pdr project\\plantdiseaserecognition\\best_accmodel.h5")


app = Flask(__name__)

# Define the path where uploaded images will be saved
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the allowed image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if a given filename is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/about")
def about():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        # Check if the file is allowed
        if file and allowed_file(file.filename):
            # Save the file to the server
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Redirect back to the about page
            return redirect(url_for('about1'))
    # Render the about page template
    return render_template('about1.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/", methods=["POST"])
def predict():
    global class_names


    imagefile= request.files["imagefile"]
    image_path = "E:\\coding\\pdr project\\plantdiseaserecognition\\static\\images\\" + imagefile.filename

    # Create the images directory if it does not exist
    if not os.path.exists("E:\\coding\\pdr project\\plantdiseaserecognition\\static\\images"):
        os.makedirs("E:\\coding\\pdr project\\plantdiseaserecognition\\static\\images")
    imagefile.save(image_path)

      # Load and preprocess the image
    img = load_img(image_path, target_size=(256, 256))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.vgg19.preprocess_input(x)

     # Make a prediction
    outputs = model.predict(x)
    prediction = np.argmax(outputs[0])
    class_name = class_names[prediction]

    
   # Extract the plant name from the class name
    plant_name = class_name.split(" - ")[0]

    # Modify the class name based on the prediction
    is_healthy = "healthy" in class_name
    if is_healthy:
        class_name = plant_name + " (Healthy)"
    else:
        class_name = class_name.split(" - ")[1]

     # Generate a URL for the uploaded image
    image_url = url_for("static", filename="images.jpg/" + imagefile.filename)


    return render_template("result.html", class_name=class_name, plant_name=plant_name, image_url=image_url, image_filename=imagefile.filename)

if __name__ == "__main__":
    app.run(debug=True)
