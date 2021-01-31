from tkinter import *
import tkinter as tk
from sympy import sqrt, sympify, latex
from sympy.parsing.sympy_parser import parse_expr
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
'''
### version 1.0.0.1 RC
1. Release Candidate contient deux parties:
    1. Écoulement Permanent Unidirectionnel
    
    2. Étiage
   
2. GUi d'application se compose de deux interfaces:
    1. la premiers interface contient des boutons de navigation et de control, des entree et des cadres des noms et des unités
    
    2. la deuxième interface contient la feuille du calcul
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


def LaTex(Math_Expression):
    TEX = '$' + latex(Math_Expression) + '$'
    return TEX


def App(character):
    try:
        pik = str(character)
        try:
            expression = parse_expr(pik, evaluate=False)
        except Exception:
            expression = sympify(pik, rational=True, evaluate=False)
        return LaTex(expression)
    except None:
        pass
    except Exception:
        pass


def Num(*args):
    try:
        if len(args) == 1 and isinstance(args[0], str):
            return sympify(args[0], evaluate=True).evalf()

        elif len(args) == 2:
            if isinstance(args[0], str) and isinstance(args[1], int):
                return sympify(args[0], evaluate=True).evalf(args[1])

            elif isinstance(args[0], int) and isinstance(args[1], str):
                return sympify(args[1], evaluate=True).evalf(args[0])
    except None:
        pass
    except Exception:
        pass


class HoverButton(tk.Button):
    def __init__(self, master=None, cnf=None, **kwargs):
        if cnf is None:
            cnf = {}
        cnf = tk._cnfmerge((cnf, kwargs))
        super(HoverButton, self).__init__(master=master, cnf=cnf, **kwargs)
        self.DBG = kwargs['background']
        self.ABG = kwargs['activeback']
        self.bind_class(self, "<Enter>", self.Enter)
        self.bind_class(self, "<Leave>", self.Leave)

    def Enter(self, event):
        self['bg'] = self.ABG

    def Leave(self, event):
        self['bg'] = self.DBG


class ScrollableTkAggXY(tk.Canvas):
    def __init__(self, figure, master, **kw):
        # --- create canvas with scrollbar ---
        super(ScrollableTkAggXY, self).__init__(master, **kw)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.fig_wrapper = tk.Frame(self)
        self.fig_wrapper.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper.rowconfigure(0, weight=1)
        self.fig_wrapper.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self.fig_wrapper)
        self.TkAggWidget = self.TkAgg.get_tk_widget()
        self.TkAggWidget.grid(row=0, column=0, sticky=tk.NSEW)

        self.vbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        self.hbar.grid(row=1, column=0, sticky=tk.EW)

        self.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set, scrollregion=self.bbox(tk.ALL))

        # --- put frame in canvas ---
        self.canvas_frame = self.create_window((0, 0), window=self.fig_wrapper, width=600, height=100, anchor=tk.NW)

    # expand canvas_frame when canvas changes its size
    def on_configure(self, width, height):
        # when all widgets are in canvas
        self.itemconfigure(self.canvas_frame, width=width, height=height)
        # update scrollregion after starting 'mainloop'
        self.configure(scrollregion=self.bbox(tk.ALL))
        self.yview_moveto(1)
        self.xview_moveto(0)

    def Draw(self, width, height):
        self.on_configure(width=width, height=height)
        self.TkAgg.draw()


class FigureXY(Figure):
    def __init__(self, fontsize, **kwargs):
        super(FigureXY, self).__init__(tight_layout=True, **kwargs)
        self.fontsize = fontsize
        self.Axes = self.add_subplot(1, 1, 1)
        self.Text = self.Axes.text(0, 1, '', fontsize=self.fontsize)
        self.latex_math = []
        self.size_w = [10]
        self.size_h = 10
        self.width = max(self.size_w)
        self.height = float(self.size_h)
        self.TkAggXY = ScrollableTkAggXY

    def DrawLaTex(self, character):
        self.latex_math.append(character)
        self.clear()
        n_lines = len(self.latex_math)
        # Gap between lines in axes coords
        self.Axes = self.add_subplot(1, 1, 1)
        self.Axes.set_ylim((0, n_lines))
        self.Axes.axis('off')
        self.Axes.set_xticklabels("", visible=False)
        self.Axes.set_yticklabels("", visible=False)

        # Plotting features formulae
        for i_line in range(0, n_lines):
            baseline = n_lines - i_line
            demo = self.latex_math[i_line]
            self.Text = self.Axes.text(0, baseline - 0.5, demo, fontsize=self.fontsize)

        Renderer = self.canvas.get_renderer()
        bb = self.Text.get_window_extent(renderer=Renderer)
        self.size_w.append((int(bb.width) + 65))
        self.size_h += (float(bb.height) * 2) + 20

        self.width = max(self.size_w)
        self.height = float(self.size_h)
        try:
            self.tight_layout(renderer=Renderer)
        except Exception:
            pass

    def InputTkAggXY(self, TkAgg):
        """

        :param TkAgg: set the ScrollableTkAggXY before call Draw from the FigureXY
        :return:
        """
        self.TkAggXY = TkAgg

    def Draw(self):
        self.TkAggXY.Draw(width=self.width, height=self.height)

    def Clear(self):
        self.clear()
        self.latex_math = []
        self.size_w = [0]
        self.size_h = 0


class Fluid:
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
    big2_prm = {'padx': 14,
                'pady': 19,
                'bd': 1,
                'background': '#212121',
                'fg': 'white',
                'bg': '#212121',
                'font': ('DejaVu Sans', 12),
                'width': 4,
                'height': 1,
                'relief': 'raised',
                'activeback': '#49000A',
                'activebackground': '#80000B',
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

    def __init__(self):
        self.entry = []
        self.nappe = "Captive"
        self.mode = 'Ecoulement'
        self.porosite = True

        self.window = Tk()
        self.window.minsize(width=1100, height=500)
        self.window.title('Hydrogéologie v1.0.0.1 RC')
        self.window.configure(background='#212121')
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.RBV0 = StringVar()
        self.CKB0 = IntVar()

        self.frame0 = Frame(self.window)
        self.frame0.grid(row=0, column=0, sticky=NSEW)
        self.frame0.columnconfigure(0, weight=1)
        self.frame0.columnconfigure(1, weight=1)

        self.frame1 = Frame(self.window)

        self.FigureXY = FigureXY(figsize=(1, 1), fontsize=16, facecolor='#F0F0F0')
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self.window)
        self.TkAggXY.grid(row=0, column=1, rowspan=3, sticky=NSEW)
        self.FigureXY.InputTkAggXY(self.TkAggXY)

        self.frame2 = Frame(self.window)
        self.frame2.grid(row=2, column=0, sticky=NSEW)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.button = []
        mbtn_text = ["Écoulement Permanent\nUnidirectionnel", "Étiage"]
        cmd_text = ["Ecoulement", "Etiage"]
        for er in range(2):
            self.button.append(HoverButton(self.frame0, **self.big2_prm, text=mbtn_text[er],
                                           command=lambda sw=cmd_text[er]: self.SwitchMode(sw)))
            self.button[er].grid(row=0, column=er, sticky=NSEW)

        button = []
        cbtn_text = ["Effacer", "Calculer"]
        for er in range(2):
            button.append(HoverButton(self.frame2, **self.btn_prm, text=cbtn_text[er]))
            button[er].grid(row=0, column=er, sticky=NSEW)
        button[0].configure(command=lambda: self.Clear())
        button[1].configure(bg='#20B645', activebackground='#00751E', command=lambda: self.Application())
        button[1].ABG = '#009C27'
        button[1].DBG = '#20B645'

        self.SwitchMode("Ecoulement")

        self.window.mainloop()

    def SwitchMode(self, mode):
        self.mode = mode

        self.FigureXY.Clear()
        self.FigureXY.DrawLaTex('Nora NAJMI Master HIGH 2019/2020')

        self.frame1.destroy()
        self.frame1 = Frame(self.window, background='#212121', relief='flat')
        self.frame1.grid(row=1, column=0, sticky=NSEW)

        if self.mode == 'Ecoulement':
            self.FigureXY.DrawLaTex("Calcule d'Écoulement Permanent Unidirectionnel:")

            self.button[0].config(bg='#80000B', relief='sunken')
            self.button[0].DBG = '#80000B'
            self.button[1].config(bg='#212121', relief='raised')
            self.button[1].DBG = '#212121'

            self.frame1.rowconfigure(0, weight=1)

            self.EcoulementToPlay()

        elif self.mode == 'Etiage':
            self.FigureXY.DrawLaTex("Calcule d'Étiage:")

            self.button[0].config(bg='#212121', relief='raised')
            self.button[0].DBG = '#212121'
            self.button[1].config(bg='#80000B', relief='sunken')
            self.button[1].DBG = '#80000B'

            self.EtiageToPlay()

        self.FigureXY.Draw()

        self.entry[0].focus_set()

    def EcoulementToPlay(self):
        self.RBV0.set("Nappe Captive")

        radio_button = []
        rb_text = ["Nappe Captive", "Nappe Libre"]
        for op in range(2):
            radio_button.append(
                Radiobutton(self.frame1, variable=self.RBV0, value=rb_text[op], **self.sml_prm, text=rb_text[op]))
            radio_button[op].grid(row=0, column=op, sticky=NSEW)
            radio_button[op].config(command=lambda: self.SwitchNappe())

        self.entry = []
        lebel = []
        lbl_text = ["Hauteur Piezometrique (h)",
                    "Hauteur Piezometrique (h₀)",
                    "Permiabilite (k)",
                    "Distance (x)", '']
        lebel_si = []
        si_text = ["m", "m", "m/s", "m", ""]

        for ty in range(5):
            lebel.append(Label(self.frame1, text=lbl_text[ty], **self.lbl_prm))
            lebel[ty].grid(row=ty + 1, column=0, sticky=NSEW)

            self.entry.append(Entry(self.frame1, **self.ent_prm))
            self.entry[ty].grid(row=ty + 1, column=1, sticky=EW)

            lebel_si.append(Label(self.frame1, text=si_text[ty], **self.si_prm))
            lebel_si[ty].grid(row=ty + 1, column=2, sticky=NSEW)

            self.frame1.rowconfigure(ty + 1, weight=1)

        lebel[4].destroy()

        self.CKB0.set(0)
        check_button = Checkbutton(self.frame1, variable=self.CKB0, **self.sml_prm, text="Porosite")
        check_button.grid(row=5, column=0, sticky=NSEW)
        check_button.configure(command=lambda: self.SwitchPorosite())

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

    def EtiageToPlay(self):
        self.entry = []
        lebel_function = []
        function_text = ["Niveau d'eau de la riviere 1 (h₁)",
                         "Niveau d'eau de la riviere 2 (h₂)",
                         "Distance (L)",
                         "Permeabilite (k)",
                         "Porosite (n)",
                         "Recharge (W)"]
        lebel_si = []
        si_text = ["m", "m", "m", "m/j", "", "m/an"]

        for sd in range(6):
            lebel_function.append(Label(self.frame1, text=function_text[sd], **self.lbl_prm))
            lebel_function[sd].grid(row=sd, column=0, sticky=NSEW)

            self.entry.append(Entry(self.frame1, **self.ent_prm))
            self.entry[sd].grid(row=sd, column=1, sticky=EW)

            lebel_si.append(Label(self.frame1, text=si_text[sd], **self.si_prm))
            lebel_si[sd].grid(row=sd, column=2, sticky=NSEW)

            self.frame1.rowconfigure(sd, weight=1)

    def Application(self):
        if self.mode == 'Ecoulement':
            h = eval(str(self.entry[0].get()))
            k = eval(str(self.entry[2].get()))
            x = eval(str(self.entry[3].get()))
            if self.nappe == "Captive":
                if not self.porosite:
                    result = eval(str(h * k / x))
                    self.FigureXY.DrawLaTex(r'Nappe Captive: $v = \frac{h.k}{x}$'f' = {result}')
                    lkio = [
                        r'Nappe Captive: $v=\frac{h.k}{x}$',
                        r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
                    ]
                elif self.porosite:
                    lopi = [
                        r'Nappe Captive: $v=\frac{h.k}{x}$',
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

        elif self.mode == 'Etiage':
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
            # q = f"(((({h1}**2)-({h2}**2))*{Num(d)})/(2*{L}))-{W}(({L}/2)-{x})"
            q = f"((((h1**2)-(h2**2))*d)/(2*L))-W((L/2)-x)"
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

        bib = ['Nora NAJMI Master HIGH 2019/2020',
               'Écoulement Permanent Unidirectionnel:',
               r'Nappe Captive: $v=\frac{h.k}{x}$',

               r'Nappe Libre: $q=\frac{k}{2x}({h_0^2-h^2})$',
               r"Vitesse Darcy: $Q=-kA\frac{\Delta h}{L}$",
               r"Vitesse reelle",

               'Étiage:',
               "Localisation de la ligne de partage d'eau souterraine (d):",
               r"$d=\frac{L}{2}-\frac{K}{W}\frac{({h_0^2-h^2})}{2L}$",

               "Hauteur Piezometrique maximale au niveau de la ligne de partage d'eau $({h_{max}})$:",
               r"$h_{max} = \sqrt{{h_1^2}-\frac{({h_1^2-h_2^2})d}{L}+\frac{K}{W}(L-d)d}$",

               "Temps de deplacement a partir la ligne de partage d'eau souterraine vers les deux rivieres (t):",
               r"$t_a=\frac{L_a}{v_a}=\frac{L_a}{(\frac{k}{n})(\frac{\Delta h}{\Delta x})}$",

               'Debit quotidien par Kilometer de la nappe vers les deus rivieres (q):',
               r"$q=\frac{d({h_1^2-h_2^2})}{2L}-W(\frac{L}{2}-x)$"]

        self.FigureXY.Draw()
        self.Clear()

    def Clear(self):
        if self.mode == 'Ecoulement':
            for ko in range(5):
                self.entry[ko].delete(0, END)

        elif self.mode == 'Etiage':
            for cf in range(6):
                self.entry[cf].delete(0, END)


if __name__ == '__main__':
    Fluid()
