from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print("Tietokone valitsi: ", siirto)
        return siirto