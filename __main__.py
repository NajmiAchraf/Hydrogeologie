from init import *
from tkinter import *
from tkinter import ttk, messagebox
from sympy import *
from sympy.solvers import solve
from sympy.solvers.solveset import solvify

r"""
1. ECOULEMENT UNIDIRECTIONNEL STABLE
    1.1. Aquifére confine:
        "$h = -\frac{vx}{K}$"

    1.2. Aquifére non confine:
        "$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$"

    1.3. Flux de base vers un flux:
        "$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"

        "$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"

        "$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$"

        "$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$"

2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS
    2.1. Aquifére confine:
        Débit de pompage:
            "$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"

            "$T = Kb = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$"
            
        Conductivité hydraulique:
            "$K = \frac{Q}{2\pi b\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$"
            
        Niveau d'eau dans le puit pompé:
            "$h_w =  h_2 - \frac{Q}{2 \pi K b} \ln{\frac{r_2}{r_1}}$"
            
        Rayon d'influence:
            "$R = r_0 = r_1 e^{\left(2\pi Kb\frac{h_0-h_1}{Q}\right)}$"

    2.2. Aquifére non confine:
        Débit de pompage:
            "$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"
    
            "$T \cong K\frac{h_1+h_2}{2}$"
        
        Conductivité hydraulique:
            "$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"
    
            "$T \cong K\frac{h_1+h_2}{2}$"
            
        Niveau d'eau dans le puit pompé:
            "$h_w =  \sqrt{h_2^2 - \frac{Q}{\pi K} \ln{\frac{r_2}{r_1}} }$"
            
        Rayon d'influence
            "$R = r_0 = r_1 e^{\left(\pi K\frac{h_0^2-h_1^2}{Q}\right)}$"
        
    2.3. Aquifére non confine avec recharge uniforme:
        Equation de la courbe de rabattement:
            "$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi K}ln\left(\frac{r_0}{r}\right)$"
            
        Débit de pompage:
            "$Q_w = \pi r_0^2 W$"
        
3. PUIT DANS UN ECOULEMENT UNIFORME
    Conductivité hydraulique (K):
        "$K = \frac{2Q}{\pi r\left(h_u+h_d\right)\left(i_u+i_d\right)}$"
        
    La pente de la surface piézométrique dans les conditions naturelles:
        $i = \frac{\Delta h}{\Delta x}$
        
    Les limites longitudinales et transversales des eaux souterraines entrant dans le puit:
        "$y_L =  \pm \frac{Q}{2Kbi}$"
        
        "$x_L = -\frac{Q}{2\pi Kbi}$"

4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.1. Equation de pompage de puits instable:
        La transmisivité:
            "$T = \frac{114.6Q}{s}W\left(u\right)$"
            
            "$T = \frac{Q}{4 \pi s}W(u)$"
            
        Le coefficient de stockage:
            "$S = \frac{Tt}{\frac{1}{u} 1.87r^2}$" (t in days)
        
            "$S = \frac{Tt}{\frac{1}{u} 2693r^2}$" (t in minutes)
        
    4.2. Methode de solution de Theis:
        La transmisivité:
            "$T = \frac{Q}{4 \pi s}W\left(u\right)$"
            
        Le coefficient de stockage:
            "$S = \frac{4Tu}{r^2/t}$"

    4.3. Methode de solution de Cooper-Jacob:
        La transmisivité:
            "$T = \frac{2.303Q}{4\pi \Delta s}$"
            
        Le coefficient de stockage:
            "$S = \frac{2.246Tt_0}{r^2}$"
    

    4.4. Methode de solution de Chow:
        "$F\left(u\right) = \frac{s}{\Delta s}$"

5. FLUX RADIAL INSTANTANE DANS UN AQUIFERE NON CONFINE
    "$s = \frac{Q}{4\pi T}W\left(u_a, u_y, \eta \right)$"

    "$u_a = \frac{r^2 S}{4Tt}$"

    "$u_y = \frac{r^2 S_y}{4Tt}$"

    "$\eta = \frac{r^2 K_z}{b^2 K_h}$"
    
6. ECOULEMENT RADIAL INSTABLE DANS UN AQUIFERE QUI FUIT
    "$s = \frac{Q}{4\pi T}W\left(u, \frac{r}{B} \right)$"

    "$u = \frac{r^2 S}{4Tt}$"

    "$\frac{r}{B} = \frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}}$"
    
7. UN PUITS S'ECOULE PRES DES LIMITES DE L'AQUIFERE 
    "$s_b = \frac{Q}{4\pi T}W\left(u_p\right) + \frac{Q}{4\pi T}W\left(u_i\right)$"

    "$u_p = \frac{r^2_p S}{4Tt_p}$"

    "$u_i = \frac{r^2_i S}{4Tt_i}$"


"""
'''
### version 3.1.0.4 FV
1. colorée les résultats et le texte généralement dans la feuille du calcul
'''
__author__ = 'NORA NAJMI'
__version__ = '3.1.0.4 FV'
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
ent_prm = {'fg': 'black',
           'bg': 'white',
           'width': '12',
           'font': ('DejaVu Sans', 14),
           'relief': 'flat'}
lbl_prm = {'fg': 'white',
           'bg': '#050505',  # purple
           'width': 27,
           'anchor': 'w',
           'font': ('DejaVu Sans', 14),
           'relief': 'flat'}
si_prm = {'fg': 'white',
          'width': 4,
          # 'bg': '#212121',
          # 'anchor': 'w',
          'font': ('DejaVu Sans', 14),
          'relief': 'flat'}

rgb_white = ((255. / 255.), (255. / 255.), (255. / 255.))
rgb_black = ((0. / 255.), (0. / 255.), (0. / 255.))

# hex_gray = '#F0F0F0'
hex_white = '#FFFFFF'
hex_dark = '#050505'

sn = SmallNumbers(10)
sns = SmallNumbers(10, "super")

n_identify = 30
n_title = 5
n_subtitle = 10
n_subsub = 15
n_intro = 5
n_calcl = 10


