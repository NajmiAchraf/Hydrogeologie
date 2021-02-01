from init import *
from tkinter import *
from tkinter.ttk import Notebook
from sympy import *
'''
### version 2.0.0.1 RC
1. switcher l'interface graphique vers le Notebook

2. amélioration du script
'''
r"""
Écoulement Permanent Unidirectionnel:
    Nappe Captive: "$v = \frac{h.k}{x}$"
    
    Nappe Libre: "$q = \frac{k}{2x}({h_0^2-h^2})$"
    
Étiage:
    Localisation de la ligne\nde partage d'eau souterraine (d):
        "$d = \frac{L}{2}-\frac{K}{W}\frac{({h_0^2-h^2})}{2L}$"
        
    Hauteur Piezometrique maximale au\nniveau de la ligne de partage d'eau $({h_{max}})$:
        "$h_{max} = \sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{K}{W}(L-d)d}$"
        
    Temps de deplacement a partir la ligne\nde partage d'eau souterraine vers les\ndeux rivieres (t):
        "$t_a=\frac{L_a}{v_a}=\frac{L_a}{(\frac{k}{n})(\frac{\Delta h}{\Delta x})}$"
        
    Debit quotidien par Kilometer de\nla nappe vers les deus rivieres (q):
        "$q=\frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x)$"
"""

__author__ = 'NORA NAJMI'
__version__ = '2.0.0.1 RC'
__title__ = 'Hydrogéologie'

btn_prm = {'padx': 18,
           'pady': 1,
           'bd': 1,
           'background': 'firebrick2',
           'fg': 'white',
           'bg': 'firebrick2',
           'font': ('DejaVu Sans', 14),
           'width': 2,
           'height': 1,
           'relief': 'raised',
           'activeback': 'firebrick3',
           'activebackground': 'firebrick4',
           'activeforeground': "white"}
sml_prm = {'fg': 'white',
           'bg': '#212121',
           'selectcolor': '#212121',
           'font': ('DejaVu Sans', 14),
           'relief': 'flat',
           'activebackground': '#212121',
           'activeforeground': "#F0F0F0"}
ent_prm = {'fg': 'black',
           'bg': 'white',
           'width': '12',
           'font': ('DejaVu Sans', 14),
           'relief': 'flat'}
lbl_prm = {'fg': 'white',
           'bg': '#212121',
           'width': 26,
           'justify': LEFT,
           'font': ('DejaVu Sans', 14),
           'relief': 'flat'}
si_prm = {'fg': 'white',
          'bg': '#212121',
          'width': 4,
          'justify': LEFT,
          'font': ('DejaVu Sans', 14),
          'relief': 'flat'}



class Fluid(Tk):
    def __init__(self):
        super(Fluid, self).__init__()
        self.iconify()
        self.minsize(width=1111, height=500)
        self.title(u"%s v%s" % (__title__, __version__))
        self.configure(background='#212121')

        self.NoteBook = Notebook(self)
        self.NoteBook.grid(row=0, column=0, sticky=NSEW)
        self.NoteBook.add(EcoulementPermanentUnidirectionnel(), text="Écoulement Permanent Unidirectionnel")
        self.NoteBook.add(Etiage(), text="Étiage")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.deiconify()
        self.mainloop()


