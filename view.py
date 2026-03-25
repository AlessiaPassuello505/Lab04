import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        self.__testo_messaggio=None
        self.__scelta_lingua=None

        self.__txt1 = ft.Text("")
        self.__scelta_modalita=None





        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        self.__scelta_lingua=ft.Dropdown(label="Seleziona la lingua",options=[ft.dropdown.Option("Italiano"),
                                                                              ft.dropdown.Option("Inglese"),
                                                                              ft.dropdown.Option("Spagnolo")],
        on_change=self.__controller.handle_language_change)
        self.__testo_messaggio=ft.Text("Nessuna lingua selezionata")
        self.page.controls.append(ft.Row(controls=[self.__scelta_lingua,self.__testo_messaggio]))



        self.__scelta_modalita = ft.Dropdown(label="Seleziona la modalità", options=[ft.dropdown.Option("Default"),
                                                                                 ft.dropdown.Option("Lineare"),
                                                                                 ft.dropdown.Option("Dicotonica")],
                                            on_change=self.__controller.handle_modality_change)
        self.__txt1=ft.Text("Nessuna modalità selezionata")

        self.__txtDaInserire=ft.TextField(label="Inserisci testo:",text_align="CENTER")
        self.__btnCorrezione=ft.ElevatedButton(label="Correzione automatica", on_click=self.__controller.handleSpellCheck)
        self.page.controls.append(ft.Row(controls=[self.__scelta_modalita,self.__txt1,self.__txtDaInserire,self.__btnCorrezione]))

        # Add your stuff here

        # self.page.add([])

        self.page.update()

    def update_lingua(self, messaggio):
        self.__testo_messaggio.value = messaggio
        self.__testo_messaggio.color = "green"
        self.page.update()

    def update_modalita(self, messaggio):
        self.__txt1.value = messaggio
        self.__txt1.color = "blue"
        self.page.update()

    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