# Master Window ////////////////////////////////////////////////////////////////////////////////////////////////////////
class Hydrogeologie(Tk):
    def __init__(self):
        # Window Configuration _________________________________________________________________________________________
        super(Hydrogeologie, self).__init__()
        self.iconbitmap('ecology-globe-icon.ico')
        self.iconify()
        self.geometry("1360x715")
        self.minsize(width=1133, height=500)
        self.resizable(width=True, height=True)
        self.title(u"%s v%s" % (__title__, __version__))
        self.configure(background=lbl_prm['bg'])
        self.bind_all('<Key>', self.Keyboard)

        # NoteBook Configuration _______________________________________________________________________________________
        classes = [ECOULEMENT_UNIDIRECTIONNEL_STABLE,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS,
                   PUIT_DANS_UN_ECOULEMENT_UNIFORME,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE]
        cls_name = ['1. ECOULEMENT UNIDIRECTIONNEL STABLE',
                    '2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS',
                    '3. PUIT DANS UN ECOULEMENT UNIFORME',
                    '4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

        # Window Configuration _________________________________________________________________________________________
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.ExitApplication)

        self.deiconify()
        self.TopMost(True)
        self.update()
        self.TopMost(False)
        self.mainloop()

    def TopMost(self, top):
        self.attributes('-topmost', top)

    def ExitApplication(self):
        self.iconify()
        sys.exit()

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# Master GUI \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class GUI_MASTER(Frame):
    def __init__(self, master, Application, function_text, si_text, save_draw):
        super(GUI_MASTER, self).__init__(master=master)
        self.grid(row=0, column=0, sticky=NSEW)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.Application = Application

        self.automatic = True

        self.frame1 = Frame(self, background=lbl_prm['bg'], relief='flat')
        self.frame1.grid(row=0, column=0, sticky=NSEW)

        self.FigureXY = FigureXY(figsize=(1, 1), font_size=16, rgb_color=rgb_black,
                                 save_draw=save_draw + 2, facecolor=hex_white)
        self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self)
        self.TkAggXY.grid(row=0, column=1, rowspan=2, sticky=NSEW)

        self.DelState()

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

            label_si.append(Label(self.frame1, text=si_text[sd], bg=lbl_prm['bg'], **si_prm))
            label_si[sd].grid(row=sd, column=2, sticky=NSEW)

            self.frame1.rowconfigure(sd, weight=1)

        self.entry[0].focus_set()

        self.btn_auto = {
            "efface": "Description de la bouton Effacer ou Suppr:"
                      "\nEffacer permet d'effacer toutes les entrées et résultats de la feuille de calcul",

            "switch": "Cliquer pour switcher vers le Mode Manuel"
                      "\nDescription du Mode Automatique :"
                      "\nLorsque nous cliquons sur le bouton :"
                      "\nEffacer : Supprimer toutes les entrées et résultats de la feuille de calcul"
                      "\nCalculer : Supprimer les anciens calculs si ils existent dans la feuille de calcul"
                      "\net ajouter des nouveaux calculs",

            "calcul": "Description de la bouton Calculer ou Enter:"
                      "\nCalculer permet d'afficher les résultats des formules"
                      "\nde cette partie dans la feuille de calcul"

        }
        self.btn_manl = {
            "efface": "Description de la bouton Effacer:"
                      "\nEffacer permet d'effacer toutes les entrées",

            "switch": "Cliquer pour switcher vers le Mode Automatique"
                      "\nDescription du Mode Manuel :"
                      "\nLorsque nous cliquons sur le bouton :"
                      "\nEffacer : supprimer toutes les entrées"
                      "\nCorbeille 🗑 : supprimer les résultats de la feuille de calcul"
                      "\nCalculer : ajouter des calculs sur les anciens qui existent dans la feuille de calcul",

            "calcul": "Description de la bouton Calculer ou Enter:"
                      "\nCalculer permet d'ajouter des calculs sur les anciens qui existent dans la feuille de calcul"

        }
        self.button = []
        cbtn_text = ["Effacer", "Mode Automatique", "Calculer"]

        cbtn_ball = [self.btn_auto['efface'], self.btn_auto['switch'], self.btn_auto['calcul']]

        for er in range(len(cbtn_text)):
            self.button.append(HoverButton(self.frame2, **btn_prm, text=cbtn_text[er], balloon=cbtn_ball[er]))
            self.button[er].grid(row=0, column=er, sticky=NSEW)

        self.button[0].configure(command=lambda: self.Delete())

        self.button[1].configure(fg='#FF9950', activeforeground='orange', command=lambda: self.Switcher())
        self.button[1].change_color_bind(DefaultBG='#737373', HoverBG='#696969', ActiveBG='#5F5F5F')

        self.button[2].configure(bg='#20B645', activebackground='#00751E', command=lambda: self.Application())
        self.button[2].change_color_bind(DefaultBG='#20B645', HoverBG='#009C27', ActiveBG='#00751E')

        self.LaTexT(f'{__author__} Master HIGH 2020/2021', n_identify)

        self.LaTexT("Chapiter 4 : Hydraulique des puits, pompage d'essai et étude des rabattements")

    def LaTexT(self, LaTexT, axe_x=0):
        self.FigureXY.DrawLaTex(LaTexT=LaTexT, axe_x=axe_x)

    def Draw(self):
        self.FigureXY.Draw()

    def InputLaTexT(self, *args):
        text = f"{TX(args[0][0])} = {args[0][1]}{TX(args[0][2])}"
        for gr in range(1, len(args)):
            text += f" || {TX(args[gr][0])} = {args[gr][1]}{TX(args[gr][2])}"
        self.LaTexT(text)
        del text

    def EvalLaTexT(self, expression, variable, unite=r"\! "):
        result_str = App(variable)
        result_expr = Eva(variable)
        result_num = Num(variable)
        # checking by zero
        dot_zero = str(result_num).replace('.0', '')

        if (result_expr == result_str) and (result_expr == result_num or result_expr == dot_zero):
            self.LaTexT(f'{TX(expression)} = {result_str} {TX(unite)}', n_calcl)

        elif (result_expr == dot_zero) or (result_expr == result_num):
            self.LaTexT(f'{TX(expression)} = {result_str}', n_calcl)
            self.LaTexT(f'{TX(expression)} = {result_expr} {TX(unite)}', n_calcl)

        elif (result_expr != dot_zero) and (result_expr == result_str):
            self.LaTexT(f'{TX(expression)} = {result_expr}', n_calcl)
            self.LaTexT(f'{TX(expression)} = {result_num} {TX(unite)}', n_calcl)
        else:
            self.LaTexT(f'{TX(expression)} = {result_str}', n_calcl)
            self.LaTexT(f'{TX(expression)} = {result_expr}', n_calcl)
            self.LaTexT(f'{TX(expression)} = {result_num} {TX(unite)}', n_calcl)

        del result_str, result_expr, result_num, dot_zero

    def Keyboard(self, keyword):
        if keyword.keysym == "Return":
            self.Application()
        elif keyword.keysym == "Delete" and self.automatic:
            self.Delete()

    def DelState(self):
        self.TkAggXY.delete_state(self.automatic)

    def Switcher(self):
        if self.automatic:
            self.button[0].change_balloon_bind(self.btn_manl['efface'])

            self.button[1]['text'] = 'Mode Manuel'
            self.button[1].change_balloon_bind(self.btn_manl['switch'])

            self.button[2].change_balloon_bind(self.btn_manl['calcul'])

            self.automatic = False
        elif not self.automatic:
            self.button[0].change_balloon_bind(self.btn_auto['efface'])

            self.button[1]['text'] = 'Mode Automatique'
            self.button[1].change_balloon_bind(self.btn_auto['switch'])

            self.button[2].change_balloon_bind(self.btn_auto['calcul'])

            self.automatic = True

        self.DelState()

    def Delete(self):
        for cf in range(len(self.entry)):
            self.entry[cf].delete(0, END)
        if self.automatic:
            self.FigureXY.Clear()

    def Clear(self):
        if self.automatic:
            self.Delete()


