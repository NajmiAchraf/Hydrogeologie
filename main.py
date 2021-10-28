from init import *

from configparser import ConfigParser
from os import path, system
import os

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, font
from ttkthemes import ThemedStyle

from sympy import *
from sympy.solvers import solve
from sympy.solvers.solveset import solvify
from matplotlib import font_manager
import matplotlib as mpl

r"""
Hydrologie des eaux souterraines Livre de David Keith Todd

	Chapitre Ⅳ: Hydraulique des puits, pompage d'essai et étude des rabattements"

		1. ECOULEMENT UNIDIRECTIONNEL STABLE
			1. Aquifére confiné:
				
				$h=-\frac{vx}{K}$
		
			2. Aquifére non confiné:
			
				$q=\frac{K}{2x}\left({h_0^2-h^2}\right)$
		
			3. Débit de base vers un cours d'eau:
			
				$q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$
		
				$d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$
		
				$h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$
		
				$h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$
		
		2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS
			1. Aquifére confiné:
				1. Débit de pompage:
				
					$Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$
		
					$T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$
					
				2. Conductivité hydraulique:
				
					$K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$
					
				3. Niveau d'eau dans le puit pompé:
				
					$h_w=h_2-\frac{Q}{2\pi{Kb}}ln{\frac{r_2}{r_1}}$
					
				4. Rayon d'influence:
				
					$R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}$
		
			2. Aquifére non confiné:
				1. Débit de pompage:
				
					$Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$
			
					$T\cong{K}\frac{h_1+h_2}{2}$
				
				2. Conductivité hydraulique:
				
					$K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$
			
					$T\cong{K}\frac{h_1+h_2}{2}$
					
				3. Niveau d'eau dans le puit pompé:
				
					$h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}ln{\frac{r_2}{r_1}}}$
					
				4. Rayon d'influence:
				
					$R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}$
				
			3. Aquifére non confiné avec recharge uniforme:
				1. Equation de la courbe de rabattement:
				
					$h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)$
					
				2. Débit de pompage:
				
					$Q_w=\pi{r_{0}^{2}}W$
				
		3. PUIT DANS UN ECOULEMENT UNIFORME
			1. Conductivité hydraulique (K):
			
				$K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}$
				
			2. La pente de la surface piézométrique dans les conditions naturelles:
			
				$i=\frac{\Delta{h}}{\Delta{x}}$
				
			3. Les limites longitudinales et transversales des eaux souterraines entrant dans le puit:
			
				$y_L=\pm\frac{Q}{2Kbi}$
				
				$x_L=-\frac{Q}{2\pi{Kbi}}$
		
		4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
			1. Equation de pompage de puits instable:
				1. La Transmisivité:
				
					$T=\frac{114.6Q}{s}W\left(u\right)$
					
					$T=\frac{Q}{4\pi{s}}W\left(u\right)$
					
				2. Le coefficient de stockage:
				
					$S=\frac{Tt}{\frac{1}{u}1.87r^2}$ (t in days)
				
					$S=\frac{Tt}{\frac{1}{u}2693r^2}$ (t in minutes)
				
			2. Methode de solution de Theis:
				1. La Transmisivité:
				
					$T=\frac{Q}{4\pi{s}}W\left(u\right)$
					
				2. Le coefficient de stockage:
				
					$S=\frac{4Tu}{r^2/t}$
		
			3. Methode de solution de Cooper-Jacob:
				1. La Transmisivité:
				
					$T=\frac{2.303Q}{4\pi\Delta{s}}$
					
				2. Le coefficient de stockage:
				
					$S=\frac{2.246Tt_0}{r^2}$
			
			4. Methode de solution de Chow:
			
				$F\left(u\right)=\frac{s}{\Delta{s}}$
		
		5. FLUX RADIAL INSTANTANE DANS UN AQUIFERE NON CONFINE
		
			$s=\frac{Q}{4\pi{T}}W\left(u_a,u_y,\eta\right)$
		
			$u_a=\frac{r^{2}S}{4Tt}$
		
			$u_y=\frac{r^{2}S_y}{4Tt}$
		
			$\eta=\frac{r^{2}K_z}{b^{2}K_h}$
			
		6. ECOULEMENT RADIAL INSTABLE DANS UN AQUIFERE QUI FUIT
		
			$s=\frac{Q}{4\pi{T}}W\left(u,\frac{r}{B}\right)$
		
			$u=\frac{r^{2}S}{4Tt}$
		
			$\frac{r}{B}=\frac{r}{\sqrt{T'\left(\frac{K'}{b'}\right)}}$
			
		7. UN PUITS S'ECOULE PRES DES LIMITES DE L'AQUIFERE 
		
			$s_b=\frac{Q}{4\pi{T}}W\left(u_p\right)+\frac{Q}{4\pi{T}}W\left(u_i\right)$
		
			$u_p=\frac{r^{2}_{p}S}{4Tt_p}$
		
			$u_i=\frac{r^{2}_{i}S}{4Tt_i}$
		
		"""
'''
### [version 4.2.1.0 FV](https://github.com/NajmiAchraf/Hydrogeologie/releases/tag/v4.2.1.0-FV)

- nouvelles:
	- nouvelle fonction qui vérifie la police officielle de l'application si elle existe et l'installe sinon

- changements:
	- les boutons de contrôle ont de nouvelles icônes png
'''
__author__ = 'NajmiAchraf'
__version__ = '4.2.1.0 FV'
__title__ = 'Hydrogéologie'


if not path.exists('paramètre.ini'):
	Create_INI_File()

parser = ConfigParser()
parser.read('paramètre.ini')

font_name_gui = parser.get('settings', 'font_name_gui')
font_size_gui = parser.getint('settings', 'font_size_gui')
theme_style = parser.get('settings', 'theme_style')
font_name_xy = parser.get('settings', 'font_name_xy')
font_size_xy = parser.getint('settings', 'font_size_xy')

Titre_ID = True
if Titre_ID:
	identify = parser.get('settings', 'identify')
else:
	identify = 'NOURA NAJMI Master HIGH 2020/2021'

mpl_default = ['rm', 'it', 'tt', 'sf', 'bf', 'default', 'bb', 'regular']
mpl.rcParams['mathtext.default'] = mpl_default[7]  # 'regular'
mpl.rcParams["font.family"] = font_name_xy
mpl.rcParams["font.size"] = font_size_xy
# mpl_fontset = ['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']
# mpl.rcParams['mathtext.fontset'] = 'stixsans'

rgb_Black = ((0. / 255.), (0. / 255.), (0. / 255.))
rgb_White = ((255. / 255.), (255. / 255.), (255. / 255.))
rgb_Red = ((255. / 255.), (0. / 255.), (0. / 255.))  # FF0000
rgb_Lime = ((0. / 255.), (255. / 255.), (0. / 255.))  # 00FF00
rgb_Blue = ((0. / 255.), (0. / 255.), (255. / 255.))  # 0000FF
rgb_Yellow = ((255. / 255.), (255. / 255.), (0. / 255.))  # FFFF00
rgb_Cyan = ((0. / 255.), (255. / 255.), (255. / 255.))  # 00FFFF
rgb_Magenta = ((255. / 255.), (0. / 255.), (255. / 255.))  # FF00FF
rgb_Maroon = ((128. / 255.), (0. / 255.), (0. / 255.))  # 800000
rgb_Olive = ((128. / 255.), (128. / 255.), (0. / 255.))  # 808000
rgb_Green = ((0. / 255.), (128. / 255.), (0. / 255.))  # 008000
rgb_Purple = ((128. / 255.), (0. / 255.), (128. / 255.))  # 800080
rgb_Teal = ((0. / 255.), (128. / 255.), (128. / 255.))  # 008080
rgb_Navy = ((0. / 255.), (0. / 255.), (128. / 255.))  # 000080

hex_White = '#FFFFFF'
hex_Black = '#000000'
hex_Dark = '#050505'
hex_Dark_Gray = '#454545'
hex_Gray = '#5F5F5F'
hex_Light_Gray = '#737373'
hex_Orange = '#FF9900'
hex_Dark_Green = '#00751E'
hex_Green = '#009C27'
hex_Light_Green = '#20B645'

btn_set = {
	'padx': 18,
	'pady': 1,
	'bd': 1,
	'background': 'firebrick2',
	'fg': hex_White,
	'bg': 'firebrick2',
	'width': 2,
	'height': 1,
	'relief': 'raised',
	'activeback': 'firebrick3',
	'activebackground': 'firebrick4',
	'activeforeground': hex_Orange
}
ent_prm = {
	'foreground': hex_Black,
	'background': hex_White,
	'width': '15',
	'font': (font_name_gui, font_size_gui)
}
lbl_prm = {'anchor': 'w'}
si_prm = {'anchor': 'center'}

