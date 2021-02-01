from init import *
from tkinter import *
from tkinter.ttk import Notebook
from sympy import *


r"""
1. DEBIT UNIDIRECTIONNEL STABLE
    1.1. Aquifere confine:
        "$h = -\frac{vx}{K}$"

    1.2. Aquifere non confine:
        "$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$"

    1.3. Flux de base vers un flux:
        "$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"

        "$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"

        "$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$"

        "$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$"

2. FLUX RADIAL CONSTANT VERS UN PUITS
    2.1. Aquifere confine:
        "$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"

        "$T = Kb = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$"

    2.2. Aquifere non confine:
        "$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"

        "$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"

        "$T \cong K\frac{h_1+h_2}{2}$"
        
    2.3. Aquifere non confine avec recharge uniforme:
        "$Q = -\pi r^2 W + C$"

        "$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi K}ln\left(\frac{r_0}{r}\right)$"
        
3. BIEN DANS UN FLUX UNIFORME
    "$K = \frac{2Q}{\pi r(h_u+h_d)(i_u+i_d)}$"

    "$y_L =  \pm \frac{Q}{2Kbi}$"
    
    "$x_L = -\frac{Q}{2\pi Kbi}$"

4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.1. Equation de pompage de puits hors equilibre:
        "$s = \frac{114.6Q}{T}W(u)$"
        
        "$u = \frac{1.87r^2 S}{Tt}$" (t in days)
        
        "$u = \frac{2693r^2 S}{Tt}$" (t in minutes)
        
    4.2. Methode de solution de Theis:
        "$s = \left( \frac{Q}{4\pi T}\right) W\left(u\right)$"

        "$\frac{r^2}{t} = \left(\frac{4T}{S}\right)u$"

    4.3. Methode de solution de Cooper-Jacob:
        "$S = \frac{2.246Tt_0}{r^2}$"

        "$T = \frac{2.303Q}{4\pi \Delta s}$"

    4.4. Methode de solution de Chow:
        "$F\left(u\right) = \frac{s}{\Delta s}$"

5. FLUX RADIAL INSTANTANE DANS UN AQUIFERE NON CONFINE
    "$s = \frac{Q}{4\pi T}W\left(u_a, u_y, \eta \right)$"

    "$u_a = \frac{r^2 S}{4Tt}$"

    "$u_y = \frac{r^2 S_y}{4Tt}$"

    "$\eta = \frac{r^2 K_z}{b^2 K_h}$"
    
6. FLUX RADIAL INSTANTANE DANS UN AQUIFERE FUISABLE
    "$s = \frac{Q}{4\pi T}W\left(u, \frac{r}{B} \right)$"

    "$u = \frac{r^2 S}{4Tt}$"

    "$\frac{r}{B} = \frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}}$"
    
7. PUITS FJOW PRES D'UNE LIMITE IMPERMEABLE
    "$s_b = \frac{Q}{4\pi T}W\left(u_p\right) + \frac{Q}{4\pi T}W\left(u_i\right)$"

    "$u_p = \frac{r^2_p S}{4Tt_p}$"

    "$u_i = \frac{r^2_i S}{4Tt_i}$"


"""
'''
### version 3.0.0.1 bêta
1. commencer à inclure de nouvelles relations dans l'application
'''
__author__ = 'NORA NAJMI'
__version__ = '3.0.0.1 bêta'
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

sn = SmallNumbers(10)


class HIGH_MASTER(Tk):
    def __init__(self):
        super(HIGH_MASTER, self).__init__()
        self.iconify()
        self.minsize(width=1133, height=500)
        self.title(u"%s v%s" % (__title__, __version__))
        self.configure(background='#212121')

        classes = [DEBIT_UNIDIRECTIONNEL_STABLE,
                   FLUX_RADIAL_CONSTANT_VERS_UN_PUITS,
                   BIEN_DANS_UN_FLUX_UNIFORME,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE]
        cls_name = ['DEBIT UNIDIRECTIONNEL STABLE',
                    'FLUX RADIAL CONSTANT VERS UN PUITS',
                    'BIEN DANS UN FLUX UNIFORME',
                    'FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE']

        self.NoteBook = Notebook(self)
        self.NoteBook.grid(row=0, column=0, sticky=NSEW)
        for nb in range(len(classes)):
            cls = classes[nb]
            self.NoteBook.add(cls(), text=cls_name[nb])

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.deiconify()
        self.mainloop()