# 1. ECOULEMENT UNIDIRECTIONNEL STABLE #################################################################################
class ECOULEMENT_UNIDIRECTIONNEL_STABLE(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_UNIDIRECTIONNEL_STABLE, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [ECOULEMENT_UNIDIRECTIONNEL_STABLE_1,
                   ECOULEMENT_UNIDIRECTIONNEL_STABLE_2,
                   ECOULEMENT_UNIDIRECTIONNEL_STABLE_3]
        cls_name = ['1.1. Aquifére confine',
                    '1.2. Aquifére non confine',
                    '1.3. Flux de base vers un flux']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# 1.1. Aquifére confine ================================================================================================
class ECOULEMENT_UNIDIRECTIONNEL_STABLE_1(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_UNIDIRECTIONNEL_STABLE_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["vitesse (v)",
                         "Distance (x)",
                         "Conductivité (K)"]
        si_text = ["m/j", "m", "m/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("1. ECOULEMENT UNIDIRECTIONNEL STABLE:", n_title)

        self.LaTexT("1.1. Aquifére confiné:", n_subtitle)

        self.LaTexT(f"Nappe Captive ({TX('h')}):", n_subsub)

        self.LaTexT(r"Relation : $h = -\frac{vx}{K}$")

        self.Draw()

    def Application(self):
        v = eval(str(self.entry[0].get()))
        x = eval(str(self.entry[1].get()))
        K = eval(str(self.entry[2].get()))

        # h = "- (v * x) / K"
        h = f"- ({v} * {x}) / {K}"

        self.Clear()

        self.InputLaTexT(('v', v, 'm/j'), ('x', x, 'm'), ('K', K, 'm/j'))
        self.LaTexT(f"Calcul de Nappe Captive ({TX('h')}):", n_intro)
        self.LaTexT(r"$h = -\frac{vx}{K}$", n_calcl)
        self.EvalLaTexT("h", h, "m")

        r"""
1. ECOULEMENT UNIDIRECTIONNEL STABLE:
    1.1. Aquifére confine:
        "$h = -\frac{vx}{K}$"
"""
        self.Draw()


# 1.2. Aquifére non confine ============================================================================================
class ECOULEMENT_UNIDIRECTIONNEL_STABLE_2(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_UNIDIRECTIONNEL_STABLE_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Hauteur Piézométrique (h)",
                         f"Hauteur Piézométrique (h{sn(0)})",
                         "Distance (x)",
                         "Conductivité (K)"]
        si_text = ["m", "m", "m", "m/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("1. DEBIT UNIDIRECTIONNEL STABLE:", n_title)

        self.LaTexT("1.2. Aquifére non confiné:", n_subtitle)

        self.LaTexT(f"Equation du puit ({TX('q')}):", n_subsub)

        self.LaTexT(r"Relation : $q = \frac{K}{2x}\left({h_0^2-h^2}\right)$")

        self.Draw()

    def Application(self):
        h = eval(str(self.entry[0].get()))
        h0 = eval(str(self.entry[1].get()))
        x = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))

        # q = f"( K / ( 2 * x )) * ( h0 ** 2 - h ** 2 )"
        q = f"( {K} / ( 2 * {x} )) * ( {h0} ** 2 - {h} ** 2 )"

        self.Clear()

        self.InputLaTexT(('h', h, 'm'), ('h_0', h0, 'm'), ('x', x, 'm'), ('K', K, 'm/j'))
        self.LaTexT(f"Calcul d'Equation du puit ({TX('q')}):", n_intro)
        self.LaTexT(r"$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$", n_calcl)
        self.EvalLaTexT("q", q, 'm^2/j')

        r"""
    1.2. Aquifére non confine:
        "$q = \frac{K}{2x}\left({h_0^2-h^2}\right)$"
"""
        self.Draw()


# 1.3. Flux de base vers un flux =======================================================================================
class ECOULEMENT_UNIDIRECTIONNEL_STABLE_3(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_UNIDIRECTIONNEL_STABLE_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau de la rivière 1 (h₁)",
                         "Niveau d'eau de la rivière 2 (h₂)",
                         "Distance (L)",
                         "Distance (x)",
                         "Conductivité (K)",
                         "Recharge (W)"]
        si_text = ["m", "m", "m", "m", "m/j", "m/an"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("1. DEBIT UNIDIRECTIONNEL STABLE:", n_title)

        self.LaTexT("1.3. Débit de base vers un cours d'eau:", n_subtitle)

        self.LaTexT(r"Relations : $q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"
                    r" || $d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"
                    r" || $h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        L = eval(str(self.entry[2].get()))
        x = eval(str(self.entry[3].get()))
        K = eval(str(self.entry[4].get()))
        Wa = eval(str(self.entry[5].get()))

        # W = Wa / 365
        W = f"{Wa} / 365"

        # qx = f"((((h1**2)-(h2**2))*K)/(2*L))-W*((L/2)-x)"
        qx = f"( ( ( ({h1} ** 2) - ({h2} ** 2) ) * {K}) / (2 * {L}) ) - ({Num(W, 3)} * (( {L} / 2 ) - {x}))"

        # d = "(L / 2) - ((K / W) * (((h1 ** 2) - (h2 ** 2)) / (2 * L)))"
        d = f"({L} / 2) - (({K} / {Num(W, 3)}) * ((({h1} ** 2) - ({h2} ** 2)) / (2 * {L})))"

        '''
    # hmax = "sqrt((h1 ** 2) - ((((h1 ** 2) - (h2 ** 2)) * d) / L) + ((W / K) * (L - d) * d))"
    hmax = f"sqrt(({h1}**2)-(((({h1}**2)-({h2}**2))*{Num(d, 3)})/{L})+(({Num(W, 3)}/{K})*({L}-{Num(d, 3)}) \
    *{Num(d, 3)}))"
        '''
        hp = f"({h1}**2)-(((({h1}**2)-({h2}**2))*{Num(d, 3)})/{L})+(({Num(W, 3)}/{K})*({L}-{Num(d, 3)})*{Num(d, 3)})"
        hms = r"\sqrt{%s}" % Num(hp, 16)
        hr = f"sqrt({Num(hp, 16)})"

        self.Clear()

        self.InputLaTexT(("h_1", h1, "m"), ("h_2", h2, "m"), ("L", L, "m"), ("x", x, "m"), ("K", K, "m/j"),
                         ("W", Wa, "m/an"))
        self.LaTexT(f'Convertir la recharge ({TX("W")}) de {TX("m/an")} vers {TX("m/j")} :', n_intro)
        self.LaTexT(TX(f"W = {Wa} / 365 = {Num(W)} m/j"), n_calcl)

        self.LaTexT(f'Calcul de debit quotidien par Kilomètre de la nappe vers les deux rivières ({TX("q_x")}):',
                    n_intro)
        self.LaTexT(r"$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$", n_calcl)
        self.EvalLaTexT("q_x", qx, "m^2/j")

        self.LaTexT(f"Calcul de localisation de la ligne de partage d'eau souterraine ({TX('d')}):", n_intro)
        self.LaTexT(r"$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$", n_calcl)
        self.EvalLaTexT("d", d, "m")

        self.LaTexT(f"Calcul de Hauteur Piézométrique maximale au niveau de la ligne de partage d'eau "
                    f"({TX('h_{max}')}):", n_intro)
        self.LaTexT(r"$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$",
                    n_calcl)
        self.EvalLaTexT("h_{max}^2", hp)
        self.LaTexT(TX(r"h_{max} = "f"{hms}"), n_calcl)
        #  self.LaTexT(r"$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$",
        #              n_calcl)
        self.EvalLaTexT("h_{max}", hr, "m")

        r"""
    1.3. Flux de base vers un flux:
        "$q_x = \frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"

        "$d = \frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"

        "$h^2_{max} = {h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$"

        "$h_{max} = \sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$"
"""
        self.Draw()


# 2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS ##########################################################################
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3]
        cls_name = ['2.1. Aquifére confine',
                    '2.2. Aquifére non confine',
                    '2.3. Aquifére non confine avec recharge uniforme']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# 2.1. Aquifére confine ================================================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_1,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_2,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_3,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_4]
        cls_name = ['Débit de pompage',
                    'Conductivité hydraulique',
                    "Niveau d'eau dans le puit pompé",
                    "Rayon d'influence"]

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# Débit de pompage -----------------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_1(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau observé 1 (h₁|h𝓌)",
                         "Niveau d'eau observé 2 (h₂|h)",
                         "Distance (r₁|r𝓌)",
                         "Distance (r₂|r)",
                         "Conductivité (K)",
                         "Épaisseur (b)"]
        si_text = ["m", "m", "m", "m", "m/j", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.1. Aquifére confiné:", n_subtitle)

        self.LaTexT(r"Relations : $Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"
                    r" || $T = Kb = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$")

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

        self.InputLaTexT(("h_1", h1, "m"), ("h_w", h1, "m"), ("h_2", h2, "m"), ("h", h2, "m"), ("r_1", r1, "m"),
                         ("r_w", r1, "m"), ("r_2", r2, "m"), ("r", r2, "m"), ("K", K, "m/j"), ("b", b, "m"))
        self.LaTexT(f'Débit de pompage ({TX("Q")}):', n_intro)
        self.LaTexT(r"$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$", n_calcl)
        self.EvalLaTexT("Q", Q, "m^3/j")

        self.LaTexT(f'Transmisivité ({TX("T")}):', n_intro)
        self.LaTexT(r"$T = Kb$", n_calcl)
        self.EvalLaTexT("T", T1, "m^2/j")

        self.LaTexT(f'Transmisivité ({TX("T")}):', n_intro)
        self.LaTexT(r"$T = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$", n_calcl)
        self.EvalLaTexT("T", T2, "m^2/j")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.1. Aquifére confine:
        Débit de pompage:
            "$Q = 2\pi Kb\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"

            "$T = Kb = \frac{Q}{2\pi \left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$"
"""
        self.Draw()


# Conductivité hydraulique ---------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_2(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau observé 1 (h𝓌)",
                         "Niveau d'eau observé 2 (h)",
                         "Distance (r𝓌)",
                         "Distance (r)",
                         "Débit de pompage (Q)",
                         "Épaisseur (b)"]
        si_text = ["m", "m", "m", "m", f"m{sns(3)}/j", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.1. Aquifére confiné:", n_subtitle)

        self.LaTexT(r"Relation : $K = \frac{Q}{2\pi b\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$")

        self.Draw()

    def Application(self):
        hw = eval(str(self.entry[0].get()))
        h = eval(str(self.entry[1].get()))
        rw = eval(str(self.entry[2].get()))
        r = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))
        b = eval(str(self.entry[5].get()))

        # K = (Q / (2 * pi * b * (h - hw))) * log(r / rw)
        K = f"({Q} / (2 * pi * {b} * ({h} - {hw}))) * log({r} / {rw})"

        self.Clear()

        self.InputLaTexT(("h_w", hw, "m"), ("h", h, "m"), ("r_w", r, "m"), ("r", r, "m"), ("Q", Q, "m^3/j"),
                         ("b", b, "m"))
        self.LaTexT(f'Conductivité hydraulique ({TX("K")}):', n_intro)
        self.LaTexT(r"$K = \frac{Q}{2\pi b\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$", n_calcl)
        self.EvalLaTexT("K", K, "m/j")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.1. Aquifére confine:
        Conductivité hydraulique:
            "$K = \frac{Q}{2\pi b\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$"
"""
        self.Draw()


# Niveau d'eau dans le puit pompé --------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_3(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = [f"Niveau d'eau observé 2 (h{sn(2)})",
                         f"Distance (r{sn(1)})",
                         f"Distance (r{sn(2)})",
                         "Conductivité (K)",
                         "Débit de pompage (Q)",
                         "Épaisseur (b)"]
        si_text = ["m", "m", "m", "m/j", f"m{sns(3)}/j", 'm']

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.1. Aquifére confiné:", n_subtitle)

        self.LaTexT(r"Relation : $h_w =  h_2 - \frac{Q}{2 \pi K b} \ln{\frac{r_2}{r_1}}$")

        self.Draw()

    def Application(self):
        h2 = eval(str(self.entry[0].get()))
        r1 = eval(str(self.entry[1].get()))
        r2 = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))
        b = eval(str(self.entry[5].get()))

        # hw = h2 - (Q / (2 * pi * K * b)) * log(r2 / r1)
        hw = f"{h2}- ({Q} / (2 * pi * {K} * {b})) * log({r2} / {r1})"

        self.Clear()

        self.InputLaTexT(("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"),
                         ("b", b, "m"))
        self.LaTexT(f"Niveau d'eau dans le puit pompé ({TX('h_w')}):", n_intro)
        self.LaTexT(r"$h_w =  h_2 - \frac{Q}{2 \pi K b} \ln{\frac{r_2}{r_1}}$", n_calcl)
        self.EvalLaTexT("h_w", hw, "m")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.1. Aquifére confine:
        Niveau d'eau dans le puit pompé:
            "$h_w =  h_2 - \frac{Q}{2 \pi K b} \ln{\frac{r_2}{r_1}}$"