sn = SmallNumbers(10)
sns = SmallNumbers(10, "super")


# Master Window ////////////////////////////////////////////////////////////////////////////////////////////////////////
class Hydrogeologie(object):
	def __init__(self):
		# Window Configuration _________________________________________________________________________________________
		super(Hydrogeologie, self).__init__()
		self.Main = Tk()
		self.Main.iconbitmap(PathMainIcon('04-earth'))
		self.Main.iconify()
		self.Main.geometry("1313x600")
		self.Main.minsize(width=1133, height=500)
		self.Main.resizable(width=True, height=True)
		self.Main.title(u"%s v%s" % (__title__, __version__))
		self.Main.configure(background=hex_Dark)
		self.Main.bind_all('<Key>', self.Keyboard)

		# Fonts Configuration __________________________________________________________________________________________
		font_list = list(tk.font.families())
		font_list.sort()

		FontsConfiguration(font_list)

		# Themed Style _________________________________________________________________________________________________
		self.ThemeStyle = ThemedStyle()
		self.ThemedStyle(theme_style, font_name_gui, font_size_gui)

		# Menu Configuration ___________________________________________________________________________________________
		self.MenuBare = Menu(self.Main)
		self.File = Menu(self.MenuBare, tearoff=False)

		self.File.add_command(label='Paramètre', command=lambda: ConfigWindow(self))
		self.File.add_separator()
		self.File.add_command(label="Sortie", command=lambda: sys.exit())

		self.MenuBare.add_cascade(label="Fichier", menu=self.File)

		# NoteBook Configuration _______________________________________________________________________________________
		classes = [ECOULEMENT_UNIDIRECTIONNEL_STABLE,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS,
				   PUIT_DANS_UN_ECOULEMENT_UNIFORME,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE]
		cls_name = ['1. ECOULEMENT UNIDIRECTIONNEL STABLE',
					'2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS',
					'3. PUIT DANS UN ECOULEMENT UNIFORME',
					'4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE']

		self.NtBk = NoTeBooK(master=self.Main, classes=classes, cls_name=cls_name)

		# Window Configuration _________________________________________________________________________________________
		self.Main.config(menu=self.MenuBare)
		self.Main.rowconfigure(0, weight=1)
		self.Main.columnconfigure(0, weight=1)
		self.Main.protocol("WM_DELETE_WINDOW", sys.exit)

		self.Main.deiconify()
		self.TopMost(True)
		self.Main.update()
		self.TopMost(False)
		self.Main.mainloop()

	def TopMost(self, top):
		self.Main.attributes('-topmost', top)

	def Unbind(self):
		self.Main.unbind_all('<Key>')

	def Bind(self):
		self.Main.bind_all('<Key>', self.Keyboard)

	def Keyboard(self, keyword):
		self.NtBk.Keyboard(keyword)

	def Apply(self, font, size_xy, clear):
		self.NtBk.Apply(font, size_xy, clear)

	def ThemedStyle(self, theme_style, font_name_gui, font_size_gui):
		self.ThemeStyle.theme_use(theme_style)
		# All Widget Style Font ----------------------------------------------------------------------------------------
		self.ThemeStyle.configure('.', font=(font_name_gui, font_size_gui))
		# NoteBook Style -----------------------------------------------------------------------------------------------
		self.ThemeStyle.configure('TNotebook', background=hex_Dark)
		# NoteBook Tab Style -------------------------------------------------------------------------------------------
		self.ThemeStyle.configure('TNotebook.Tab', font=(font_name_gui, FontSizeNote(font_size_gui)))
		# Frame Style --------------------------------------------------------------------------------------------------
		self.ThemeStyle.configure('TFrame', background=hex_Dark)
		# Label Style --------------------------------------------------------------------------------------------------
		self.ThemeStyle.configure('TLabel', background=hex_Dark, foreground=hex_White)

		THEME = [
			"alt",  # _______0
			"black",  # _____1
			"clam",  # ______2
			"classic",  # ___3
			"default",  # ___4
		]
		if theme_style in THEME:
			# NoteBook Tab Style ---------------------------------------------------------------------------------------
			self.ThemeStyle.configure('TNotebook.Tab', background=hex_Light_Gray, foreground=hex_Black)
			self.ThemeStyle.map('TNotebook.Tab', foreground=[('active', hex_Orange), ("selected", hex_White)],
								background=[('active', hex_Dark_Gray), ("selected", hex_Dark)])

			# Button Style ---------------------------------------------------------------------------------------------
			self.ThemeStyle.configure('TButton', foreground=hex_White)
			self.ThemeStyle.map('TButton', foreground=[('pressed', hex_Orange), ('active', hex_Black)])

			self.ThemeStyle.configure('eff_ann.TButton', background='firebrick2')
			self.ThemeStyle.map('eff_ann.TButton', background=[('pressed', 'firebrick4'), ('active', 'firebrick3')])

			self.ThemeStyle.configure('mod_def.TButton', background=hex_Light_Gray)
			self.ThemeStyle.map('mod_def.TButton', background=[('pressed', hex_Dark_Gray), ('active', hex_Gray)])

			self.ThemeStyle.configure('cal_app.TButton', background=hex_Light_Green)
			self.ThemeStyle.map('cal_app.TButton', background=[('pressed', hex_Dark_Green), ('active', hex_Green)])