class GUI_MASTER(Frame):
    def __init__(self, master, Application, function_text, si_text, savedraw):
        super(GUI_MASTER, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.automatic = True

        self.frame1 = Frame(self, background='#212121', relief='flat')
        self.frame1.grid(row=0, column=0, sticky=NSEW)
        self.frame1.rowconfigure(0, weight=1)

        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=16, savedraw=savedraw + 2, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self)
        self.TkAggXY.grid(row=0, column=1, rowspan=2, sticky=NSEW)

        self.TkAggXY.ToolBar.delete_state(self.automatic)

        self.frame2 = Frame(self)
        self.frame2.grid(row=1, column=0, sticky=NSEW)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.columnconfigure(2, weight=1)

        self.entry = []
        label_function = []
        label_si = []

        for sd in range(len(function_text)):
            label_function.append(Label(self.frame1, text=function_text[sd], **lbl_prm))
            label_function[sd].grid(row=sd, column=0, sticky=NSEW)

            self.entry.append(Entry(self.frame1, **ent_prm))
            self.entry[sd].grid(row=sd, column=1, sticky=EW)

            label_si.append(Label(self.frame1, text=si_text[sd], **si_prm))
            label_si[sd].grid(row=sd, column=2, sticky=NSEW)

            self.frame1.rowconfigure(sd, weight=1)

        self.entry[0].focus_set()

        self.button = []
        cbtn_text = ["Effacer", "Automatique", "Calculer"]
        for er in range(len(cbtn_text)):
            self.button.append(HoverButton(self.frame2, **btn_prm, text=cbtn_text[er]))
            self.button[er].grid(row=0, column=er, sticky=NSEW)

        self.button[0].configure(command=lambda: self.Delete())

        self.button[1].configure(fg='#FF9950', activeforeground='orange', command=lambda: self.Switcher())
        self.button[1].change_color_bind(DefaultBG='#737373', HoverBG='#696969', ActiveBG='#5F5F5F')

        self.button[2].configure(bg='#20B645', activebackground='#00751E', command=lambda: Application())
        self.button[2].change_color_bind(DefaultBG='#20B645', HoverBG='#009C27', ActiveBG='#00751E')

        self.LaTexT(f'{__author__} Master HIGH 2020/2021')

        self.LaTexT(f"Chapiter 4 : {__title__}")

    def LaTexT(self, LaTexT):
        self.FigureXY.DrawLaTex(LaTexT)

    def Draw(self):
        self.FigureXY.Draw()

    def Switcher(self):
        if self.automatic:
            self.button[1]['text'] = 'Manuel'
            self.automatic = False
        elif not self.automatic:
            self.button[1]['text'] = 'Automatique'
            self.automatic = True

        self.TkAggXY.ToolBar.delete_state(self.automatic)

    def Delete(self):
        if self.automatic:
            self.FigureXY.Clear()
        for cf in range(len(self.entry)):
            self.entry[cf].delete(0, END)

    def Clear(self):
        if self.automatic:
            self.Delete()