"""
        self.Draw()


# Rayon d'influence ----------------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_4(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_4, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = [f"Niveau d'eau observé 1 (h{sn(0)})",
                         f"Niveau d'eau observé 2 (h{sn(1)})",
                         f"Distance (r{sn(1)})",
                         "Conductivité (K)",
                         "Débit de pompage (Q)",
                         "Épaisseur (b)"]
        si_text = ["m", "m", "m", "m", f"m{sns(3)}/j", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.1. Aquifére confiné:", n_subtitle)

        self.LaTexT(r"Relation : $R = r_0 = r_1 e^{\left(2\pi Kb\frac{h_0-h_1}{Q}\right)}$")

        self.Draw()

    def Application(self):
        h0 = eval(str(self.entry[0].get()))
        h1 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))
        b = eval(str(self.entry[5].get()))

        # R = r1 * exp(2 * pi * K * b * ((h0 - h1) / Q))
        R = f"{r1} * exp(2 * pi * {K} * {b} * (({h0} - {h1}) / {Q}))"

        self.Clear()

        self.InputLaTexT(("h_0", h0, "m"), ("h_1", h1, "m"), ("r_1", r1, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"),
                         ("b", b, "m"))
        self.LaTexT(f"Rayon d'influence ({TX('R')}):", n_intro)
        self.LaTexT(r"$R = r_0 = r_1 e^{\left(2\pi Kb\frac{h_0-h_1}{Q}\right)}$", n_calcl)
        self.EvalLaTexT("R = r_0", R, "m")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.1. Aquifére confine:
        Rayon d'influence
            "$R = r_0 = r_1 e^{\left(2\pi Kb\frac{h_0-h_1}{Q}\right)}$"
"""
        self.Draw()