# Config Window \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class ConfigWindow(Toplevel):
	def __init__(self, parent):
		self.Parent = parent

		self.parser = ConfigParser()
		self.parser.read('paramètre.ini')
		self.x_pre, self.y_pre = 0, 0

		# Window Configuration _________________________________________________________________________________________
		super(ConfigWindow, self).__init__()
		self.WindowGeometry()
		self.Parent.Unbind()
		self.window_exist = True

		# TopLevel Configuration _______________________________________________________________________________________
		self.grab_set()  # when you show the popup
		self.geometry("350x400")
		self.minsize(width=350, height=400)
		self.resizable(width=False, height=False)
		self.title(u"Paramètre de %s" % __title__)
		self.configure(background=hex_Dark)
		self.protocol("WM_DELETE_WINDOW", self.ExitWindow)
		self.wm_overrideredirect(True)
		self.bind_all("<Configure>", self.WindowConfigure)
		self.bind_all("<ButtonRelease>", self.ApplyButton)
		self.bind_all("<Key>", self.ApplyButton)

		# Widgets ______________________________________________________________________________________________________

		# Frames -------------------------------------------------------------------------------------------------------

		text = ["configuration de l'interface", "configuration de feuille de calculs"]
		label_frame = []
		for fr in range(len(text)):
			label_frame.append(LabelFrame(self, text=text[fr]))
			label_frame[fr].grid(row=fr, column=0, sticky=NSEW)
			# label_frame[fr].columnconfigure(0, weight=1)
			label_frame[fr].columnconfigure(1, weight=1)
			label_frame[fr].columnconfigure(2, weight=1)

		frame = Frame(self)
		frame.grid(row=2, column=0, sticky=NSEW)

		# Labels -------------------------------------------------------------------------------------------------------

		label0 = []
		lbl_txt = ["Police & Taille :",
				   "Style Theme :"]
		for lb in range(len(lbl_txt)):
			label0.append(Label(label_frame[0], text=lbl_txt[lb], anchor='w'))
			label0[lb].grid(row=lb, column=0, sticky=NSEW)
			label_frame[0].rowconfigure(lb, weight=1)

		label1 = []
		if Titre_ID:
			lbl_txt = ["Police & Taille :",
					   "Titre ID :"]
		else:
			lbl_txt = ["Police & Taille :"]
		for lb in range(len(lbl_txt)):
			label1.append(Label(label_frame[1], text=lbl_txt[lb], anchor='w'))
			label1[lb].grid(row=lb, column=0, sticky=NSEW)
			label_frame[1].rowconfigure(lb, weight=1)

		# Fonts --------------------------------------------------------------------------------------------------------

		# font_gui tkiner
		font_gui = list(tk.font.families())
		font_gui.sort()

		# font_text matplolib
		font_xy = ([font for font in sorted(set([f.name for f in font_manager.fontManager.ttflist]))])
		font_list = [font_gui, font_xy]

		self.var_font = [StringVar(), StringVar()]
		self.var_font[0].set(self.parser.get('settings', 'font_name_gui'))
		self.var_font[1].set(self.parser.get('settings', 'font_name_xy'))

		om_font = []
		for omf in range(len(self.var_font)):
			om_font.append(ttk.Combobox(label_frame[omf], textvariable=self.var_font[omf], values=font_list[omf]))
			om_font[omf].grid(row=0, column=1, sticky=EW)

		# Theme Style --------------------------------------------------------------------------------------------------

		self.var_styl = StringVar()
		self.var_styl.set(self.parser.get('settings', 'theme_style'))
		THEMES = [
			"alt",  # _______0
			"black",  # _____1
			"clam",  # ______2
			"classic",  # ___3
			"default",  # ___4
			"elegance",  # __5
			"plastik",  # ___6
			"radiance",  # __7
			"scidblue",  # __8
			"scidgreen",  # _9
			"scidgrey",  # __10
			"scidmint",  # __11
			"scidpink",  # __12
			"scidpurple",  # 13
			"scidsand",  # __14
			"vista",  # _____15
			"winnative",  # _16
			"winxpblue",  # _17
			"xpnative",  # __18
			"yaru"  # _______19
		]
		ttk.Combobox(label_frame[0], textvariable=self.var_styl, values=THEMES).grid(row=1, column=1, columnspan=2,
																					 sticky=EW)

		# Size ---------------------------------------------------------------------------------------------------------

		size_list = []
		for sz in range(8, 14):
			size_list.append(int(sz))
		for zs in range(14, 25, 2):
			size_list.append(int(zs))

		self.var_size = [IntVar(), IntVar()]
		self.var_size[0].set(self.parser.getint('settings', 'font_size_gui'))
		self.var_size[1].set(self.parser.getint('settings', 'font_size_xy'))

		om_size = []
		for oms in range(len(self.var_size)):
			om_size.append(ttk.Combobox(label_frame[oms], textvariable=self.var_size[oms], values=size_list))
			om_size[oms].grid(row=0, column=2, sticky=EW)

		# Entry --------------------------------------------------------------------------------------------------------
		if Titre_ID:
			self.entry = Entry(label_frame[1])
			self.entry.grid(row=1, column=1, columnspan=2, sticky=EW)
			self.entry.insert(0, self.parser.get('settings', 'identify'))

		# Buttons ------------------------------------------------------------------------------------------------------

		txt = ["Annuler", "Par Défaut", "Appliquer"]
		self.btn = []
		for bt in range(len(txt)):
			self.btn.append(HoverButton(frame, text=txt[bt], **btn_set))
			self.btn[bt].grid(row=0, column=bt, sticky=EW)
			frame.columnconfigure(bt, weight=1)

		self.btn[0].configure(command=lambda: self.ExitWindow())

		self.btn[1].configure(command=lambda: self.Default())
		self.btn[1].change_color_bind(DefaultBG=hex_Light_Gray, HoverBG=hex_Gray, ActiveBG=hex_Dark_Gray)

		self.btn[2].configure(command=lambda: self.Appliquer(), state=DISABLED)
		self.btn[2].change_color_bind(DefaultBG=hex_Light_Green, HoverBG=hex_Green, ActiveBG=hex_Dark_Green)

		# TopLevel Configuration _______________________________________________________________________________________
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		self.update()
		self.Parent.Main.update()

	def WindowGeometry(self):
		x = self.Parent.Main.winfo_rootx()
		y = self.Parent.Main.winfo_rooty()
		self.wm_geometry("+%d+%d" % (x, y))

	def WindowConfigure(self, event):
		if not self.window_exist:
			return

		if self.x_pre != event.x or self.y_pre != event.y:
			self.x_pre, self.y_pre = event.x, event.y
			self.WindowGeometry()

	def ApplyButton(self, event):
		if not self.window_exist:
			return

		if Titre_ID:
			if self.parser.get('settings', 'font_name_gui') != self.var_font[0].get() or \
					self.parser.getint('settings', 'font_size_gui') != self.var_size[0].get() or \
					self.parser.get('settings', 'theme_style') != self.var_styl.get() or \
					self.parser.get('settings', 'font_name_xy') != self.var_font[1].get() or \
					self.parser.getint('settings', 'font_size_xy') != self.var_size[1].get() or \
					self.parser.get('settings', 'identify') != self.entry.get():
				self.btn[2].configure(state=NORMAL)
			else:
				self.btn[2].configure(state=DISABLED)

		elif not Titre_ID:
			if self.parser.get('settings', 'font_name_gui') != self.var_font[0].get() or \
					self.parser.getint('settings', 'font_size_gui') != self.var_size[0].get() or \
					self.parser.get('settings', 'theme_style') != self.var_styl.get() or \
					self.parser.get('settings', 'font_name_xy') != self.var_font[1].get() or \
					self.parser.getint('settings', 'font_size_xy') != self.var_size[1].get():
				self.btn[2].configure(state=NORMAL)
			else:
				self.btn[2].configure(state=DISABLED)

	@staticmethod
	def AskRestart():
		return messagebox.askyesno(title="Redémarrer",
								   message=f"Pour appliquez le changement sur Titre ID il faut redémarrer "
										   f"Hydrogéologie.\noui pour redémarrer et non pour rester.")

	@staticmethod
	def AskDelete():
		return messagebox.askyesno(title="appliquer les modifications ",
								   message=f"Pour appliquer les modifications sur les feuilles de calcul, "
										   f"elles doivent toutes être supprimées."
										   f"\noui pour supprimer si non fait le manuel.")

	def Appliquer(self):
		if self.window_exist:
			ask = NO

			if Titre_ID:
				Create_INI_File(font_name_gui=self.var_font[0].get(), font_size_gui=self.var_size[0].get(),
								theme_style=self.var_styl.get(),
								font_name_xy=self.var_font[1].get(), font_size_xy=self.var_size[1].get(),
								identify=self.entry.get())

				if self.parser.get('settings', 'identify') != self.entry.get():
					ask = self.AskRestart()
					if ask == YES:
						os.startfile(sys.argv[0])
						sys.exit()

			elif not Titre_ID:
				Create_INI_File(font_name_gui=self.var_font[0].get(), font_size_gui=self.var_size[0].get(),
								theme_style=self.var_styl.get(),
								font_name_xy=self.var_font[1].get(), font_size_xy=self.var_size[1].get())

			if self.parser.get('settings', 'font_name_xy') != self.var_font[1].get() or \
					self.parser.getint('settings', 'font_size_xy') != self.var_size[1].get():
				ask = self.AskDelete()

			self.Parent.ThemedStyle(theme_style=self.var_styl.get(),
									font_name_gui=self.var_font[0].get(),
									font_size_gui=self.var_size[0].get())

			old_font_size = mpl.rcParams["font.size"]
			mpl.rcParams["font.family"] = self.var_font[1].get()
			mpl.rcParams["font.size"] = self.var_size[1].get()

			self.Parent.Apply(font=(self.var_font[0].get(), self.var_size[0].get()),
							  size_xy=[old_font_size, self.var_size[1].get()], clear=ask)

			self.ExitWindow()

	def ExitWindow(self):
		if self.window_exist:
			self.window_exist = False
			self.Parent.Bind()
			self.grab_release()  # to return to normal
			self.destroy()

	def Default(self):
		self.var_font[0].set(self.parser.get('default', 'font_name_gui'))
		self.var_size[0].set(self.parser.getint('default', 'font_size_gui'))

		self.var_styl.set(self.parser.get('default', 'theme_style'))

		self.var_font[1].set(self.parser.get('default', 'font_name_xy'))
		self.var_size[1].set(self.parser.getint('default', 'font_size_xy'))

		if Titre_ID:
			self.entry.delete(0, END)
			self.entry.insert(0, self.parser.get('default', 'identify'))


