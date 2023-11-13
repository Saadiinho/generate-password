from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MonApp(App):
    def build(self):
        # Création de la mise en page (layout)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Création des widgets
        label = Label(text='Entrez votre nom:')
        entry = TextInput(text='', multiline=False)
        bouton = Button(text='Cliquez-moi!')
        resultat_label = Label(text='')

        # Liaison du bouton à une fonction
        bouton.bind(on_press=lambda x: self.bouton_clic(entry.text, resultat_label))

        # Ajout des widgets à la mise en page
        layout.add_widget(label)
        layout.add_widget(entry)
        layout.add_widget(bouton)
        layout.add_widget(resultat_label)

        return layout

    def bouton_clic(self, nom, resultat_label):
        resultat_label.text = "Bonjour " + nom

# Lancement de l'application
if __name__ == '__main__':
    MonApp().run()