# 2.2. Aquifére non confine ============================================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_1,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_2,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_3,
                   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_4]
        cls_name = ['Débit de pompage',
                    'Conductivité hydraulique',
                    "Niveau d'eau dans le puit pompé",
                    "Rayon d'influence"]

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# Débit de pompage -----------------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_1(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau observé 1 (h₁)",
                         "Niveau d'eau observé 2 (h₂)",
                         "Distance (r₁)",
                         "Distance (r₂)",
                         "Conductivité (K)"]
        si_text = ["m", "m", "m", "m", "m/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.2. Aquifére non confiné:", n_subtitle)

        self.LaTexT(r"Relations : $Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"
                    r" || $T \cong K\frac{h_1+h_2}{2}$")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        r2 = eval(str(self.entry[3].get()))
        K = eval(str(self.entry[4].get()))

        # Q = "pi * K * ((h2 ** 2 - h1 ** 2) / (log(r2 / r1)))"
        Q = f"pi * {K} * (({h2 ** 2} - {h1 ** 2}) / (log({r2} / {r1})))"

        # T = K * ((h1 + h2) / 2)
        T = f"{K} * (({h1} + {h2}) / 2)"

        self.Clear()

        self.InputLaTexT(("h_1", h1, "m"), ("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"))
        self.LaTexT(f'Débit de pompage ({TX("Q")}):', n_intro)
        self.LaTexT(r"$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$", n_calcl)
        self.EvalLaTexT("Q", Q, 'm^3/j')

        self.LaTexT(f'Transmisivité ({TX("T")}):', n_intro)
        self.LaTexT(r"$T \cong K\frac{h_1+h_2}{2}$", n_calcl)
        self.EvalLaTexT("T", T, 'm^2/j')

        r"""
    2.2. Aquifére non confine:
        Débit de pompage:
            "$Q = \pi K\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"

            "$T \cong K\frac{h_1+h_2}{2}$"
"""
        self.Draw()


# Conductivité hydraulique ---------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_2(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau observé 1 (h₁)",
                         "Niveau d'eau observé 2 (h₂)",
                         "Distance (r₁)",
                         "Distance (r₂)",
                         "Débit de pompage (Q)"]
        si_text = ["m", "m", "m", "m", f"m{sns(3)}/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.2. Aquifére non confiné:", n_subtitle)

        self.LaTexT(r"Relations : $K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"
                    r" || $T \cong K\frac{h_1+h_2}{2}$")

        self.Draw()

    def Application(self):
        h1 = eval(str(self.entry[0].get()))
        h2 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        r2 = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))

        # K = "(Q /(pi * (h2 ** 2 - h1 ** 2))) * (log(r2 / r1))"
        K = f"({Q} /(pi * ({h2} ** 2 - {h1} ** 2))) * (log({r2} / {r1}))"

        # T = K * ((h1 + h2) / 2)
        T = f"{K} * (({h1} + {h2}) / 2)"

        self.Clear()

        self.InputLaTexT(("h_1", h1, "m"), ("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("Q", Q, "m^3/j"))
        self.LaTexT(f'Conductivité hydraulique ({TX("K")}):', n_intro)
        self.LaTexT(r"$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$", n_calcl)
        self.EvalLaTexT("K", K, "m/j")

        self.LaTexT(f'Transmisivité ({TX("T")}):', n_intro)
        self.LaTexT(r"$T \cong K\frac{h_1+h_2}{2}$", n_calcl)
        self.EvalLaTexT("T", T, "m^2/j")

        r"""
    2.2. Aquifére non confine:
        Conductivité hydraulique:
            "$K = \frac{Q}{\pi \left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"

            "$T \cong K\frac{h_1+h_2}{2}$"
"""
        self.Draw()


# Niveau d'eau dans le puit pompé --------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_3(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = [f"Niveau d'eau observé 2 (h{sn(2)})",
                         f"Distance (r{sn(1)})",
                         f"Distance (r{sn(2)})",
                         "Conductivité (K)",
                         "Débit de pompage (Q)"]
        si_text = ["m", "m", "m", "m/j", f"m{sns(3)}/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.2. Aquifére non confiné:", n_subtitle)

        self.LaTexT(r"Relation : $h_w =  \sqrt{h_2^2 - \frac{Q}{\pi K} \ln{\frac{r_2}{r_1}}} $")

        self.Draw()

    def Application(self):
        h2 = eval(str(self.entry[0].get()))
        r1 = eval(str(self.entry[1].get()))
        r2 = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))

        # hw = sqrt(h2 ** 2 - (Q / (pi * K)) * log(r2 / r1))
        hw = f"sqrt({h2} ** 2 - ({Q} / (pi * {K})) * log({r2} / {r1}))"

        self.Clear()

        self.InputLaTexT(("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"))
        self.LaTexT(f"Niveau d'eau dans le puit pompé ({TX('h_w')}):", n_intro)
        self.LaTexT(r"$h_w =  \sqrt{h_2^2 - \frac{Q}{\pi K} \ln{\frac{r_2}{r_1}} }$", n_calcl)
        self.EvalLaTexT("h_w", hw, "m")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.2. Aquifére non confine:
        Niveau d'eau dans le puit pompé:
            "$h_w =  \sqrt{h_2^2 - \frac{Q}{\pi K} \ln{\frac{r_2}{r_1}} }$"
"""
        self.Draw()


# Rayon d'influence ----------------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_4(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_4, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = [f"Niveau d'eau observé 1 (h{sn(0)})",
                         f"Niveau d'eau observé 2 (h{sn(1)})",
                         f"Distance (r{sn(1)})",
                         "Conductivité (K)",
                         "Débit de pompage (Q)"]
        si_text = ["m", "m", "m", "m", f"m{sns(3)}/j"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.2. Aquifére non confiné:", n_subtitle)

        self.LaTexT(r"Relation : $R = r_0 = r_1 e^{\left(\pi K\frac{h_0^2-h_1^2}{Q}\right)}$")

        self.Draw()

    def Application(self):
        h0 = eval(str(self.entry[0].get()))
        h1 = eval(str(self.entry[1].get()))
        r1 = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        Q = eval(str(self.entry[4].get()))

        # R = r1 * exp(pi * K * ((h0 ** 2 - h1 ** 2) / Q))
        R = f"{r1} * exp(pi * {K} * (({h0} ** 2 - {h1} ** 2) / {Q}))"

        self.Clear()

        self.InputLaTexT(("h_0", h0, "m"), ("h_1", h1, "m"), ("r_1", r1, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"))
        self.LaTexT(f"Rayon d'influence ({TX('R')}):", n_intro)
        self.LaTexT(r"$R = r_0 = r_1 e^{\left(\pi K\frac{h_0^2-h_1^2}{Q}\right)}$", n_calcl)
        self.EvalLaTexT("R = r_0", R, "m")

        r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
    2.2. Aquifére non confine:
        Rayon d'influence
            "$R = r_0 = r_1 e^{\left(\pi K\frac{h_0^2-h_1^2}{Q}\right)}$"
"""
        self.Draw()