# Master GUI ///////////////////////////////////////////////////////////////////////////////////////////////////////////
class GUI_MASTER(ttk.Frame):
	def __init__(self, master, Application, function_text, si_text, save_draw):

		self.Application = Application
		self.automatic = True

		# axe x Configuration (((bb.w1-bb.w2)/4)·100)÷73=x _____________________________________________________________
		self.n_identify = (128 * font_size_xy) / 100
		self.n_book = (64 * font_size_xy) / 100
		self.n_title2nd = (32 * font_size_xy) / 100
		self.n_title3rd = (64 * font_size_xy) / 100
		self.n_title4rd = (96 * font_size_xy) / 100
		self.n_intro = (32 * font_size_xy) / 100
		self.n_calcl = (64 * font_size_xy) / 100
		self.SizeXY = None
		# Frame Configuration __________________________________________________________________________________________
		super(GUI_MASTER, self).__init__(master=master)
		self.grid(row=0, column=0, sticky=NSEW)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)

		# Widgets ______________________________________________________________________________________________________

		# Frames -------------------------------------------------------------------------------------------------------
		self.frame1 = ttk.Frame(self)
		self.frame1.grid(row=0, column=0, sticky=NSEW)
		self.frame1.columnconfigure(1, weight=1)

		self.frame2 = ttk.Frame(self)
		self.frame2.grid(row=1, column=0, sticky=NSEW)
		self.frame2.columnconfigure(0, weight=1)
		self.frame2.columnconfigure(1, weight=1)
		self.frame2.columnconfigure(2, weight=1)

		# ScrollableTkAggXY --------------------------------------------------------------------------------------------
		self.FigureXY = FigureXY(figsize=(1, 1), save_draw=save_draw + 3, facecolor=hex_White)
		self.TkAggXY = ScrollableTkAggXY(figure=self.FigureXY, master=self)
		self.TkAggXY.grid(row=0, column=1, rowspan=2, sticky=NSEW)

		self.DelState()

		# Labels Entries -----------------------------------------------------------------------------------------------
		self.Range = len(function_text)
		self.entry = []
		label_function = []
		label_si = []

		for sd in range(self.Range):
			label_function.append(ttk.Label(self.frame1, text=function_text[sd], **lbl_prm))
			label_function[sd].grid(row=sd, column=0, sticky=NSEW)

			self.entry.append(ttk.Entry(self.frame1, **ent_prm))
			self.entry[sd].grid(row=sd, column=2, sticky=EW)

			label_si.append(ttk.Label(self.frame1, text=si_text[sd], **si_prm))
			label_si[sd].grid(row=sd, column=3, sticky=NSEW)

			self.frame1.rowconfigure(sd, weight=1)

		self.entry[0].focus_set()

		# Buttons ------------------------------------------------------------------------------------------------------
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
					  "\nCalculer : ajouter des calculs sur les anciens si ils existent dans la feuille de calcul",

			"calcul": "Description de la bouton Calculer ou Enter:\n"
					  "Calculer permet d'ajouter des calculs sur les anciens si ils existent dans la feuille de calcul"

		}
		self.button = []
		btn_txt = ["Effacer", "Mode Automatique", "Calculer"]
		btn_bal = [self.btn_auto['efface'], self.btn_auto['switch'], self.btn_auto['calcul']]
		btn_sty = ['eff_ann.TButton', 'mod_def.TButton', 'cal_app.TButton']

		for er in range(len(btn_txt)):
			self.button.append(
				HapticButton(self.frame2, style=btn_sty[er], text=btn_txt[er], balloon=btn_bal[er], width=15))
			self.button[er].grid(row=0, column=er, sticky=NSEW)

		self.button[0].configure(command=lambda: self.Delete())

		self.button[1].configure(command=lambda: self.Switcher())

		self.button[2].configure(command=lambda: self.Application())

		# LaTexT -------------------------------------------------------------------------------------------------------
		self.LaTexT(identify, self.n_identify, color=rgb_Blue)

		self.LaTexT(f'Hydrologie des eaux souterraines Livre de David Keith Todd', self.n_book, color=rgb_Red)

		self.LaTexT(f"Chapitre IV: Hydraulique des puits, pompage d'essai et étude des rabattements")

	def LaTexT(self, LaTexT, axe_x=0, color=rgb_Black):
		return self.FigureXY.DrawLaTex(LaTexT=LaTexT, axe_x=axe_x, color=color)

	def Title2ndTex(self, LaTexT, color=rgb_Maroon):
		self.LaTexT(LaTexT=LaTexT, axe_x=self.n_title2nd, color=color)

	def Title3rdTex(self, LaTexT, color=rgb_Teal):
		self.LaTexT(LaTexT=LaTexT, axe_x=self.n_title3rd, color=color)

	def Title4rdTex(self, LaTexT, color=rgb_Olive):
		self.LaTexT(LaTexT=LaTexT, axe_x=self.n_title4rd, color=color)

	def RelaTex(self, *args):
		if len(args) == 1:
			text = f"Relation : {TX(args[0])}"
		else:
			text = f"Relations : {TX(args[0])} "
			for gr in range(1, len(args)):
				text += r'$\Vert$'f" {TX(args[gr])} "

		self.LaTexT(text)
		del text

	def EntryTex(self, *args):
		text = f"Entrées : {TX(args[0][0])} = {args[0][1]}{TX(args[0][2])} "
		for gr in range(1, len(args)):
			text += r'$\Vert$'f" {TX(args[gr][0])} = {args[gr][1]}{TX(args[gr][2])} "
		self.LaTexT(text)
		del text

	def IntroTex(self, LaTexT, color=rgb_Navy):
		self.LaTexT(LaTexT=LaTexT, axe_x=self.n_intro, color=color)

	def CalclTex(self, LaTexT, color=rgb_Purple):
		self.LaTexT(LaTexT=LaTexT, axe_x=self.n_calcl, color=color)

	def EvalTex(self, expression, variable, unite=r"\! ", color=rgb_Green):
		result_str = Operation(variable, 'Before')
		result_expr = Operation(variable, 'After')
		result_num = Operation(variable, 'Number')
		# checking by zero
		dot_zero = str(result_num).replace('.0', '')

		if (result_expr == result_str) and (result_expr == result_num or result_expr == dot_zero):
			self.CalclTex(f'{TX(expression)} = {result_str} {TX(unite)}', color=color)

		elif (result_expr == dot_zero) or (result_expr == result_num):
			self.CalclTex(f'{TX(expression)} = {result_str}', color=rgb_Black)
			self.CalclTex(f'{TX(expression)} = {result_expr} {TX(unite)}', color=color)

		elif (result_expr != dot_zero) and (result_expr == result_str):
			self.CalclTex(f'{TX(expression)} = {result_expr}', color=rgb_Black)
			self.CalclTex(f'{TX(expression)} = {result_num} {TX(unite)}', color=color)
		else:
			self.CalclTex(f'{TX(expression)} = {result_str}', color=rgb_Black)
			self.CalclTex(f'{TX(expression)} = {result_expr}', color=rgb_Black)
			self.CalclTex(f'{TX(expression)} = {result_num} {TX(unite)}', color=color)

		del result_str, result_expr, result_num, dot_zero

	def Draw(self):
		self.FigureXY.Draw()

	def Keyboard(self, keyword):
		if keyword.keysym == "Return":
			self.Application()
		elif keyword.keysym == "Delete" and self.automatic:
			self.Delete()

	def Apply(self, font, size_xy, clear):
		for sd in range(self.Range):
			self.entry[sd].configure(font=font, background=hex_White, foreground=hex_Black)

		self.n_identify = (128 * size_xy[1]) / 100
		self.n_book = (64 * size_xy[1]) / 100
		self.n_title2nd = (32 * size_xy[1]) / 100
		self.n_title3rd = (64 * size_xy[1]) / 100
		self.n_title4rd = (96 * size_xy[1]) / 100
		self.n_intro = (32 * size_xy[1]) / 100
		self.n_calcl = (64 * size_xy[1]) / 100
		self.SizeXY = size_xy
		if clear == YES:
			self.FigureXY.Clear(size_xy=size_xy)

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
			self.FigureXY.Clear(size_xy=self.SizeXY)

	def Clear(self):
		if self.automatic:
			self.Delete()


