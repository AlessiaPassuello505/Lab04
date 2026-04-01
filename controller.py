import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        parole_risultato = []

        t1= time.time()
        if modality=="Default":
            parole = self._multiDic.searchWord(words, language)

        elif modality== "Lineare":
            parole = self._multiDic.searchWordLinear(words, language)

        elif modality=="Dicotonica":
            parole = self._multiDic.searchWordDichotomic(words, language)

        else:
                return "Modalità non valida",0

        for p in parole:
            if not p.corretta:
                parole_risultato.append(p._parola)

        t2=time.time()

        str_errate="-".join(parole_risultato) if parole_risultato else("Nessun errore")
        return str_errate, t2-t1


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handle_language_change(self, e):
        # Recuperiamo il valore
        nuova_lingua = e.control.value
        messaggio = f"Lingua selezionata: {nuova_lingua}"
        # Chiamiamo il metodo della view che aggiorna la riga della LINGUA
        self._view.update_lingua(messaggio)

    def handle_modality_change(self, e):
        # Recuperiamo il valore
        nuova_mod = e.control.value
        messaggio = f"Modalità selezionata: {nuova_mod}"
        # Chiamiamo il metodo della view che aggiorna la riga della MODALITÀ
        self._view.update_modalita(messaggio)

    def handleSpellCheck(self,e):
        lingua=self._view._View__scelta_lingua.value
        modalita=self._view._View__scelta_modalita.value
        testo_input=self._view._View__txtDaInserire.value

        #controllo validità campi
        if lingua is None or modalita is None or testo_input.strip()=="":
            self._view.append_to_output("Errore: Selezione lingua,modalità e inserisci testo non validi")
            return

        parole_errate, tempo=self.handleSentence(testo_input,lingua,modalita)

        self._view.append_to_output(f"Frase inserita:{testo_input}")
        self._view.append_to_output(f"Parole errate:{parole_errate}")
        self._view.append_to_output(f"Tempo impiegato :{tempo}")

        self._view.clear_input_field()



def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