# 2.3. Aquifére non confine avec recharge uniforme =====================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3(ttk.Frame):
    def __init__(self, master):
        super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Niveau d'eau observé 1 (h)",
                         f"Niveau d'eau observé 2 (h{sn(0)})",
                         "Distance (r)",
                         "Conductivité (K)",
                         "Recharge (W)"]
        si_text = ["m", "m", "m", "m/j", "m/an"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.r_0 = symbols('r_0')
        self.R = S.Reals
        self.C = S.Complexes

        self.RUN()

    def RUN(self):
        self.LaTexT("2. FLUX RADIAL CONSTANT VERS UN PUITS:", n_title)

        self.LaTexT("2.3. Aquifére non confiné avec recharge uniforme:", n_subtitle)

        self.LaTexT(
            r"Relations : "
            r"$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{\pi r_0^2 W}{\pi K}ln\left(\frac{r_0}{r}\right)$"
            r" || $Q_w = \pi r_0^2 W$")

        self.Draw()

    def Application(self):
        h = eval(str(self.entry[0].get()))
        h0 = eval(str(self.entry[1].get()))
        r = eval(str(self.entry[2].get()))
        K = eval(str(self.entry[3].get()))
        W = eval(str(self.entry[4].get()))

        # qs = h0 ** 2 - h ** 2
        q = f"{h0} ** 2 - {h} ** 2"

        # ps = (W / (2 * K)) * (r ** 2 - x ** 2) + ((pi * x ** 2 * W) / (pi * K)) * log(r0 / r)
        p = f"({W} / (2*{K})) * ({r}**2 - {self.r_0}**2) + ((pi*{self.r_0}**2 * {W}) / (pi*{K}))*log({self.r_0} / {r})"

        try:
            sol = solve(Eq(sympify(q), sympify(p)), self.r_0)
        except Exception:
            sol = solvify(Eq(sympify(q), sympify(p)), self.r_0, self.C)
            if sol is None:
                sol = solvify(Eq(sympify(q), sympify(p)), self.r_0, self.R)
        try:
            r0 = str(sol[0])
        except IndexError:
            messagebox.showerror(title="Erreur !!", message=f"L'équation de la courbe de rabattement n'a pas de "
                                                            f"solution pour le Rayon d'influence r{sn(0)}")
        # Q = pi * r0 ** 2 * W
        Q = f"{pi} * {r0} ** 2 * {W}"

        self.Clear()

        self.InputLaTexT(("h", h, "m"), ("h_0", h0, "m"), ("r", r, "m"), ("K", K, "m/j"), ("W", W, "m/an"))
        self.LaTexT(f"Equation de la courbe de rabattement:", n_intro)
        self.LaTexT(
            r"$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{\pi r_0^2 W}{\pi K}ln\left(\frac{r_0}{r}\right)$",
            n_calcl)
        self.LaTexT(f"{App(q)} = {App(p)}", n_calcl)
        self.LaTexT(App(Eq(sympify(q), sympify(p))), n_calcl)
        self.LaTexT(f"Rayon d'influence ({TX('r_0')}) donné par la résolution d'équation de la courbe de rabattement:",
                    n_intro)
        self.EvalLaTexT("r_0", r0, "m")

        self.LaTexT(f'Débit de pompage ({TX("Q_w")}):', n_intro)
        self.LaTexT(r"$Q_w = \pi r_0^2 W$", n_calcl)
        self.EvalLaTexT("Q_w", Q, "m^3/j")

        r"""
    2.3. Aquifére non confine avec recharge uniforme:
        Equation de la courbe de rabattement:
            "$h^2_0-h^2 = \frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi K}ln\left(\frac{r_0}{r}\right)$"
            
        Débit de pompage:
            "$Q_w = \pi r_0^2 W$"
"""
        self.Draw()


# 3. PUIT DANS UN ECOULEMENT UNIFORME ##################################################################################
class PUIT_DANS_UN_ECOULEMENT_UNIFORME(ttk.Frame):
    def __init__(self, master):
        super(PUIT_DANS_UN_ECOULEMENT_UNIFORME, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [PUIT_DANS_UN_ECOULEMENT_UNIFORME_1,
                   PUIT_DANS_UN_ECOULEMENT_UNIFORME_2,
                   PUIT_DANS_UN_ECOULEMENT_UNIFORME_3]
        cls_name = ['Conductivité hydraulique',
                    "La pente de la surface piézométrique dans les conditions naturelles",
                    "Les limites longitudinales et transversales des eaux souterraines entrant dans le puit"]

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# Conductivité hydraulique ---------------------------------------------------------------------------------------------
class PUIT_DANS_UN_ECOULEMENT_UNIFORME_1(ttk.Frame):
    def __init__(self, master):
        super(PUIT_DANS_UN_ECOULEMENT_UNIFORME_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Épaisseur saturé 1 (hᵤ)",
                         "Épaisseur saturé 2 (h𝒹)",
                         "Distance (r)",
                         "Débit de pompage (Q)",
                         "Pente de la nappe phréatique (iᵤ)",
                         "Pente de la nappe phréatique (i𝒹)"]
        si_text = ["m", "m", "m", f"m{sns(3)}/j", "", ""]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("3.PUIT DANS UN ECOULEMENT UNIFORME:", n_title)

        self.LaTexT('Conductivité hydraulique (K):', n_subtitle)

        self.LaTexT(r"Relation : $K = \frac{2Q}{\pi r(h_u+h_d)(i_u+i_d)}$")

        self.Draw()

    def Application(self):
        hu = eval(str(self.entry[0].get()))
        hd = eval(str(self.entry[1].get()))
        r = eval(str(self.entry[2].get()))
        Q = eval(str(self.entry[3].get()))
        iu = eval(str(self.entry[4].get()))
        id = eval(str(self.entry[5].get()))

        # K = (2 * Q) / (pi * r * (hu + hd) * (iu + id))
        K = f"(2 * {Q}) / (pi * {r} * ({hu} + {hd}) * ({iu} + {id}))"

        self.Clear()

        self.InputLaTexT(("h_u", hu, "m"), ("h_d", hd, "m"), ("r", r, "m"), ("Q", Q, "m^3/j"), ("i_u", iu, r"\, "),
                         ("i_d", id, r"\, "))
        self.LaTexT("Calcul de la Conductivité hydraulique $(K)$:", n_intro)
        self.LaTexT(r"$K = \frac{2Q}{\pi r\left(h_u+h_d\right)\left(i_u+i_d\right)}$", n_calcl)
        self.EvalLaTexT("K", K, "m/j")

        r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
    Conductivité hydraulique (K):
        "$K = \frac{2Q}{\pi r\left(h_u+h_d\right)\left(i_u+i_d\right)}$"
"""
        self.Draw()


# La pente de la surface piézométrique dans les conditions naturelles --------------------------------------------------
class PUIT_DANS_UN_ECOULEMENT_UNIFORME_2(ttk.Frame):
    def __init__(self, master):
        super(PUIT_DANS_UN_ECOULEMENT_UNIFORME_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Le niveau piézométrique observé\nentre les deux puits (∆h)",
                         "La distance entre les deux puits\n(∆x)"]
        si_text = ["m", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("3.PUIT DANS UN ECOULEMENT UNIFORME:", n_title)

        self.LaTexT("La pente de la surface piézométrique dans les conditions naturelles:", n_subtitle)

        self.LaTexT(r"Relation : $i = \frac{\Delta h}{\Delta x}$")

        self.Draw()

    def Application(self):
        dh = eval(str(self.entry[0].get()))
        dx = eval(str(self.entry[1].get()))

        # i = dh / dx
        i = f"{dh} / {dx}"

        self.Clear()

        self.InputLaTexT((r"\Delta h", dh, "m"), (r"\Delta x", dx, "m"))
        self.LaTexT("Calcul de la pente de la surface piézométrique dans les conditions naturelles $(i)$:", n_intro)
        self.LaTexT(r"$i = \frac{\Delta h}{\Delta x}$", n_calcl)
        self.EvalLaTexT("i", i)

        r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
    La pente de la surface piézométrique dans les conditions naturelles:
        $i = \frac{\Delta h}{\Delta x}$
"""
        self.Draw()


# Les limites longitudinales et transversales des eaux souterraines entrant dans le puit -------------------------------
class PUIT_DANS_UN_ECOULEMENT_UNIFORME_3(ttk.Frame):
    def __init__(self, master):
        super(PUIT_DANS_UN_ECOULEMENT_UNIFORME_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Conductivité hydraulique (K)",
                         "Débit de décharge (Q)",
                         "Pente piézométrique naturelle (i)",
                         "Épaisseur (b)"]
        si_text = ["m/j", f"m{sns(3)}/j", "", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("3.PUIT DANS UN ECOULEMENT UNIFORME:", n_title)

        self.LaTexT("Les limites longitudinales et transversales des eaux souterraines entrant dans le puit:",
                    n_subtitle)

        self.LaTexT(r"Relations : $y_L =  \pm \frac{Q}{2Kbi}$  || $x_L = -\frac{Q}{2\pi Kbi}$")

        self.Draw()

    def Application(self):
        K = eval(str(self.entry[0].get()))
        Q = eval(str(self.entry[1].get()))
        i = eval(str(self.entry[2].get()))
        b = eval(str(self.entry[3].get()))

        # yl = Q / (2 * K * b * iu)
        yl = f"{Q} / (2 * {K} * {b} * {i})"

        # xl = - Q / (2 * pi * K * b * iu)
        xl = f"- {Q} / (2 * pi * {K} * {b} * {i})"

        self.Clear()

        self.InputLaTexT(("K", K, "m/j"), ("Q", Q, "m^3/j"), ("i", i, r"\, "), ("b", b, "m"))
        self.LaTexT("Calcul des limites longitudinales des eaux souterraines entrant dans le puit $y_L$:", n_intro)
        self.LaTexT(r"$y_L =  \pm \frac{Q}{2Kbi}$", n_calcl)
        self.EvalLaTexT("y_L", yl, "m")

        self.LaTexT(f"Calcul des limites transversales des eaux souterraines entrant dans le puit $x_L$:", n_intro)
        self.LaTexT(r"$x_L = -\frac{Q}{2\pi Kbi}$", n_calcl)
        self.EvalLaTexT("x_L", xl, "m")

        r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
    Les limites longitudinales et transversales des eaux souterraines entrant dans le puit:
        "$y_L =  \pm \frac{Q}{2Kbi}$"
        
        "$x_L = -\frac{Q}{2\pi Kbi}$"
"""
        self.Draw()


# 4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE ###################################################################
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3, ]
        # FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_4]
        cls_name = ['4.1. Equation de pompage de puits hors équilibre',
                    '4.2. Methode de solution de Theis',
                    '4.3. Methode de solution de Cooper-Jacob',
                    '4.4. Methode de solution de Chow']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# 4.1. Equation de pompage de puits hors équilibre =====================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_1,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2, ]
        cls_name = ['La transmisivité',
                    'Le coefficient de stockage']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# La transmisivité -----------------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_1(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Le débit constant du puit (Q)",
                         "Le rabattement (s)",
                         "Fonction du puit (W(u))"]
        si_text = ["gpm", "ft", ""]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.1. Equation de pompage de puits instable:", n_subtitle)

        self.LaTexT("La transmisivité (T):", n_subsub)

        self.LaTexT(r"Relations : $T = \frac{114.6Q}{s}W\left(u\right)$ || $T = \frac{Q}{4 \pi s}W\left(u\right)$")

        self.Draw()

    def Application(self):
        Q = eval(str(self.entry[0].get()))
        s = eval(str(self.entry[1].get()))
        Wu = eval(str(self.entry[2].get()))

        # T1 = ((114.6 * Q) / s) * Wu
        T1 = f"((114.6 * {Q}) / {s}) * {Wu}"

        # Qt = Q * 0.06309 * 86.4
        Qt = f"{Q} * 0.06309 * 86.4"  # gpm to L/s to m^3/j

        # st = s * 0.3048
        st = f"{s} * 0.3048"  # ft to m

        # T2 = (Q / (4 * pi * s)) * Wu
        T2 = f"({Qt} / (4 * pi * {st})) * {Wu}"

        self.Clear()

        self.InputLaTexT(("Q", Q, "gpm"), ("s", s, "ft"), (r"W\left( u \right)", Wu, r"\, "))
        self.LaTexT("La transmisivité en gpd/ft:", n_intro)
        self.LaTexT(r"$T = \frac{114.6Q}{s}W\left(u\right)$", n_calcl)
        self.EvalLaTexT("T", T1, "gpd/ft")

        self.LaTexT(f"Conversion depuis les unités usuelles de U.S. vers S.I:", n_intro)
        self.LaTexT(f"Q = {Q} {TX('gpm')} = {Num(Qt)} {TX('m^3/j')}", n_calcl)
        self.LaTexT(f"s = {s} {TX('ft')} = {Num(st)} {TX('m')}", n_calcl)

        self.LaTexT(f"La transmisivité en {TX('m^2/j')}:", n_intro)
        self.LaTexT(r"$T = \frac{Q}{4 \pi s}W\left(u\right)$", n_calcl)
        self.EvalLaTexT("T", T2, "m^2/j")

        # T = T1 * 0.01242
        T = f"{T1} * 0.01242"

        self.LaTexT(f"Vérifier que la transmisivité en {TX('gpd/ft')} égale {TX('m^2/j')}:", n_intro)

        self.LaTexT(f"T = {App(T)}", n_calcl)

        self.LaTexT(f"T = {Num(T)} {TX('m^2/j')}", n_calcl)

        r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.1. Equation de pompage de puits instable:
        La transmisivité:
            "$T = \frac{114.6Q}{s}W\left(u\right)$"
            
            "$T = \frac{Q}{4 \pi s}W(u)$"
"""
        self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["La transmisivité (T)",
                         "Distance (r)",
                         "Temps (t)",
                         "(1/u)"]
        si_text = [f"m{sns(2)}/j\ngpd/ft", "m", "j", ""]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.1. Equation de pompage de puits instable:", n_subtitle)

        self.LaTexT("Le coefficient de stockage (S):", n_subsub)

        self.LaTexT(r"Relations : $S = \frac{Tt}{\frac{1}{u} 1.87r^2}$ (t en jours)"
                    r" || $S = \frac{Tt}{\frac{1}{u} 2693r^2}$ (t en minutes)")

        self.Draw()

    def Application(self):
        T = eval(str(self.entry[0].get()))
        r = eval(str(self.entry[1].get()))
        t = eval(str(self.entry[2].get()))
        u = eval(str(self.entry[3].get()))

        # S = (T * t) / (u * 1.87 * r ** 2)
        Sj = f"({T} * {t}) / ({u} * 1.87 * {r} ** 2)"

        # t = t * 24 * 60
        tm = f"{t} * 24 * 60"

        # S = (T * t) / (u * 2693 * r ** 2)
        Sm = f"({T} * {Num(tm, 4)}) / ({u} * 2693 * {r} ** 2)"

        self.Clear()

        self.InputLaTexT(("T", T, "m^2/j"), ("T", T, "gpd/ft"), ("r", r, "m"), ("t", t, "j"),
                         (r"\frac{1}{u}", u, r"\, "))
        self.LaTexT("t en jours:", n_intro)
        self.LaTexT(r"$S = \frac{Tt}{\frac{1}{u} 1.87r^2}$", n_calcl)
        self.EvalLaTexT("S", Sj)

        self.LaTexT(f"Conversion du jours vers minutes:", n_intro)
        self.LaTexT(f"t = {t} {TX('jours')} = {Num(tm)} {TX('minutes')}", n_calcl)

        self.LaTexT("t en minutes:", n_intro)
        self.LaTexT(r"$S = \frac{Tt}{\frac{1}{u} 2693r^2}$", n_calcl)
        self.EvalLaTexT("S", Sm)

        r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.1. Equation de pompage de puits instable:
        Le coefficient de stockage:
            "$S = \frac{Tt}{\frac{1}{u} 1.87r^2}$" (t in days)
            
            "$S = \frac{Tt}{\frac{1}{u} 2693r^2}$" (t in minutes)
"""
        self.Draw()


# 4.2. Methode de solution de Theis ====================================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_1,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2, ]
        cls_name = ['La transmisivité',
                    'Le coefficient de stockage']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# La transmisivité -----------------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_1(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Le débit constant du puit (Q)",
                         "Le rabattement (s)",
                         "Fonction du puit (W(u))"]
        si_text = [f"m{sns(3)}/j", "m", ""]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.2. Methode de solution de Theis:", n_subtitle)

        self.LaTexT("La transmisivité (T):", n_subsub)

        self.LaTexT(r"Relation : $T = \frac{Q}{4 \pi s}W\left(u\right)$")

        self.Draw()

    def Application(self):
        Q = eval(str(self.entry[0].get()))
        s = eval(str(self.entry[1].get()))
        Wu = eval(str(self.entry[2].get()))

        # T = (Q / (4 * pi * s)) * Wu
        T = f"({Q} / (4 * pi * {s})) * {Wu}"

        self.Clear()

        self.InputLaTexT(("Q", Q, "m^3/j"), ("s", s, "m"), (r"W\left( u \right)", Wu, r"\, "))
        self.LaTexT(f"Calcul de la transmisivité ({TX('t')}):", n_intro)
        self.LaTexT(r"$T = \frac{Q}{4 \pi s}W\left(u\right)$", n_calcl)
        self.EvalLaTexT("T", T, "m^2/j")

        r"""
        
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE    
    4.2. Methode de solution de Theis:
        La transmisivité:
            "$T = \frac{Q}{4 \pi s}W\left(u\right)$"
"""
        self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["La transmisivité (T)",
                         f"la distance carré par le temps (r{sns(2)}/t)",
                         "(u)"]
        si_text = [f"m{sns(2)}/j", f"m{sns(2)}/j", ""]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.2. Methode de solution de Theis:", n_subtitle)

        self.LaTexT("Le coefficient de stockage (S):", n_subsub)

        self.LaTexT(r"Relation : $S = \frac{4Tu}{r^2/t}$")

        self.Draw()

    def Application(self):
        T = eval(str(self.entry[0].get()))
        rt = eval(str(self.entry[1].get()))
        u = eval(str(self.entry[2].get()))

        # S = (4 * T * u) / (rt)
        S = f"(4 * {T} * {u}) / {rt}"

        self.Clear()

        self.InputLaTexT(("T", T, "m^2/j"), ("r^2/t", rt, "m^2/j"), ("u", u, r"\, "))
        self.LaTexT("Calcul du coefficient de stockage (S):", n_intro)
        self.LaTexT(r"$S = \frac{4Tu}{r^2/t}$", n_calcl)
        self.EvalLaTexT("S", S)

        r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.2. Methode de solution de Theis:
        Le coefficient de stockage:
            "$S = \frac{4Tu}{r^2/t}$"
"""
        self.Draw()


# 4.3. Methode de solution de Cooper-Jacob =============================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_1,
                   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2, ]
        cls_name = ['La transmisivité',
                    'Le coefficient de stockage']

        self.NtBk = NoteBook(master=self, classes=classes, cls_name=cls_name)

    def Keyboard(self, keyword):
        self.NtBk.Keyboard(keyword)


# La transmisivité -----------------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_1(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_1, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["Le débit constant du puit (Q)",
                         "le différentiel de rabattement (∆s)"]
        si_text = [f"m{sns(3)}/j", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.3. Methode de solution de Cooper-Jacob:", n_subtitle)

        self.LaTexT("La transmisivité (T):", n_subsub)

        self.LaTexT(r"Relation : $T = \frac{2.303Q}{4\pi \Delta s}$")

        self.Draw()

    def Application(self):
        Q = eval(str(self.entry[0].get()))
        ds = eval(str(self.entry[1].get()))

        # T = 2.303 * Q / (4 * pi * ds)
        T = f"2.303 * {Q} / (4 * pi * {ds})"

        self.Clear()

        self.InputLaTexT(("Q", Q, "m^3/j"), (r"\Delta s", ds, "m"))
        self.LaTexT(f"Calcul de la transmisivité ({TX('t')}):", n_intro)
        self.LaTexT(r"$T = \frac{2.303Q}{4\pi \Delta s}$", n_calcl)
        self.EvalLaTexT("T", T, "m^2/j")

        r"""
        
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE    
    4.3. Methode de solution de Cooper-Jacob:
        La transmisivité:
            "$T = \frac{2.303Q}{4\pi \Delta s}$"
"""
        self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2(ttk.Frame):
    def __init__(self, master):
        super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2, self).__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        function_text = ["La transmisivité (T)",
                         f"Temps (t{sn(0)})",
                         "Distance (r)"]
        si_text = [f"m{sns(2)}/j", "j", "m"]

        self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

        self.entry = self.Master.entry
        self.Clear = self.Master.Clear
        self.LaTexT = self.Master.LaTexT
        self.Draw = self.Master.Draw
        self.EvalLaTexT = self.Master.EvalLaTexT
        self.InputLaTexT = self.Master.InputLaTexT
        self.Keyboard = self.Master.Keyboard

        self.RUN()

    def RUN(self):
        self.LaTexT("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:", n_title)

        self.LaTexT("4.3. Methode de solution de Cooper-Jacob:", n_subtitle)

        self.LaTexT("Le coefficient de stockage (S):", n_subsub)

        self.LaTexT(r"Relation : $S = \frac{2.246Tt_0}{r^2}$")

        self.Draw()

    def Application(self):
        T = eval(str(self.entry[0].get()))
        t0 = eval(str(self.entry[1].get()))
        r = eval(str(self.entry[2].get()))

        # S = (2.246 * T * t0) / (r ** 2)
        S = f"(2.246 * {T} * {t0}) / ({r} ** 2)"

        self.Clear()

        self.InputLaTexT(("T", T, "m^2/j"), ("t_0", t0, "j"), ("r", r, "m"))
        self.LaTexT("Calcul du coefficient de stockage (S):", n_intro)
        self.LaTexT(r"$S = \frac{2.246Tt_0}{r^2}$", n_calcl)
        self.EvalLaTexT("S", S)

        r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
    4.3. Methode de solution de Cooper-Jacob:
        Le coefficient de stockage:
            "$S = \frac{2.246Tt_0}{r^2}$"
"""
        self.Draw()


# 4.4. Methode de solution de Chow =====================================================================================

if __name__ == '__main__':
    # run Hydrogéologie
    Hydrogeologie()