# 1. ECOULEMENT UNIDIRECTIONNEL STABLE #################################################################################
class ECOULEMENT_UNIDIRECTIONNEL_STABLE(CLASS_MODEL):
	def __init__(self, master):
		super(ECOULEMENT_UNIDIRECTIONNEL_STABLE, self).__init__(master=master)

		classes = [ECOULEMENT_UNIDIRECTIONNEL_STABLE_1,
				   ECOULEMENT_UNIDIRECTIONNEL_STABLE_2,
				   ECOULEMENT_UNIDIRECTIONNEL_STABLE_3]
		cls_name = ['1.1. Aquifére confiné',
					'1.2. Aquifére non confiné',
					"1.3. Débit de base vers un cours d'eau"]

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# 1.1. Aquifére confiné ================================================================================================
class ECOULEMENT_UNIDIRECTIONNEL_STABLE_1(ttk.Frame):
	def __init__(self, master):
		super(ECOULEMENT_UNIDIRECTIONNEL_STABLE_1, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["Vitesse (v)",
						 "Distance (x)",
						 "Conductivité (K)"]
		si_text = ["m/j", "m", "m/j"]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("1. ECOULEMENT UNIDIRECTIONNEL STABLE:")

		self.Title3rdTex("1.1. Aquifére confiné:")

		self.Title4rdTex(f"Nappe Captive ({TX('h')}):")

		self.RelaTex(r"h=-\frac{vx}{K}")

		self.Draw()

	def Application(self):
		v = eval(str(self.entry[0].get()))
		x = eval(str(self.entry[1].get()))
		K = eval(str(self.entry[2].get()))

		# h = "- (v * x) / K"
		h = f"- ({v} * {x}) / {K}"

		self.Clear()

		self.EntryTex(('v', v, 'm/j'), ('x', x, 'm'), ('K', K, 'm/j'))
		self.IntroTex(f"Calcul de Nappe Captive ({TX('h')}):")
		self.CalclTex(r"$h=-\frac{vx}{K}$")
		self.EvalTex("h", h, "m")

		r"""
1. ECOULEMENT UNIDIRECTIONNEL STABLE:
	1.1. Aquifére confiné:
		"$h=-\frac{vx}{K}$"
"""
		self.Draw()


# 1.2. Aquifére non confiné ============================================================================================
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("1. ECOULEMENT UNIDIRECTIONNEL STABLE:")

		self.Title3rdTex("1.2. Aquifére non confiné:")

		self.Title4rdTex(f"Equation du puit ({TX('q')}):")

		self.RelaTex(r"q=\frac{K}{2x}\left({h_0^2-h^2}\right)")

		self.Draw()

	def Application(self):
		h = eval(str(self.entry[0].get()))
		h0 = eval(str(self.entry[1].get()))
		x = eval(str(self.entry[2].get()))
		K = eval(str(self.entry[3].get()))

		# q = f"( K / ( 2 * x )) * ( h0 ** 2 - h ** 2 )"
		q = f"( {K} / ( 2 * {x} )) * ( {h0} ** 2 - {h} ** 2 )"

		self.Clear()

		self.EntryTex(('h', h, 'm'), ('h_0', h0, 'm'), ('x', x, 'm'), ('K', K, 'm/j'))
		self.IntroTex(f"Calcul d'Equation du puit ({TX('q')}):")
		self.CalclTex(r"$q=\frac{K}{2x}\left({h_0^2-h^2}\right)$")
		self.EvalTex("q", q, 'm^2/j')

		r"""
	1.2. Aquifére non confiné:
		"$q=\frac{K}{2x}\left({h_0^2-h^2}\right)$"
"""
		self.Draw()


# 1.3. Débit de base vers un cours d'eau ===============================================================================
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("1. ECOULEMENT UNIDIRECTIONNEL STABLE:")

		self.Title3rdTex("1.3. Débit de base vers un cours d'eau:")

		self.RelaTex(r"q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)",
					 r"d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}",
					 r"h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d")

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
		qx = f"( ( ( ({h1} ** 2) - ({h2} ** 2) ) * {K}) / (2 * {L}) ) - ({eval(W)} * (( {L} / 2 ) - {x}))"

		# d = "(L / 2) - ((K / W) * (((h1 ** 2) - (h2 ** 2)) / (2 * L)))"
		d = f"({L} / 2) - (({K} / {eval(W)}) * ((({h1} ** 2) - ({h2} ** 2)) / (2 * {L})))"

		# First Method
		# hmax = "sqrt((h1 ** 2) - ((((h1 ** 2) - (h2 ** 2)) * d) / L) + ((W / K) * (L - d) * d))"
		hmax = f"sqrt(({h1}**2)-(((({h1}**2)-({h2}**2))*{eval(d)})/{L})+(({eval(W)}/{K})*({L}-{eval(d)})*{eval(d)}))"
		# Second Method
		hp = f"({h1}**2)-(((({h1}**2)-({h2}**2))*{eval(d)})/{L})+(({eval(W)}/{K})*({L}-{eval(d)})*{eval(d)})"
		hms = r"\sqrt{%s}" % eval(hp)
		hr = f"sqrt({eval(hp)})"

		self.Clear()

		self.EntryTex(("h_1", h1, "m"), ("h_2", h2, "m"), ("L", L, "m"), ("x", x, "m"), ("K", K, "m/j"),
					  ("W", Wa, "m/an"))
		self.IntroTex(f'Convertir la recharge ({TX("W")}) de {TX("m/an")} vers {TX("m/j")} :')
		self.CalclTex(TX(f"W = {Wa} / 365 = {eval(W)} m/j"), color=rgb_Green)

		self.IntroTex(f'Calcul de debit quotidien par Kilomètre de la nappe vers les deux rivières ({TX("q_x")}):')
		self.CalclTex(r"$q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$")
		self.EvalTex("q_x", qx, "m^2/j")

		self.IntroTex(f"Calcul de localisation de la ligne de partage d'eau souterraine ({TX('d')}):")
		self.CalclTex(r"$d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$")
		self.EvalTex("d", d, "m")

		self.IntroTex(f"Calcul de Hauteur Piézométrique maximale au niveau de la ligne de partage d'eau "
					  f"({TX('h_{max}')}):")
		# First Method
		self.IntroTex(f"Première méthode:")
		self.CalclTex(r"$h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$")
		self.CalclTex(r"$h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$")
		self.EvalTex("h_{max}", hmax, "m")
		# Second Method
		self.IntroTex(f"Deuxième méthode:")
		self.CalclTex(r"$h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$")
		self.EvalTex("h_{max}^2", hp, color=rgb_Black)
		self.CalclTex(TX(r"h_{max} = "f"{hms}"), color=rgb_Black)
		self.EvalTex("h_{max}", hr, "m")

		r"""
	1.3. Débit de base vers un cours d'eau:
		"$q_x=\frac{K\left({h_1^2-h_2^2}\right)}{2L}-W\left(\frac{L}{2}-x\right)$"

		"$d=\frac{L}{2}-\frac{K}{W}\frac{\left({h_0^2-h^2}\right)}{2L}$"

		"$h^2_{max}={h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d$"

		"$h_{max}=\sqrt{{h_1^2}-\frac{\left({h_1^2-h_2^2}\right)d}{L}+\frac{W}{K}\left(L-d\right)d}$"
"""
		self.Draw()


# 2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS ##########################################################################
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS(CLASS_MODEL):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS, self).__init__(master=master)

		classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3]
		cls_name = ['2.1. Aquifére confiné',
					'2.2. Aquifére non confiné',
					'2.3. Aquifére non confiné avec recharge uniforme']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# 2.1. Aquifére confiné ================================================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1(CLASS_MODEL):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1, self).__init__(master=master)

		classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_1,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_2,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_3,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_1_4]
		cls_name = ['Débit de pompage',
					'Conductivité hydraulique',
					"Niveau d'eau dans le puit pompé",
					"Rayon d'influence"]

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.1. Aquifére confiné:")

		self.Title4rdTex(f"Débit de pompage ({TX('Q')}):")

		self.RelaTex(r"Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}",
					 r"T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)")

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
		T2 = f"({eval(Q)} /({2} * pi * ({h2} - {h1}))) * (log({r2} / {r1}))"

		self.Clear()

		self.EntryTex(("h_1", h1, "m"), ("h_w", h1, "m"), ("h_2", h2, "m"), ("h", h2, "m"), ("r_1", r1, "m"),
					  ("r_w", r1, "m"), ("r_2", r2, "m"), ("r", r2, "m"), ("K", K, "m/j"), ("b", b, "m"))
		self.IntroTex(f'Calcul du Débit de pompage ({TX("Q")}):')
		self.CalclTex(r"$Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$")
		self.EvalTex("Q", Q, "m^3/j")

		self.IntroTex(f'Calcul de la premier relation de la Transmisivité ({TX("T")}) :')
		self.CalclTex(r"$T = Kb$")
		self.EvalTex("T", T1, "m^2/j")

		self.IntroTex(f'Calcul de la deuxième relation de la Transmisivité ({TX("T")}):')
		self.CalclTex(r"$T=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$")
		self.EvalTex("T", T2, "m^2/j")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.1. Aquifére confiné:
		Débit de pompage:
			"$Q=2\pi{Kb}\frac{h-h_w}{ln\left(\frac{r}{r_w}\right)}$"

			"$T=Kb=\frac{Q}{2\pi\left(h_1-h_2\right)}ln\left(\frac{r_2}{r_1}\right)$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.1. Aquifére confiné:")

		self.Title4rdTex(f"Conductivité hydraulique ({TX('K')}):")

		self.RelaTex(r"K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)")

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

		self.EntryTex(("h_w", hw, "m"), ("h", h, "m"), ("r_w", r, "m"), ("r", r, "m"), ("Q", Q, "m^3/j"), ("b", b, "m"))
		self.IntroTex(f'Calcul de la Conductivité hydraulique ({TX("K")}):')
		self.CalclTex(r"$K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$")
		self.EvalTex("K", K, "m/j")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.1. Aquifére confiné:
		Conductivité hydraulique:
			"$K=\frac{Q}{2\pi{b}\left(h-h_w\right)}ln\left(\frac{r}{r_w}\right)$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.1. Aquifére confiné:")

		self.Title4rdTex(f"Niveau d'eau dans le puit pompé ({TX('h_w')}):")

		self.RelaTex(r"h_w=h_2-\frac{Q}{2\pi{Kb}}ln{\frac{r_2}{r_1}}")

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

		self.EntryTex(("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"),
					  ("b", b, "m"))
		self.IntroTex(f"Calcul du niveau d'eau dans le puit pompé ({TX('h_w')}):")
		self.CalclTex(r"$h_w=h_2-\frac{Q}{2\pi{Kb}}ln{\frac{r_2}{r_1}}$")
		self.EvalTex("h_w", hw, "m")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.1. Aquifére confiné:
		Niveau d'eau dans le puit pompé:
			"$h_w=h_2-\frac{Q}{2\pi{Kb}}ln{\frac{r_2}{r_1}}$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.1. Aquifére confiné:")

		self.Title4rdTex(f"Rayon d'influence ({TX('R')}):")

		self.RelaTex(r"R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}")

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

		self.EntryTex(("h_0", h0, "m"), ("h_1", h1, "m"), ("r_1", r1, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"),
					  ("b", b, "m"))
		self.IntroTex(f"Calcul du Rayon d'influence ({TX('R')}):")
		self.CalclTex(r"$R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}$")
		self.EvalTex("R = r_0", R, "m")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.1. Aquifére confiné:
		Rayon d'influence
			"$R=r_0=r_1e^{\left(2\pi{Kb}\frac{h_0-h_1}{Q}\right)}$"
"""
		self.Draw()


# 2.2. Aquifére non confiné ============================================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2(CLASS_MODEL):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2, self).__init__(master=master)

		classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_1,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_2,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_3,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_2_4]
		cls_name = ['Débit de pompage',
					'Conductivité hydraulique',
					"Niveau d'eau dans le puit pompé",
					"Rayon d'influence"]

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.2. Aquifére non confiné:")

		self.Title4rdTex(f"Débit de pompage ({TX('Q')}):")

		self.RelaTex(r"Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}", r"T\cong{K}\frac{h_1+h_2}{2}")

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

		self.EntryTex(("h_1", h1, "m"), ("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"))
		self.IntroTex(f'Calcul du Débit de pompage ({TX("Q")}):')
		self.CalclTex(r"$Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$")
		self.EvalTex("Q", Q, 'm^3/j')

		self.IntroTex(f'Calcul de la Transmisivité ({TX("T")}):')
		self.CalclTex(r"$T\cong{K}\frac{h_1+h_2}{2}$")
		self.EvalTex("T", T, 'm^2/j')

		r"""
	2.2. Aquifére non confiné:
		Débit de pompage:
			"$Q=\pi{K}\frac{h^2_2-h^2_1}{ln\left(\frac{r_2}{r_1}\right)}$"

			"$T\cong{K}\frac{h_1+h_2}{2}$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.2. Aquifére non confiné:")

		self.Title4rdTex(f"Conductivité hydraulique ({TX('K')}):")

		self.RelaTex(r"K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)",
					 r"T\cong{K}\frac{h_1+h_2}{2}")

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

		self.EntryTex(("h_1", h1, "m"), ("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("Q", Q, "m^3/j"))
		self.IntroTex(f'Calcul de la Conductivité hydraulique ({TX("K")}):')
		self.CalclTex(r"$K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$")
		self.EvalTex("K", K, "m/j")

		self.IntroTex(f'Calcul de la Transmisivité ({TX("T")}):')
		self.CalclTex(r"$T\cong{K}\frac{h_1+h_2}{2}$")
		self.EvalTex("T", T, "m^2/j")

		r"""
	2.2. Aquifére non confiné:
		Conductivité hydraulique:
			"$K=\frac{Q}{\pi\left(h^2_2-h^2_1\right)}ln\left(\frac{r_2}{r_1}\right)$"

			"$T\cong{K}\frac{h_1+h_2}{2}$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.2. Aquifére non confiné:")

		self.Title4rdTex(f"Niveau d'eau dans le puit pompé ({TX('h_w')}):")

		self.RelaTex(r"h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}ln{\frac{r_2}{r_1}}}")

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

		self.EntryTex(("h_2", h2, "m"), ("r_1", r1, "m"), ("r_2", r2, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"))
		self.IntroTex(f"Calcul du niveau d'eau dans le puit pompé ({TX('h_w')}):")
		self.CalclTex(r"$h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}ln{\frac{r_2}{r_1}}}$")
		self.EvalTex("h_w", hw, "m")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.2. Aquifére non confiné:
		Niveau d'eau dans le puit pompé:
			"$h_w=\sqrt{h_2^2-\frac{Q}{\pi{K}}ln{\frac{r_2}{r_1}}}$"
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

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.2. Aquifére non confiné:")

		self.Title4rdTex(f"Rayon d'influence ({TX('R')}):")

		self.RelaTex(r"R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}")

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

		self.EntryTex(("h_0", h0, "m"), ("h_1", h1, "m"), ("r_1", r1, "m"), ("K", K, "m/j"), ("Q", Q, "m^3/j"))
		self.IntroTex(f"Calcul du Rayon d'influence ({TX('R')}):")
		self.CalclTex(r"$R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}$")
		self.EvalTex("R = r_0", R, "m")

		r"""
2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:
	2.2. Aquifére non confiné:
		Rayon d'influence
			"$R=r_0=r_{1}e^{\left(\pi{K}\frac{h_0^2-h_1^2}{Q}\right)}$"
"""
		self.Draw()


# 2.3. Aquifére non confiné avec recharge uniforme =====================================================================
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3(CLASS_MODEL):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3, self).__init__(master=master)

		classes = [ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_1,
				   ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_2]
		cls_name = ['Equation de la courbe de rabattement',
					'Débit de pompage']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# Equation de la courbe de rabattement ---------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_1(ttk.Frame):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_1, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["Niveau d'eau observé 1 (h)",
						 f"Niveau d'eau observé 2 (h{sn(0)})",
						 "Distance (r)",
						 "Conductivité (K)",
						 "Recharge (W)"]
		si_text = ["m", "m", "m", "m/j", "m/an"]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.r_0 = symbols('r_0')
		self.R = S.Reals
		self.C = S.Complexes
		self.solution_exist = True

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.3. Aquifére non confiné avec recharge uniforme:")

		self.Title4rdTex(f"Equation de la courbe de rabattement:")

		self.RelaTex(r"h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)",
					 r"Q_w=\pi{r_{0}^{2}}W")

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
			self.solution_exist = True
		except IndexError:
			messagebox.showerror(title="Erreur !!", message=f"L'équation de la courbe de rabattement n'a pas de "
															f"solution pour le Rayon d'influence r{sn(0)}")
			self.solution_exist = False

		if self.solution_exist:
			# Q = pi * r0 ** 2 * W
			Q = f"{pi} * {sympify(r0, evaluate=True).evalf()} ** 2 * {W}"

			self.Clear()

			self.EntryTex(("h", h, "m"), ("h_0", h0, "m"), ("r", r, "m"), ("K", K, "m/j"), ("W", W, "m/an"))
			self.IntroTex(f"Equation de la courbe de rabattement:")
			self.CalclTex(r"$h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)$")
			self.CalclTex(f"{Operation(q, 'Before')} = {Operation(p, 'Before')}", color=rgb_Black)
			self.CalclTex(Operation(Eq(sympify(q), sympify(p)), 'Before'), color=rgb_Black)
			self.IntroTex(
				f"Rayon d'influence ({TX('r_0')}) donné par la résolution d'équation de la courbe de rabattement:")
			self.EvalTex("r_0", r0, "m")

			self.IntroTex(f'Calcul du Débit de pompage ({TX("Q_w")}):')
			self.CalclTex(r"$Q_w=\pi{r_{0}^{2}}W$")
			self.EvalTex("Q_w", Q, "m^3/j")

			r"""
		2.3. Aquifére non confiné avec recharge uniforme:
			Equation de la courbe de rabattement:
				"$h^2_0-h^2=\frac{W}{2K}\left(r^2-r^2_0\right)+\frac{Q_w}{\pi{K}}ln\left(\frac{r_0}{r}\right)$"
				
			Débit de pompage:
				"$Q_w=\pi{r_{0}^{2}}W$"
	"""
			self.Draw()


# Débit de pompage -----------------------------------------------------------------------------------------------------
class ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_2(ttk.Frame):
	def __init__(self, master):
		super(ECOULEMENT_RADIAL_CONSTANT_VERS_UN_PUITS_3_2, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = [f"Rayon d'influence (r{sn(0)})",
						 "Recharge (W)"]
		si_text = ["m", "m/an"]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("2. ECOULEMENT RADIAL CONSTANT VERS UN PUITS:")

		self.Title3rdTex("2.3. Aquifére non confiné avec recharge uniforme:")

		self.Title4rdTex(f"Débit de pompage ({TX('Q')}):")

		self.RelaTex(r"Q_w=\pi{r_{0}^{2}}W")

		self.Draw()

	def Application(self):
		r0 = eval(str(self.entry[0].get()))
		W = eval(str(self.entry[1].get()))

		# Q = pi * r0 ** 2 * W
		Q = f"{pi} * {sympify(r0, evaluate=True).evalf()} ** 2 * {W}"

		self.Clear()

		self.EntryTex((f"r{sn(0)}", r0, "m"), ("W", W, "m/an"))
		self.IntroTex(f'Calcul du Débit de pompage ({TX("Q_w")}):')
		self.CalclTex(r"$Q_w=\pi{r_{0}^{2}}W$")
		self.EvalTex("Q_w", Q, "m^3/j")

		r"""
	2.3. Aquifére non confiné avec recharge uniforme:			
		Débit de pompage:
			"$Q_w=\pi{r_{0}^{2}}W$"
"""
		self.Draw()


# 3. PUIT DANS UN ECOULEMENT UNIFORME ##################################################################################
class PUIT_DANS_UN_ECOULEMENT_UNIFORME(CLASS_MODEL):
	def __init__(self, master):
		super(PUIT_DANS_UN_ECOULEMENT_UNIFORME, self).__init__(master=master)

		classes = [PUIT_DANS_UN_ECOULEMENT_UNIFORME_1,
				   PUIT_DANS_UN_ECOULEMENT_UNIFORME_2,
				   PUIT_DANS_UN_ECOULEMENT_UNIFORME_3]
		cls_name = ['Conductivité hydraulique',
					"La pente de la surface piézométrique dans les conditions naturelles",
					"Les limites longitudinales et transversales des eaux souterraines entrant dans le puit"]

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("3.PUIT DANS UN ECOULEMENT UNIFORME:")

		self.Title3rdTex('Conductivité hydraulique $(K)$:')

		self.RelaTex(r"K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}")

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

		self.EntryTex(("h_u", hu, "m"), ("h_d", hd, "m"), ("r", r, "m"), ("Q", Q, "m^3/j"), ("i_u", iu, r"\, "),
					  ("i_d", id, r"\, "))
		self.IntroTex("Calcul de la Conductivité hydraulique $(K)$:")
		self.CalclTex(r"$K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}$")
		self.EvalTex("K", K, "m/j")

		r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
	Conductivité hydraulique (K):
		"$K=\frac{2Q}{\pi{r\left(h_u+h_d\right)}\left(i_u+i_d\right)}$"
"""
		self.Draw()


# La pente de la surface piézométrique dans les conditions naturelles --------------------------------------------------
class PUIT_DANS_UN_ECOULEMENT_UNIFORME_2(ttk.Frame):
	def __init__(self, master):
		super(PUIT_DANS_UN_ECOULEMENT_UNIFORME_2, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["Le niveau piézométrique observé\nentre les deux puits (∆h)",
						 "La distance entre les deux puits (∆x)"]
		si_text = ["m", "m"]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=3)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("3.PUIT DANS UN ECOULEMENT UNIFORME:")

		self.Title3rdTex(f"La pente de la surface piézométrique dans les conditions naturelles ({TX('i')}):")

		self.RelaTex(r"i=\frac{\Delta{h}}{\Delta{x}}")

		self.Draw()

	def Application(self):
		dh = eval(str(self.entry[0].get()))
		dx = eval(str(self.entry[1].get()))

		# i = dh / dx
		i = f"{dh} / {dx}"

		self.Clear()

		self.EntryTex((r"\Delta h", dh, "m"), (r"\Delta x", dx, "m"))
		self.IntroTex("Calcul de la pente de la surface piézométrique dans les conditions naturelles $(i)$:")
		self.CalclTex(r"$i=\frac{\Delta{h}}{\Delta{x}}$")
		self.EvalTex("i", i)

		r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
	La pente de la surface piézométrique dans les conditions naturelles:
		$i=\frac{\Delta{h}}{\Delta{x}}$
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("3.PUIT DANS UN ECOULEMENT UNIFORME:")

		self.Title3rdTex(f"Les limites longitudinales et transversales des eaux souterraines entrant dans le puit "
						 f"({TX('y_L')}) & ({TX('x_L')}):")

		self.RelaTex(r"y_L=\pm\frac{Q}{2Kbi}", r"x_L=-\frac{Q}{2\pi{Kbi}}")

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

		self.EntryTex(("K", K, "m/j"), ("Q", Q, "m^3/j"), ("i", i, r"\, "), ("b", b, "m"))
		self.IntroTex("Calcul des limites longitudinales des eaux souterraines entrant dans le puit $y_L$:")
		self.CalclTex(r"$y_L=\pm\frac{Q}{2Kbi}$")
		self.EvalTex("y_L", yl, "m")

		self.IntroTex(f"Calcul des limites transversales des eaux souterraines entrant dans le puit $x_L$:")
		self.CalclTex(r"$x_L=-\frac{Q}{2\pi{Kbi}}$")
		self.EvalTex("x_L", xl, "m")

		r"""
3. PUIT DANS UN ECOULEMENT UNIFORME
	Les limites longitudinales et transversales des eaux souterraines entrant dans le puit:
		"$y_L=\pm\frac{Q}{2Kbi}$"
		
		"$x_L=-\frac{Q}{2\pi{Kbi}}$"
"""
		self.Draw()


# 4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE ###################################################################
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE(CLASS_MODEL):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE, self).__init__(master=master)

		classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3, ]
		# FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_4]
		cls_name = ['4.1. Equation de pompage de puits instable',
					'4.2. Methode de solution de Theis',
					'4.3. Methode de solution de Cooper-Jacob',
					'4.4. Methode de solution de Chow']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# 4.1. Equation de pompage de puits instable ===========================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1(CLASS_MODEL):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1, self).__init__(master=master)

		classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_1,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2, ]
		cls_name = ['La Transmisivité',
					'Le coefficient de stockage']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# La Transmisivité -----------------------------------------------------------------------------------------------------
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.1. Equation de pompage de puits instable:")

		self.Title4rdTex("La Transmisivité ($T$):")

		self.RelaTex(r"T=\frac{114.6Q}{s}W\left(u\right)", r"T=\frac{Q}{4\pi{s}}W\left(u\right)")

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

		self.EntryTex(("Q", Q, "gpm"), ("s", s, "ft"), (r"W\left( u \right)", Wu, r"\, "))
		self.IntroTex("La Transmisivité en gpd/ft:")
		self.CalclTex(r"$T=\frac{114.6Q}{s}W\left(u\right)$")
		self.EvalTex("T", T1, "gpd/ft")

		self.IntroTex(f"Conversion depuis les unités usuelles de U.S. vers S.I:")
		self.CalclTex(f"Q = {Q} {TX('gpm')} = {Operation(Qt, 'Number')} {TX('m^3/j')}", color=rgb_Black)
		self.CalclTex(f"s = {s} {TX('ft')} = {Operation(st, 'Number')} {TX('m')}", color=rgb_Black)

		self.IntroTex(f"La Transmisivité en {TX('m^2/j')}:")
		self.CalclTex(r"$T=\frac{Q}{4\pi{s}}W\left(u\right)$")
		self.EvalTex("T", T2, "m^2/j")

		# T = T1 * 0.01242
		T = f"{T1} * 0.01242"

		self.IntroTex(f"Vérifier que la Transmisivité en {TX('gpd/ft')} égale {TX('m^2/j')}:")

		self.CalclTex(f"T = {Operation(T, 'Before')}", color=rgb_Black)

		self.CalclTex(f"T = {Operation(T, 'Number')} {TX('m^2/j')}", color=rgb_Green)

		r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
	4.1. Equation de pompage de puits instable:
		La Transmisivité:
			"$T=\frac{114.6Q}{s}W\left(u\right)$"
			
			"$T=\frac{Q}{4\pi{s}}W\left(u\right)$"
