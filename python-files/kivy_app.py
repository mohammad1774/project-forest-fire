from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.loader import Loader
import requests
from io import BytesIO
from PIL import Image as PILImage

class ImagePredictionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Image display widget
        self.image = Image(size=(300, 300), allow_stretch=True)
        self.layout.add_widget(self.image)

        # FileChooser widget
        self.file_chooser = FileChooserListView()
        self.layout.add_widget(self.file_chooser)

        # Button to make predictions
        btn_predict = Button(text='Predict', size_hint=(None, None))
        btn_predict.bind(on_press=self.predict_image)
        self.layout.add_widget(btn_predict)

        return self.layout

    def predict_image(self, instance):
        # Check if an image is selected
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]
        if not selected_file:
            self.show_error_popup("Please select an image file.")
            return

        # Load and display the selected image
        image_path = selected_file
        self.load_and_display_image(image_path)

        # Make predictions using the API
        try:
            prediction = self.call_api_for_prediction(image_path)
            self.show_prediction_popup(prediction)
        except Exception as e:
            self.show_error_popup(f"Error: {str(e)}")

    def load_and_display_image(self, image_path):
        # Load and display the selected image
        self.image.source = image_path
        self.image.reload()

    def call_api_for_prediction(self, image_path):
        # Convert image to bytes for sending in the API request
        img = PILImage.open(image_path)
        img_bytes = BytesIO()
        img.save(img_bytes, format='JPEG')

        # Send a POST request to the API endpoint (replace with your API URL)
        api_url = 'http://127.0.0.1:5000'
        files = {'image': img_bytes.getvalue()}
        response = requests.post(api_url, files=files)

        # Parse and return the prediction from the response
        prediction = response.json()
        print(prediction)
        return prediction

    def show_prediction_popup(self, prediction):
        # Display a popup with the prediction
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text='Prediction:'))
        content.add_widget(Label(text=str(prediction)))

        popup = Popup(title='Prediction', content=content, size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_error_popup(self, error_message):
        # Display a popup for errors
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text=f'Error: {error_message}'))

        popup = Popup(title='Error', content=content, size_hint=(None, None), size=(300, 150))
        popup.open()

if __name__ == '__main__':
    ImagePredictionApp().run()