class EcoulementPermanentUnidirectionnel(Frame):
    def __init__(self):
        super(EcoulementPermanentUnidirectionnel, self).__init__()
        self.nappe = "Captive"
        self.porosite = True

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.RBV0 = StringVar()
        self.CKB0 = IntVar()

        self.RBV0.set("Nappe Captive")
        self.CKB0.set(0)

        self.frame1 = Frame(self, background='#212121', relief='flat')
        self.frame1.grid(row=0, column=0, sticky=NSEW)
        self.frame1.rowconfigure(0, weight=1)

        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=16, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self)
        self.TkAggXY.grid(row=0, column=1, rowspan=2, sticky=NSEW)

        self.frame2 = Frame(self)
        self.frame2.grid(row=1, column=0, sticky=NSEW)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        radio_button = []
        rb_text = ["Nappe Captive", "Nappe Libre"]
        for op in range(2):
            radio_button.append(
                Radiobutton(self.frame1, variable=self.RBV0, value=rb_text[op], **sml_prm, text=rb_text[op]))
            radio_button[op].grid(row=0, column=op, sticky=NSEW)
            radio_button[op].config(command=lambda: self.SwitchNappe())

        label = []
        lbl_text = ["Hauteur Piezometrique (h)",
                    "Hauteur Piezometrique (h₀)",
                    "Permiabilite (k)",
                    "Distance (x)"]

        for to in range(4):
            label.append(Label(self.frame1, text=lbl_text[to], **lbl_prm))
            label[to].grid(row=to + 1, column=0, sticky=NSEW)

        self.entry = []
        label_si = []
        text_si = ["m", "m", "m/s", "m", ""]
        for ty in range(5):
            self.entry.append(Entry(self.frame1, **ent_prm))
            self.entry[ty].grid(row=ty + 1, column=1, sticky=EW)

            label_si.append(Label(self.frame1, text=text_si[ty], **si_prm))
            label_si[ty].grid(row=ty + 1, column=2, sticky=NSEW)

            self.frame1.rowconfigure(ty + 1, weight=1)

        self.entry[0].focus_set()

        check_button = Checkbutton(self.frame1, variable=self.CKB0, **sml_prm, text="Porosite")
        check_button.grid(row=5, column=0, sticky=NSEW)
        check_button.configure(command=lambda: self.SwitchPorosite())

        button = []
        cbtn_text = ["Effacer", "Calculer"]
        for er in range(2):
            button.append(HoverButton(self.frame2, **btn_prm, text=cbtn_text[er]))
            button[er].grid(row=0, column=er, sticky=NSEW)
        button[0].configure(command=lambda: self.Clear())
        button[1].configure(bg='#20B645', activebackground='#00751E', command=lambda: self.Application())
        button[1].change_color_bind(DefaultBG='#20B645', HoverBG='#009C27', ActiveBG='#00751E')

        self.FigureXY.DrawLaTex(f'{__author__} Master HIGH 2019/2020')

        self.FigureXY.DrawLaTex("Calcule d'Écoulement Permanent Unidirectionnel:")

        self.FigureXY.Draw()

        self.SwitchNappe()
        self.SwitchPorosite()

    def SwitchNappe(self):
        etiage_mode = self.RBV0.get()

        if etiage_mode == "Nappe Libre":
            self.entry[1].delete(0, END)
            self.entry[1].configure(state=NORMAL, bg='white')
            self.nappe = "Libre"
        else:
            self.entry[1].configure(state='readonly', readonlybackground='#212121')
            self.nappe = "Captive"

    def SwitchPorosite(self):
        porosite_mode = self.CKB0.get()
        if porosite_mode == 0:
            self.entry[4].delete(0, END)
            self.entry[4].configure(state='readonly', readonlybackground='#212121')
            self.porosite = False
        else:
            self.entry[4].configure(state=NORMAL, bg='white')
            self.porosite = True

    def Application(self):
        h = eval(str(self.entry[0].get()))
        k = eval(str(self.entry[2].get()))
        x = eval(str(self.entry[3].get()))
        if self.nappe == "Captive":
            if not self.porosite:
                v = f"({h} * {k}) / {x}"
                self.FigureXY.DrawLaTex(r"Nappe Captive: $v = \frac{h.k}{x}$"f" = {App(v)} = {Num(v, 3)}")
                # Q =
                self.FigureXY.DrawLaTex(r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$"f" = {App(v)} = {Num(v, 3)}")
                lkio = [
                    r"Nappe Captive: $v=\frac{h.k}{x}$",
                    r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
                ]
            elif self.porosite:
                lopi = [
                    r"Nappe Captive: $v=\frac{h.k}{x}$",
                    r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
                    r"Vitesse reelle"
                ]
                # self.FigureXY.DrawLaTex()
                pass
        elif self.nappe == "Libre":
            h0 = eval(str(self.entry[1].get()))
            if not self.porosite:
                result = [
                    r'Nappe Captive: $v=\frac{h.k}{x}$',
                    r'Nappe Libre: $q=\frac{k}{2x}({h_0^2-h^2})$',
                    r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$"
                ]
                # self.FigureXY.DrawLaTex()
                pass
            elif self.porosite:
                prog = [
                    r'Nappe Captive: $v=\frac{h.k}{x}$',
                    r'Nappe Libre: $q=\frac{k}{2x}({h_0^2-h^2})$',
                    r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
                    r"Vitesse reelle"
                ]
                # self.FigureXY.DrawLaTex()
                pass

        bib = [f'{__author__} Master HIGH 2019/2020',
               'Écoulement Permanent Unidirectionnel:',
               r'Nappe Captive: $v=\frac{h.k}{x}$',

               r'Nappe Libre: $q=\frac{k}{2x}({h_0^2-h^2})$',
               r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
               r"Vitesse reelle"]

        self.FigureXY.Draw()
        self.Clear()

    def Clear(self):
        for ko in range(5):
            self.entry[ko].delete(0, END)


class Etiage(Frame):
    def __init__(self):
        super(Etiage, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.frame1 = Frame(self, background='#212121', relief='flat')
        self.frame1.grid(row=0, column=0, sticky=NSEW)
        self.frame1.rowconfigure(0, weight=1)

        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=16, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self)
        self.TkAggXY.grid(row=0, column=1, rowspan=2, sticky=NSEW)

        self.frame2 = Frame(self)
        self.frame2.grid(row=1, column=0, sticky=NSEW)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.entry = []
        label_function = []
        function_text = ["Niveau d'eau de la riviere 1 (h₁)",
                         "Niveau d'eau de la riviere 2 (h₂)",
                         "Distance (L)",
                         "Permeabilite (k)",
                         "Porosite (n)",
                         "Recharge (W)"]
        label_si = []
        si_text = ["m", "m", "m", "m/j", "", "m/an"]

        for sd in range(6):
            label_function.append(Label(self.frame1, text=function_text[sd], **lbl_prm))
            label_function[sd].grid(row=sd, column=0, sticky=NSEW)

            self.entry.append(Entry(self.frame1, **ent_prm))
            self.entry[sd].grid(row=sd, column=1, sticky=EW)

            label_si.append(Label(self.frame1, text=si_text[sd], **si_prm))
            label_si[sd].grid(row=sd, column=2, sticky=NSEW)

            self.frame1.rowconfigure(sd, weight=1)

        self.entry[0].focus_set()

        button = []
        cbtn_text = ["Effacer", "Calculer"]
        for er in range(2):
            button.append(HoverButton(self.frame2, **btn_prm, text=cbtn_text[er]))
            button[er].grid(row=0, column=er, sticky=NSEW)
        button[0].configure(command=lambda: self.Clear())
        button[1].configure(bg='#20B645', activebackground='#00751E', command=lambda: self.Application())
        button[1].change_color_bind(DefaultBG='#20B645', HoverBG='#009C27', ActiveBG='#00751E')

        self.FigureXY.DrawLaTex(f'{__author__} Master HIGH 2019/2020')

        self.FigureXY.DrawLaTex("Calcule d'Étiage:")

        self.FigureXY.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        L = eval(str(self.entry[2].get()))
        k = eval(str(self.entry[3].get()))
        n = eval(str(self.entry[4].get()))
        W = eval(str(self.entry[5].get()))

        # d = "(L / 2) - ((k / W) * (((h1 ** 2) - (h2 ** 2)) / (2 * L)))"
        d = f"({L} / 2) - (({k} / {W}) * ((({h1} ** 2) - ({h2} ** 2)) / (2 * {L})))"
        # hmax = "sqrt((h1 ** 2) - ((((h1 ** 2) - (h2 ** 2)) * d) / L) + ((k / W) * (L - d) * d))"
        hmax = f"sqrt(({h1}**2)-(((({h1}**2)-({h2}**2))*{Num(d)})/{L})+(({k}/{W})*({L}-{Num(d)})*{Num(d)}))"
        # ta =
        q = f"((((h1**2)-(h2**2))*d)/(2*L))-W((L/2)-x)"
        # q = f"(((({h1}**2)-({h2}**2))*{Num(d)})/(2*{L}))-{W}(({L}/2)-{x})"
        self.FigureXY.DrawLaTex("Localisation de la ligne de partage d'eau souterraine (d):")
        self.FigureXY.DrawLaTex(
            r"$d = \frac{L}{2}-\frac{k}{W}\frac{({h_1^2-h_2^2})}{2L}$"f" = {App(d)} = {Num(d, 3)}")
        self.FigureXY.DrawLaTex(
            "Hauteur Piezometrique maximale au niveau de la ligne de partage d'eau $({h_{max}})$:")
        self.FigureXY.DrawLaTex(
            r"$h_{max} = \sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{k}{W}(L-d)d}$"f" = {App(hmax)} = {Num(hmax)}")
        self.FigureXY.DrawLaTex(
            "Temps de deplacement a partir la ligne de partage d'eau souterraine vers les deux rivieres (t):")
        self.FigureXY.DrawLaTex(
            r"$t_a = \frac{L_a}{v_a} = \frac{L_a}{(\frac{k}{n})(\frac{\Delta h}{\Delta x})}$")
        self.FigureXY.DrawLaTex('Debit quotidien par Kilometer de la nappe vers les deus rivieres (q):')
        self.FigureXY.DrawLaTex(r"$q = \frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x)$"f" = {App(q)} = {Num(q)}")

        bib = [f'{__author__} Master HIGH 2019/2020',
               'Étiage:',
               "Localisation de la ligne de partage d'eau souterraine (d):",
               r"$d=\frac{L}{2}-\frac{K}{W}\frac{({h_0^2-h^2})}{2L}$",

               "Hauteur Piezometrique maximale au niveau de la ligne de partage d'eau $({h_{max}})$:",
               r"$h_{max} = \sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{K}{W}(L-d)d}$",

               "Temps de deplacement a partir la ligne de partage d'eau souterraine vers les deux rivieres (t):",
               r"$t_a=\frac{L_a}{v_a}=\frac{L_a}{(\frac{k}{n})(\frac{\Delta h}{\Delta x})}$",

               'Debit quotidien par Kilometer de la nappe vers les deux rivieres (q):',
               r"$q=\frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x)$"]

        self.FigureXY.Draw()
        self.Clear()

    def Clear(self):
        for cf in range(6):
            self.entry[cf].delete(0, END)


if __name__ == '__main__':
    Fluid()