"""
		self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2(ttk.Frame):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_1_2, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["La Transmisivité (T)",
						 "Distance (r)",
						 "Temps (t)",
						 "(1/u)"]
		si_text = [f"m{sns(2)}/j\ngpd/ft", "m", "j", ""]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.1. Equation de pompage de puits instable:")

		self.Title4rdTex("Le coefficient de stockage ($S$):")

		self.RelaTex(r"S=\frac{Tt}{\frac{1}{u}1.87r^2}\quad (t\; en\; jours)",
					 r"S=\frac{Tt}{\frac{1}{u}2693r^2}\quad (t\; en\; minutes)")

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
		Sm = f"({T} * {eval(tm)}) / ({u} * 2693 * {r} ** 2)"

		self.Clear()

		self.EntryTex(("T", T, "m^2/j"), ("T", T, "gpd/ft"), ("r", r, "m"), ("t", t, "j"), (r"\frac{1}{u}", u, r"\, "))
		self.IntroTex("t en jours:")
		self.CalclTex(r"$S=\frac{Tt}{\frac{1}{u}1.87r^2}$")
		self.EvalTex("S", Sj)

		self.IntroTex(f"Conversion du jours vers minutes:")
		self.CalclTex(f"t = {t} {TX('jours')} = {Operation(tm, 'Number')} {TX('minutes')}")

		self.IntroTex("t en minutes:")
		self.CalclTex(r"$S=\frac{Tt}{\frac{1}{u}2693r^2}$")
		self.EvalTex("S", Sm)

		r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
	4.1. Equation de pompage de puits instable:
		Le coefficient de stockage:
			"$S=\frac{Tt}{\frac{1}{u}1.87r^2}$" (t in days)
			
			"$S=\frac{Tt}{\frac{1}{u}2693r^2}$" (t in minutes)
"""
		self.Draw()