class DEBIT_UNIDIRECTIONNEL_STABLE(Frame):
    def __init__(self):
        super(DEBIT_UNIDIRECTIONNEL_STABLE, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [DEBIT_UNIDIRECTIONNEL_STABLE_1,
                   DEBIT_UNIDIRECTIONNEL_STABLE_2,
                   DEBIT_UNIDIRECTIONNEL_STABLE_3]
        cls_name = ['Aquifere confine',
                    'Aquifere non confine',
                    'Flux de base vers un flux']

        self.NoteBook = Notebook(self)
        self.NoteBook.grid(row=0, column=0, sticky=NSEW)
        for nb in range(len(classes)):
            cls = classes[nb]
            self.NoteBook.add(cls(), text=cls_name[nb])


class DEBIT_UNIDIRECTIONNEL_STABLE_1(Frame):
    def __init__(self):
        super(DEBIT_UNIDIRECTIONNEL_STABLE_1, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["vitesse (v)",
                         "Distance (x)",
                         "Permiabilite (K)"]
        si_text = ["m??", "m", "m/s?"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("1. DEBIT UNIDIRECTIONNEL STABLE:")

        self.LaTexT("1.1. Aquifere confine:")

        self.Draw()

    def Application(self):
        v = eval(str(self.entry[0].get()))
        x = eval(str(self.entry[1].get()))
        K = eval(str(self.entry[2].get()))

        # h = "- (v * x) / K"
        h = f"- ({v} * {x}) / {K}"

        self.Clear()

        self.LaTexT(f"Nappe Captive ({TeX('h')}):")
        self.LaTexT(r"$h = -\frac{vx}{K}$"f" = {App(h)} = {Num(h)}")

        r"""

    1.1. Aquifere confine:
        "$h = -\frac{vx}{K}$"
"""
        self.Draw()


class DEBIT_UNIDIRECTIONNEL_STABLE_2(Frame):
    def __init__(self):
        super(DEBIT_UNIDIRECTIONNEL_STABLE_2, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Hauteur Piezometrique (h)",
                         f"Hauteur Piezometrique (h{sn(0)})",
                         "Distance (x)",
                         "Permiabilite (K)"]
        si_text = ["m", "m", "m", "m/s?"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("1. DEBIT UNIDIRECTIONNEL STABLE:")

        self.LaTexT("1.2. Aquifere non confine:")

        self.Draw()

    def Application(self):
        h = eval(str(self.entry[0].get()))
        h0 = eval(str(self.entry[1].get()))
        x = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))

        # q = f"( K / ( 2 * x )) * ( h0 ** 2 - h ** 2 )"
        q = f"( {K} / ( 2 * {x} )) * ( {h0} ** 2 - {h} ** 2 )"

        self.Clear()

        self.LaTexT(f"Vitesse Darcy ({TeX('q')}):")
        self.LaTexT(r"$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$"f" = {App(q)} = {Num(q)}")

        r"""
    1.2. Aquifere non confine:
        "$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$"
"""
        self.Draw()


class DEBIT_UNIDIRECTIONNEL_STABLE_3(Frame):
    def __init__(self):
        super(DEBIT_UNIDIRECTIONNEL_STABLE_3, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la riviere 1 (h₁)",
                         "Niveau d'eau de la riviere 2 (h₂)",
                         "Distance (L)",
                         "Distance (x)",
                         "Permeabilite (K)",
                         "Recharge (W)"]
        si_text = ["m", "m", "m", "m", "m/j", "m/an"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("1. DEBIT UNIDIRECTIONNEL STABLE:")

        self.LaTexT("1.3. Flux de base vers un flux:")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        L = eval(str(self.entry[2].get()))
        x = eval(str(self.entry[3].get()))
        K = eval(str(self.entry[4].get()))
        W = eval(str(self.entry[5].get()))

        # qx = f"((((h1**2)-(h2**2))*K)/(2*L))-W*((L/2)-x)"
        qx = f"( ( ( ({h1} ** 2) - ({h2} ** 2) ) * {K}) / (2 * {L}) ) - ({W} * (( {L} / 2 ) - {x}))"

        # d = "(L / 2) - ((K / W) * (((h1 ** 2) - (h2 ** 2)) / (2 * L)))"
        d = f"({L} / 2) - (({K} / {W}) * ((({h1} ** 2) - ({h2} ** 2)) / (2 * {L})))"

        # hmax = "sqrt((h1 ** 2) - ((((h1 ** 2) - (h2 ** 2)) * d) / L) + ((K / W) * (L - d) * d))"
        hmax = f"sqrt(({h1}**2)-(((({h1}**2)-({h2}**2))*{Num(d, 3)})/{L})+(({K}/{W})*({L}-{Num(d, 3)})*{Num(d, 3)}))"

        self.Clear()

        self.LaTexT(f'Debit quotidien par Kilometer de la nappe vers les deus rivieres ({TeX("q_x")}):')
        self.LaTexT(r"$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$")
        self.LaTexT(f"{TeX('q_x')} = {App(qx)}")
        self.LaTexT(f"{TeX('q_x')} = {Num(qx)}")

        self.LaTexT(f"Localisation de la ligne de partage d'eau souterraine ({TeX('d')}):")
        self.LaTexT(r"$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$")
        self.LaTexT(f"{TeX('d')} = {App(d)}")
        self.LaTexT(f"{TeX('d')} = {Num(d)}")

        self.LaTexT(f"Hauteur Piezometrique maximale au niveau de la ligne de partage d'eau ({TeX('h_{max}')}):")
        self.LaTexT(r"$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$")
        self.LaTexT(r"$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$")
        self.LaTexT(f"{TeX('h_{max}')} = {App(hmax)}")
        self.LaTexT(f"{TeX('h_{max}')} = {Num(hmax)}")

        r"""
    1.3. Flux de base vers un flux:
        "$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"

        "$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"

        "$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$"

        "$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$"
"""
        self.Draw()


class FLUX_RADIAL_CONSTANT_VERS_UN_PUITS(Frame):
    def __init__(self):
        super(FLUX_RADIAL_CONSTANT_VERS_UN_PUITS, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_1,
                   FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_2,
                   FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_3]
        cls_name = ['Aquifere confine',
                    'Aquifere non confine',
                    'Aquifere non confine avec recharge uniforme']

        self.NoteBook = Notebook(self)
        self.NoteBook.grid(row=0, column=0, sticky=NSEW)
        for nb in range(len(classes)):
            cls = classes[nb]
            self.NoteBook.add(cls(), text=cls_name[nb])


class FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_1(Frame):
    def __init__(self):
        super(FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_1, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la riviere 1 (h₁|h)",
                         "Niveau d'eau de la riviere 2 (h₂|h𝓌)",
                         "Distance (r₁|r)",
                         "Distance (r₂|r𝓌)",
                         "Permeabilite (K)",
                         " ?? (b)"]
        si_text = ["m", "m", "m", "m", "m/j", "m/an"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:")

        self.LaTexT("2.1. Aquifere confine:")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        r2 = eval(str(self.entry[3].get()))
        K = eval(str(self.entry[4].get()))
        b = eval(str(self.entry[5].get()))

        # Q = "2 * pi * K * b * ((h2 - h1) / (log(r2 / r1)))"
        Q = f"{2} * {pi} * {K} * {b} * (({h2} - {h1}) / (log({r2} / {r1})))"

        # T1 = "K * b"
        T1 = f"{K} * {b}"

        # T2 = "(Q /(2 * pi * (h2 - h1))) * (log(r2 / r1))"
        T2 = f"({Num(Q, 3)} /({2} * pi * ({h2} - {h1}))) * (log({r2} / {r1}))"

        self.Clear()

        self.LaTexT(r"$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$")
        self.LaTexT(f"{TeX('Q')} = {App(Q)}")
        self.LaTexT(f"{TeX('Q')} = {Num(Q)}")

        self.LaTexT(r"$T = Kb$"f" = {App(T1)} = {Num(T1)}")
        self.LaTexT(r"$T = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$")
        self.LaTexT(f"{TeX('T')} = {App(T2)}")
        self.LaTexT(f"{TeX('T')} = {Num(T2)}")

        r"""
2. FLUX RADIAL CONSTANT VERS UN PUITS:
    2.1. Aquifere confine:
        "$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"

        "$T = Kb = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$"
"""
        self.Draw()


class FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_2(Frame):
    def __init__(self):
        super(FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_2, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la riviere 1 (h₁|h)",
                         "Niveau d'eau de la riviere 2 (h₂|h𝓌)",
                         "Distance (r₁|r)",
                         "Distance (r₂|r𝓌)",
                         "Permeabilite (K)"]
        si_text = ["m", "m", "m", "m", "m/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:")

        self.LaTexT("2.2. Aquifere non confine:")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        r2 = eval(str(self.entry[3].get()))
        K = eval(str(self.entry[4].get()))

        # Q = "pi * K * ((h2 ** 2 - h1 ** 2) / (log(r2 / r1)))"
        Q = f"pi * {K} * (({h2 ** 2} - {h1 ** 2}) / (log({r2} / {r1})))"

        # K = "(Q /(pi * (h2 ** 2 - h1 ** 2))) * (log(r2 / r1))"
        K = f"({Num(Q, 3)} /(pi * ({h2} ** 2 - {h1} ** 2))) * (log({r2} / {r1}))"

        # T = K * ((h1 + h2) / 2)
        T = f"{K} * (({h1} + {h2}) / 2)"

        self.Clear()

        self.LaTexT(r"$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$")
        self.LaTexT(f"{TeX('Q')} = {App(Q)}")
        self.LaTexT(f"{TeX('Q')} = {Num(Q)}")

        self.LaTexT(r"$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$")
        self.LaTexT(f"{TeX('K')} = {App(K)}")
        self.LaTexT(f"{TeX('K')} = {Num(K)}")

        self.LaTexT(r"$T \cong K\frac{h_1+h_2}{2}$")
        self.LaTexT(f"{TeX('T')} = {App(T)}")
        self.LaTexT(f"{TeX('T')} = {Num(T)}")

        r"""
    2.2. Aquifere non confine:
        "$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"

        "$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"

        "$T \cong K\frac{h_1+h_2}{2}$"
"""
        self.Draw()


class FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_3(Frame):
    def __init__(self):
        super(FLUX_RADIAL_CONSTANT_VERS_UN_PUITS_3, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Distance (r)",
                         f"Distance (r{sn(0)})",
                         "Permeabilite (K)",
                         "Recharge (W)",
                         " ?? (C)"]
        si_text = ["m", "m", "m/j", "m/an", "??"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:")

        self.LaTexT("2.3. Aquifere non confine avec recharge uniforme:")

        self.Draw()

    def Application(self):
        r = eval(str(self.entry[0].get()))
        r0 = eval(str(self.entry[1].get()))
        K = eval(str(self.entry[2].get()))
        W = eval(str(self.entry[3].get()))
        C = eval(str(self.entry[4].get()))

        # Q = pi * r ** 2 * W + C
        Q = f"{pi} * {r} ** 2 * {W} + {C}"

        # h0h = (W / (2 * K)) * (r ** 2 - r0 ** 2) + (Num(Q, 3) / (pi * K)) * log(r0 / r)
        h0h = f"({W} / (2 * {K})) * ({r} ** 2 - {r0} ** 2) + ({Num(Q, 3)} / (pi * {K})) * log({r0} / {r})"

        self.Clear()

        self.LaTexT(r"$Q = -\pi r^2 W + C$")
        self.LaTexT(f"{TeX('Q')} = {App(Q)}")
        self.LaTexT(f"{TeX('Q')} = {Num(Q)}")

        self.LaTexT(r"$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi K}ln\left(\frac{r_0}{r}\right)$")
        self.LaTexT(f"{TeX('h^2_0-h^2')} = {App(h0h)}")
        self.LaTexT(f"{TeX('h^2_0-h^2')} = {Num(h0h)}")

        r"""
    2.3. Aquifere non confine avec recharge uniforme:
        "$Q = -\pi r^2 W + C$"

        "$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi K}ln\left(\frac{r_0}{r}\right)$"
"""
        self.Draw()


class BIEN_DANS_UN_FLUX_UNIFORME(Frame):
    def __init__(self):
        super(BIEN_DANS_UN_FLUX_UNIFORME, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la riviere 1 (hᵤ)",
                         "Niveau d'eau de la riviere 2 (h𝒹)",
                         "Distance (r)",
                         "Permeabilite (K)",
                         " ?? (Q)",
                         " ?? (iᵤ|i) ??",
                         " ?? (i𝒹)",
                         " ?? (b)"]
        si_text = ["m", "m", "m", "m/j", "??", "??", "??", "??"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=1)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("3. BIEN DANS UN FLUX UNIFORME:")

        self.Draw()

    def Application(self):
        hu = eval(str(self.entry[0].get()))
        hd = eval(str(self.entry[1].get()))
        r = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))
        iu = eval(str(self.entry[5].get()))
        id = eval(str(self.entry[6].get()))
        b = eval(str(self.entry[7].get()))

        # K = (2 * Q) / (pi * r * (hu + hd) * (iu + id))
        K = f"(2 * {Q}) / (pi * {r} * ({hu} + {hd}) * ({iu} + {id}))"

        # yl = Q / (2 * K * b * iu)
        yl = f"{Q} / (2 * {Num(K, 3)} * {b} * {iu})"

        # xl = - Q / (2 * pi * K * b * iu)
        xl = f"- {Q} / (2 * pi * {Num(K, 3)} * {b} * {iu})"

        self.Clear()

        self.LaTexT(r"$K = \frac{2Q}{\pi r(h_u+h_d)(i_u+i_d)}$")
        self.LaTexT(f"{TeX('K')} = {App(K)}")
        self.LaTexT(f"{TeX('K')} = {Num(K)}")

        self.LaTexT(r"$y_L =  \pm \frac{Q}{2Kbi}$")
        self.LaTexT(f"{TeX('y_L')} = {App(yl)}")
        self.LaTexT(f"{TeX('y_L')} = {Num(yl)}")

        self.LaTexT(r"$x_L = -\frac{Q}{2\pi Kbi}$")
        self.LaTexT(f"{TeX('x_L')} = {App(xl)}")
        self.LaTexT(f"{TeX('x_L')} = {Num(xl)}")

        r"""
3. BIEN DANS UN FLUX UNIFORME
    "$K = \frac{2Q}{\pi r(h_u+h_d)(i_u+i_d)}$"

    "$y_L =  \pm \frac{Q}{2Kbi}$"
    
    "$x_L = -\frac{Q}{2\pi Kbi}$"
"""
        self.Draw()


class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE(Frame):
    def __init__(self):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1,]
                   # FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2,
                   # FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3,
                   # FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_4]
        cls_name = ['Equation de pompage de puits hors equilibre',
                    'Methode de solution de Theis',
                    'Methode de solution de Cooper-Jacob',
                    'Methode de solution de Chow']

        self.NoteBook = Notebook(self)
        self.NoteBook.grid(row=0, column=0, sticky=NSEW)
        for nb in range(len(classes)):
            cls = classes[nb]
            self.NoteBook.add(cls(), text=cls_name[nb])


class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1(Frame):
    def __init__(self):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1, self).__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la riviere 1 (hᵤ)",
                         "Niveau d'eau de la riviere 2 (h𝒹)",
                         "Distance (r)",
                         "Permeabilite (K)",
                         " ?? (Q)",
                         " ?? (iᵤ|i) ??",
                         " ?? (i𝒹)",
                         " ?? (b)"]
        si_text = ["m", "m", "m", "m/j", "??", "??", "??", "??"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, savedraw=2)
        self.Master.grid(row=0, column=0, sticky=NSEW)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw

        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

        self.LaTexT("4.1. Equation de pompage de puits hors equilibre:")

        self.Draw()

    def Application(self):
        hu = eval(str(self.entry[0].get()))
        hd = eval(str(self.entry[1].get()))
        r = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))
        iu = eval(str(self.entry[5].get()))
        id = eval(str(self.entry[6].get()))
        b = eval(str(self.entry[7].get()))

        # K = (2 * Q) / (pi * r * (hu + hd) * (iu + id))
        K = f"(2 * {Q}) / (pi * {r} * ({hu} + {hd}) * ({iu} + {id}))"

        # yl = Q / (2 * K * b * iu)
        yl = f"{Q} / (2 * {Num(K, 3)} * {b} * {iu})"

        # xl = - Q / (2 * pi * K * b * iu)
        xl = f"- {Q} / (2 * pi * {Num(K, 3)} * {b} * {iu})"

        self.Clear()

        self.LaTexT(r"$K = \frac{2Q}{\pi r(h_u+h_d)(i_u+i_d)}$")
        self.LaTexT(f"{TeX('K')} = {App(K)}")
        self.LaTexT(f"{TeX('K')} = {Num(K)}")

        self.LaTexT(r"$y_L =  \pm \frac{Q}{2Kbi}$")
        self.LaTexT(f"{TeX('y_L')} = {App(yl)}")
        self.LaTexT(f"{TeX('y_L')} = {Num(yl)}")

        self.LaTexT(r"$x_L = -\frac{Q}{2\pi Kbi}$")
        self.LaTexT(f"{TeX('x_L')} = {App(xl)}")
        self.LaTexT(f"{TeX('x_L')} = {Num(xl)}")

        r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.1. Equation de pompage de puits hors equilibre:
        "$s = \frac{114.6Q}{T}W(u)$"
        
        "$u = \frac{1.87r^2 S}{Tt}$" (t in days)
        
        "$u = \frac{2693r^2 S}{Tt}$" (t in minutes)
"""
        self.Draw()


if __name__ == '__main__':
    HIGH_MASTER()
