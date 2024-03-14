from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests

class MyApp(App):
    def build(self):
        # UI components
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text='Waiting for response...')
        self.layout.add_widget(self.label)

        self.button = Button(text='Get Flask Response', on_press=self.get_flask_response)
        self.layout.add_widget(self.button)

        return self.layout

    def get_flask_response(self, instance):
        try:
            # Replace 'http://127.0.0.1:5000/' with the actual Flask app URL
            flask_url = 'http://127.0.0.1:5000/'
            response = requests.get(flask_url)
            flask_message = response.text

            # Update label with Flask response
            self.label.text = f'Flask Response: {flask_message}'
        except Exception as e:
            self.label.text = f'Error: {str(e)}'

if __name__ == '__main__':
    MyApp().run()