# 4.2. Methode de solution de Theis ====================================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2(CLASS_MODEL):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2, self).__init__(master=master)

		classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_1,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2, ]
		cls_name = ['La Transmisivité',
					'Le coefficient de stockage']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# La Transmisivité -----------------------------------------------------------------------------------------------------
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.2. Methode de solution de Theis:")

		self.Title4rdTex("La Transmisivité ($T$):")

		self.RelaTex(r"T=\frac{Q}{4\pi{s}}W\left(u\right)")

		self.Draw()

	def Application(self):
		Q = eval(str(self.entry[0].get()))
		s = eval(str(self.entry[1].get()))
		Wu = eval(str(self.entry[2].get()))

		# T = (Q / (4 * pi * s)) * Wu
		T = f"({Q} / (4 * pi * {s})) * {Wu}"

		self.Clear()

		self.EntryTex(("Q", Q, "m^3/j"), ("s", s, "m"), (r"W\left( u \right)", Wu, r"\, "))
		self.IntroTex(f"Calcul de la Transmisivité ({TX('t')}):")
		self.CalclTex(r"$T=\frac{Q}{4\pi{s}}W\left(u\right)$")
		self.EvalTex("T", T, "m^2/j")

		r"""
		
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE	
	4.2. Methode de solution de Theis:
		La Transmisivité:
			"$T=\frac{Q}{4\pi{s}}W\left(u\right)$"
"""
		self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2(ttk.Frame):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_2_2, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["La Transmisivité (T)",
						 f"la distance carré par le temps (r{sns(2)}/t)",
						 "(u)"]
		si_text = [f"m{sns(2)}/j", f"m{sns(2)}/j", ""]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.2. Methode de solution de Theis:")

		self.Title4rdTex("Le coefficient de stockage ($S$):")

		self.RelaTex(r"S=\frac{4Tu}{r^2/t}")

		self.Draw()

	def Application(self):
		T = eval(str(self.entry[0].get()))
		rt = eval(str(self.entry[1].get()))
		u = eval(str(self.entry[2].get()))

		# S = (4 * T * u) / (rt)
		S = f"(4 * {T} * {u}) / {rt}"

		self.Clear()

		self.EntryTex(("T", T, "m^2/j"), ("r^2/t", rt, "m^2/j"), ("u", u, r"\, "))
		self.IntroTex("Calcul du coefficient de stockage (S):")
		self.CalclTex(r"$S=\frac{4Tu}{r^2/t}$")
		self.EvalTex("S", S)

		r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
	4.2. Methode de solution de Theis:
		Le coefficient de stockage:
			"$S=\frac{4Tu}{r^2/t}$"
