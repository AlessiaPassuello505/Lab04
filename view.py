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
        self.__DaInserire=None
        self.__btnCorrezione=None

        self.__lv_output=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

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

        self.__txtDaInserire=ft.TextField(label="Inserisci testo:", expand=True)
        self.__btnCorrezione=ft.ElevatedButton(text="Correzione automatica", on_click=self.__controller.handleSpellCheck)
        self.page.controls.append(ft.Row(controls=[self.__scelta_modalita,self.__txt1,self.__txtDaInserire,self.__btnCorrezione]))

        output_container=ft.Container(content=self.__lv_output,margin=10,
                                      padding=10)
        self.page.controls.append(output_container)

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

        # ... (sotto update_modalita)

    def append_to_output(self, messaggio):
            """Aggiunge testo alla ListView e aggiorna la pagina"""
            self.__lv_output.controls.append(ft.Text(messaggio))
            self.page.update()

    def clear_input_field(self):
            """Pulisce il campo di testo"""
            self.__txtDaInserire.value = ""
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
