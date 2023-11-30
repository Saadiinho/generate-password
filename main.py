from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import secrets
import string


class PasswordGeneratorLayout(BoxLayout):
    def generate_password(self):
        platform = self.ids.platform_input.text
        alphabet = string.ascii_letters + string.digits + string.punctuation
        print("Hello, World!")
        try:
            pwd_length = int(self.ids.length_input.text)
            if pwd_length < 8:
                self.ids.result_label.text = "La longueur doit être supérieure à 8."
            else:
                password = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))
                self.ids.result_label.text = f"Mot de passe pour {platform} : {password}"

                with open('save_password.txt', 'a') as fichier:
                    fichier.write(f"{platform}: {password}\n")
        except ValueError:
            self.ids.result_label.text = "Veuillez saisir une longueur valide."

    def show_password(self):
        nom_fichier = 'save_password.txt'
        with open(nom_fichier, 'r') as fichier:
            # Lire le contenu du fichier ligne par ligne
            lignes = fichier.readlines()
                
            # Afficher chaque ligne lue
            for ligne in lignes:
                print(ligne.strip()) 
    def stop(self):
        # Cette fonction est appelée lors de l'appui sur le bouton "Quitter l'application"
        App.get_running_app().stop()



class PasswordGeneratorApp(App):
    def build(self):
        return PasswordGeneratorLayout()


if __name__ == '__main__':
    PasswordGeneratorApp().run()