"""
		self.Draw()


# 4.3. Methode de solution de Cooper-Jacob =============================================================================
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3(CLASS_MODEL):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3, self).__init__(master=master)

		classes = [FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_1,
				   FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2, ]
		cls_name = ['La Transmisivité',
					'Le coefficient de stockage']

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)


# La Transmisivité -----------------------------------------------------------------------------------------------------
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
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.3. Methode de solution de Cooper-Jacob:")

		self.Title4rdTex("La Transmisivité ($T$):")

		self.RelaTex(r"T=\frac{2.303Q}{4\pi\Delta{s}}")

		self.Draw()

	def Application(self):
		Q = eval(str(self.entry[0].get()))
		ds = eval(str(self.entry[1].get()))

		# T = 2.303 * Q / (4 * pi * ds)
		T = f"2.303 * {Q} / (4 * pi * {ds})"

		self.Clear()

		self.EntryTex(("Q", Q, "m^3/j"), (r"\Delta s", ds, "m"))
		self.IntroTex(f"Calcul de la Transmisivité ({TX('t')}):")
		self.CalclTex(r"$T=\frac{2.303Q}{4\pi\Delta{s}}$")
		self.EvalTex("T", T, "m^2/j")

		r"""
		
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE	
	4.3. Methode de solution de Cooper-Jacob:
		La Transmisivité:
			"$T=\frac{2.303Q}{4\pi\Delta{s}}$"
"""
		self.Draw()


# Le coefficient de stockage -------------------------------------------------------------------------------------------
class FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2(ttk.Frame):
	def __init__(self, master):
		super(FLUX_RADIAL_INSTANTANE_DANS_UN_AQUIFERE_CONFINE_3_2, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		function_text = ["La Transmisivité (T)",
						 f"Temps (t{sn(0)})",
						 "Distance (r)"]
		si_text = [f"m{sns(2)}/j", "j", "m"]

		self.Master = GUI_MASTER(self, self.Application, function_text, si_text, save_draw=4)

		self.entry = self.Master.entry
		self.Clear = self.Master.Clear
		self.LaTexT = self.Master.LaTexT
		self.Title2ndTex = self.Master.Title2ndTex
		self.Title3rdTex = self.Master.Title3rdTex
		self.Title4rdTex = self.Master.Title4rdTex
		self.RelaTex = self.Master.RelaTex
		self.EntryTex = self.Master.EntryTex
		self.IntroTex = self.Master.IntroTex
		self.CalclTex = self.Master.CalclTex
		self.EvalTex = self.Master.EvalTex
		self.Draw = self.Master.Draw
		self.Keyboard = self.Master.Keyboard
		self.Apply = self.Master.Apply

		self.RUN()

	def RUN(self):
		self.Title2ndTex("4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE:")

		self.Title3rdTex("4.3. Methode de solution de Cooper-Jacob:")

		self.Title4rdTex("Le coefficient de stockage ($S$):")

		self.RelaTex(r"S=\frac{2.246Tt_0}{r^2}")

		self.Draw()

	def Application(self):
		T = eval(str(self.entry[0].get()))
		t0 = eval(str(self.entry[1].get()))
		r = eval(str(self.entry[2].get()))

		# S = (2.246 * T * t0) / (r ** 2)
		S = f"(2.246 * {T} * {t0}) / ({r} ** 2)"

		self.Clear()

		self.EntryTex(("T", T, "m^2/j"), ("t_0", t0, "j"), ("r", r, "m"))
		self.IntroTex("Calcul du coefficient de stockage (S):")
		self.CalclTex(r"$S=\frac{2.246Tt_0}{r^2}$")
		self.EvalTex("S", S)

		r"""
4. FLUX RADIAL INSTANTANE DANS UN AQUIFERE CONFINE
	4.3. Methode de solution de Cooper-Jacob:
		Le coefficient de stockage:
			"$S=\frac{2.246Tt_0}{r^2}$"
"""
		self.Draw()


# 4.4. Methode de solution de Chow =====================================================================================

if __name__ == '__main__':
	# run Hydrogéologie
	Hydrogeologie()
