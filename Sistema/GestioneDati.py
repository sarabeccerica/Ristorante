import datetime
import os
import pickle
import time
from threading import Thread


class GestioneDati:

    def __init__(self):
        pass

    def backupSetup(self):
        t = Thread(target=self.avvioBackup, args=())
        t.start()
        h = Thread(target=self.scadenzaPrenotazioni, args=())
        h.start()
        g = Thread(target=self.inizioPrenotazioni, args=())
        g.start()

    def avvioBackup(self):
        momentoAvvio = datetime.datetime.now()
        momentoBackup = datetime.datetime(year=momentoAvvio.year, month=momentoAvvio.month, day=momentoAvvio.day,\
                                          hour=0, minute=0, second=0)
        notSleepTime = time.mktime(momentoAvvio.timetuple()) - time.mktime(momentoBackup.timetuple())
        sleepTime = (60*60*24)-notSleepTime
        time.sleep(sleepTime)
        self.backupPrenotazioni()
        self.backupDipendenti()
        self.backupScontrini()
        self.statisticheScontrini()
        self.statistichePrenotazioni()

    def backupPrenotazioni(self):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
        if os.path.isfile('Dati\BackupPrenotazioni.pickle'):
            with open('Dati\BackupPrenotazioni.pickle', 'rb') as f:
                backUpPrenotazioni = dict(pickle.load(f))
                for prenotazione in prenotazioni.keys():
                    if not(prenotazione in backUpPrenotazioni.keys()):
                        backUpPrenotazioni[prenotazione] = prenotazioni[prenotazione]
        with open('Dati\BackupPrenotazioni.pickle', 'wb') as f:
            pickle.dump(backUpPrenotazioni, f, pickle.HIGHEST_PROTOCOL)

    def backupDipendenti(self):
        backUpCamerieri = {}
        backUpCuochi = {}
        if os.path.isfile('Dati\Camerieri.pickle'):
            with open('Dati\Camerieri.pickle', 'rb') as f:
                camerieri = dict(pickle.load(f))
        if os.path.isfile('Dati\BackupCamerieri.pickle'):
            with open('Dati\BackupCamerieri.pickle', 'rb') as f:
                backUpCamerieri = dict(pickle.load(f))
                for cameriere in camerieri.keys():
                    if not(cameriere in backUpCamerieri.keys()):
                        backUpCamerieri[cameriere] = camerieri[cameriere]
        with open('Dati\BackupCamerieri.pickle', 'wb') as f:
            pickle.dump(backUpCamerieri, f, pickle.HIGHEST_PROTOCOL)
        if os.path.isfile('Dati\Cuochi.pickle'):
            with open('Dati\Cuochi.pickle', 'rb') as f:
                cuochi = dict(pickle.load(f))
        if os.path.isfile('Dati\BackupCuochi.pickle'):
            with open('Dati\BackupCuochi.pickle', 'rb') as f:
                backUpCuochi = dict(pickle.load(f))
                for cuoco in cuochi.keys():
                    if not(cuoco in backUpCuochi.keys()):
                        backUpCuochi[cuoco] = cuochi[cuoco]
        with open('Dati\BackupCuochi.pickle', 'wb') as f:
            pickle.dump(backUpCuochi, f, pickle.HIGHEST_PROTOCOL)

    def backupScontrini(self):
        if os.path.isfile('Dati\Scontrini.pickle'):
            with open('Dati\Scontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
        if os.path.isfile('Dati\BackupScontrini.pickle'):
            with open('Dati\BackupScontrini.pickle', 'rb') as f:
                backUpScontrini = dict(pickle.load(f))
                for scontrino in scontrini.keys():
                    if not(scontrino in backUpScontrini.keys()):
                        backUpScontrini[scontrino] = scontrini[scontrino]
        with open('Dati\BackupScontrini.pickle', 'wb') as f:
            pickle.dump(backUpScontrini, f, pickle.HIGHEST_PROTOCOL)

    def statisticheScontrini(self):
        statistiche = {}
        if os.path.isfile('Dati\BackupScontrini.pickle'):
            with open('Dati\BackupScontrini.pickle', 'rb') as f:
                scontrini = dict(pickle.load(f))
        incasso = self.calcoloIncasso(scontrini)
        scontrinoMedio = incasso/self.numeroScontrini(scontrini)
        if os.path.isfile('Dati\StatisticheScontrini.pickle'):
            with open('Dati\StatisticheScontrini.pickle', 'rb') as f:
                statistiche = dict(pickle.load(f))
        dataOggi = datetime.datetime.today()
        oggi = str(dataOggi.day) +"/"+ str(dataOggi.month) +"/"+ str(dataOggi.year)
        statistiche["Incasso giornaliero"] = dict()
        statistiche["Incasso giornaliero"][oggi] = incasso
        statistiche["Media scontrino giornaliera"] = dict()
        statistiche["Media scontrino giornaliera"][oggi] = scontrinoMedio
        i = 0
        statistiche["Scontrino medio"] = 0
        for mediaGiorno in statistiche["Media scontrino giornaliera"].values():
            statistiche["Scontrino medio"] += int(mediaGiorno)
            i+=1
        statistiche["Scontrino medio"] = statistiche["Scontrino medio"]/i
        with open('Dati\StatisticheScontrini.pickle', 'wb') as f:
            pickle.dump(statistiche, f, pickle.HIGHEST_PROTOCOL)

    def calcoloIncasso(self, scontrini):
        totale = 0
        for scontrino in scontrini.values():
            totale += scontrino.totale
        return totale

    def numeroScontrini(self, scontrini):
        return len(scontrini)

    def statistichePrenotazioni(self):
        statistiche ={}
        if os.path.isfile('Dati\BackupPrenotazioni.pickle'):
            with open('Dati\BackupPrenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
        totalePersone = self.calcoloPersonePrenotate(prenotazioni)
        if os.path.isfile('Dati\StatistichePrenotazioni.pickle'):
            with open('Dati\StatistichePrenotazioni.pickle', 'rb') as f:
                statistiche = dict(pickle.load(f))
        statistiche ["Persone Prenotate"] = totalePersone
        if len(prenotazioni):
            statistiche ["Media persone per prenotazione"] = totalePersone/len(prenotazioni)
        else:
            statistiche["Media persone per prenotazione"] = 0
        with open('Dati\StatistichePrenotazioni.pickle', 'wb') as f:
            pickle.dump(statistiche, f, pickle.HIGHEST_PROTOCOL)

    def calcoloPersonePrenotate(self, prenotazioni):
        totale = 0
        for prenotazione in prenotazioni.values():
            totale += prenotazione.numeroPersone
        return totale


    def inizioPrenotazioni(self):
        sleepTime = 30
        time.sleep(sleepTime)
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
        for prenotazione in prenotazioni.values():
            if time.mktime(prenotazione.dataOra.timetuple())<= (time.mktime(datetime.datetime.now().timetuple()) + sleepTime):
                for tavolo in prenotazione.tavoliAssociati:
                    tavolo.modificaStatoTavolo(tavolo.numero, "Prenotato")

    def scadenzaPrenotazioni(self):
        sleepTime = 30
        time.sleep(sleepTime)
        prenotazioni = {}
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
        for prenotazione in prenotazioni.values():
            if time.mktime(prenotazione.dataOra.timetuple())<= (time.mktime(datetime.datetime.now().timetuple()) - sleepTime) and\
                    prenotazione.tavoliAssociati[0].stato =="Prenotato":
                for tavolo in prenotazione.tavoliAssociati:
                    tavolo.modificaStatoTavolo(tavolo.numero, "Libero")
                prenotazione.eliminaPrenotazione(prenotazione.nome)
        self.scadenzaPrenotazioni()
