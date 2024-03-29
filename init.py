from abc import ABC
from configparser import ConfigParser
import itertools
import pathlib
import sys
import tkinter as tk
from tkinter.ttk import Notebook
from tkinter import ttk
from ttkwidgets.autohidescrollbar import AutoHideScrollbar

from sympy import sympify, latex
from sympy.parsing.sympy_parser import parse_expr
from matplotlib.figure import Figure
from matplotlib.colors import to_hex
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backends._backend_tk import ToolTip
from Pmw.Pmw_2_0_1.lib.PmwBalloon import Balloon
import pyglet as pg


def FontSizeNote(font_size_gui):
	if font_size_gui <= 8:
		return font_size_gui
	elif 8 < font_size_gui <= 12:
		return int((4 * font_size_gui) / 5)
	else:
		return int((2 * font_size_gui) / 3)


def Create_INI_File(font_name_gui='DejaVu Sans', font_size_gui='16',
					theme_style='vista',
					font_name_xy='DejaVu Sans', font_size_xy='16',
					identify="Vous pouvez écrire n'importe quoi ici : Fichier >> Paramètre"):
	config = ConfigParser()

	config['default'] = {
		"font_name_gui": "DejaVu Sans", "font_size_gui": "16",
		"theme_style": "default",
		"font_name_xy": "DejaVu Sans", "font_size_xy": "16",
		"identify": "Vous pouvez écrire n'importe quoi ici : Fichier >> Paramètre"
	}

	config['settings'] = {
		"font_name_gui": font_name_gui, "font_size_gui": font_size_gui,
		"theme_style": theme_style,
		"font_name_xy": font_name_xy, "font_size_xy": font_size_xy,
		"identify": identify
	}

	with open('paramètre.ini', 'w') as fp:
		config.write(fp)


def TX(Math_Expression):
	TEX = '$' + Math_Expression + '$'
	return TEX


def LaTeX(Math_Expression):
	TEX = '$' + latex(Math_Expression) + '$'
	return TEX


def Operation(character, mode, *args):
	"""

	:param character: str
	:param mode: Before, After, AfterNum
	:return: LaTex
	"""

	pik = str(character)
	if mode == 'Before':
		try:
			expression = parse_expr(pik, evaluate=False)
		except Exception:
			expression = sympify(pik, rational=True, evaluate=False)

	elif mode == 'After':
		expression = sympify(pik, evaluate=True)

	elif mode == 'Number':
		if len(args) == 1 and isinstance(args[0], int):
				expression = sympify(pik, evaluate=True).evalf(args[0])
		else: expression = sympify(pik, evaluate=True).evalf()

	TEX = LaTeX(expression)
	symbol = [r'\log']
	func = ['ln']
	index = len(symbol)
	for num in range(index):
		TEX = TEX.replace(symbol[num], func[num])
	return TEX


def FontsConfiguration(font_list):
	install_font_name = ["DejaVu Sans"]
	install_font_file = ['DejaVuSans']
	for ft in range(len(install_font_name)):
		if install_font_name[ft] not in font_list:
			if sys.platform == "win32":
				pg.font.add_file(f'./Font/{install_font_file[ft]}.ttf')
				pg.font.load(install_font_name[ft])


def PathIconAdaptation(image_file):
	return f'{pathlib.Path(f"Icons/{image_file}").resolve()}32.png'


def PathMainIcon(image_file):
	return f'{pathlib.Path(f"Icons/{image_file}").resolve()}.ico'


class HoverButton(tk.Button):
	def __init__(self, master=None, balloon=None, status=None, cnf=None, **kwargs):
		if cnf is None:
			cnf = {}
		cnf = tk._cnfmerge((cnf, kwargs))
		super(HoverButton, self).__init__(master=master, cursor="hand2", cnf=cnf, **kwargs)

		self.kwargs = kwargs
		self.balloon = Balloon(master)
		self.DefaultBG = self.kwargs['bg']
		self.HoverBG = self.kwargs['activeback']
		self.change_balloon_bind(balloon=balloon, status=status)

	def change_balloon_bind(self, balloon=None, status=None):
		self.balloon.bind(self, balloonHelp=balloon, statusHelp=status)
		self.activate_color_bind()

	def activate_color_bind(self):
		self.bind("<Enter>", self.Enter, add='+')
		self.bind("<Leave>", self.Leave, add='+')

	def change_color_bind(self, DefaultBG, HoverBG, ActiveBG):
		self.configure(bg=DefaultBG, activebackground=ActiveBG)
		self.kwargs['bg'] = self.DefaultBG = DefaultBG
		self.kwargs['activeback'] = self.HoverBG = HoverBG

	def Enter(self, event):
		self['bg'] = self.HoverBG

	def Leave(self, event):
		self['bg'] = self.DefaultBG


class HapticButton(ttk.Button):
	def __init__(self, master=None, balloon=None, status=None, **kwargs):
		super(HapticButton, self).__init__(master=master, cursor="hand2", **kwargs)

		self.balloon = Balloon(master)
		self.change_balloon_bind(balloon=balloon, status=status)

	def change_balloon_bind(self, balloon=None, status=None):
		self.balloon.bind(self, balloonHelp=balloon, statusHelp=status)


class ToolbarController(NavigationToolbar2Tk, ABC):
	def __init__(self, canvas, window, *, pack_toolbar=True):
		self.toolitems = (
			('Delete', 'Effacer la feuille de calcul', 'delete', 'delete_history'),
			(None, None, None, None),
			('Save', 'Enregistrer la feuille de calcul', 'filesave', 'save_figure')
		)

		self.window = window
		self.BG = '#5F5F5F'
		self.ABG = '#454545'
		self.pad = 5

		tk.Frame.__init__(self, master=window, borderwidth=2, bg=self.BG,
						  width=int(canvas.figure.bbox.width), height=50)

		self._buttons = {}
		for text, tooltip_text, image_file, callback in self.toolitems:
			if text is None:
				# Add a spacer; return value is unused.
				self._Spacer()
			else:
				self._buttons[text] = button = self._Button(
					text=text,
					image_file=PathIconAdaptation(image_file),
					toggle=callback in ["zoom", "pan"],
					command=getattr(self, callback),
				)
				if tooltip_text is not None:
					ToolTip.createToolTip(button, tooltip_text)

		# This filler item ensures the toolbar is always at least two text
		# lines high. Otherwise the canvas gets redrawn as the mouse hovers
		# over images because those use two-line messages which resize the
		# toolbar.
		label = tk.Label(master=self,
						 text='\N{NO-BREAK SPACE}\n\N{NO-BREAK SPACE}', bg=self.BG)
		label.pack(side=tk.RIGHT)

		self.message = tk.StringVar(master=self)
		self._message_label = tk.Label(master=self, textvariable=self.message, bg=self.BG, fg="#FFFFFF")
		self._message_label.pack(side=tk.RIGHT)

		NavigationToolbar2.__init__(self, canvas)
		if pack_toolbar:
			self.pack(side=tk.BOTTOM, fill=tk.X)

		# hide the motion notify event (x,y)
		self.canvas.mpl_disconnect(self._id_drag)

	def delete_history(self):
		self.canvas.figure.Clear()
		self.canvas.draw()

	def delete_state(self, automatic):
		if not automatic:
			self._buttons['Delete']['state'] = tk.NORMAL

		elif automatic:
			self._buttons['Delete']['state'] = tk.DISABLED

	def _Button(self, text, image_file, toggle, command):
		image = (tk.PhotoImage(master=self, file=image_file)
				 if image_file is not None else None)
		if not toggle:
			b = tk.Button(
				master=self,
				text=text,
				padx=self.pad,
				image=image,
				command=command,
				bg=self.BG,
				activebackground=self.ABG
			)
		else:
			# There is a bug in tkinter included in some python 3.6 versions
			# that without this variable, produces a "visual" toggling of
			# other near checkbuttons
			# https://bugs.python.org/issue29402
			# https://bugs.python.org/issue25684
			var = tk.IntVar(master=self)
			b = tk.Checkbutton(
				master=self, text=text, image=image, command=command, padx=self.pad,
				bg=self.BG, activebackground=self.ABG, selectcolor=self.ABG,
				indicatoron=False, variable=var)
			b.var = var
		b._ntimage = image
		b.pack(side=tk.LEFT)
		return b


class ScrollableTkAggXY(tk.Canvas):
	def __init__(self, figure, master, **kw):
		figure.InputTkAggXY(self)
		facecolor = str(to_hex(figure.get_facecolor()))
		# --- create canvas with scrollbar ---
		super(ScrollableTkAggXY, self).__init__(master, background=facecolor, **kw)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		self.fig_canvas_xy = tk.Canvas(self, background=facecolor)
		self.fig_canvas_xy.grid(row=1, column=0, sticky=tk.NSEW)
		self.fig_canvas_xy.rowconfigure(0, weight=1)
		self.fig_canvas_xy.columnconfigure(0, weight=1)

		self.fig_wrapper_xy = tk.Frame(self.fig_canvas_xy, background=facecolor)
		self.fig_wrapper_xy.grid(row=0, column=0, sticky=tk.NSEW)
		self.fig_wrapper_xy.rowconfigure(0, weight=1)
		self.fig_wrapper_xy.columnconfigure(0, weight=1)

		self.TkAgg = FigureCanvasTkAgg(figure, master=self.fig_wrapper_xy)
		self.AggWidget = self.TkAgg.get_tk_widget()
		self.AggWidget.grid(row=0, column=0, sticky=tk.NSEW)

		self.vbar = AutoHideScrollbar(self, orient=tk.VERTICAL, command=self.fig_canvas_xy.yview)
		self.vbar.grid(row=1, column=1, sticky=tk.NS)

		self.hbar = AutoHideScrollbar(self, orient=tk.HORIZONTAL, command=self.fig_canvas_xy.xview)
		self.hbar.grid(row=2, column=0, sticky=tk.EW)

		self.fig_canvas_xy.configure(yscrollcommand=self.vbar.set, xscrollcommand=self.hbar.set,
									 scrollregion=self.fig_canvas_xy.bbox(tk.ALL))

		# --- put frame in canvas ---
		self.canvas_frame = self.fig_canvas_xy.create_window((0, 0), window=self.fig_wrapper_xy, width=600, height=100,
															 anchor=tk.NW)

		self.ToolBarFrame = tk.Frame(self)
		self.ToolBarFrame.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

		self.ToolBar = ToolbarController(self.TkAgg, self.ToolBarFrame)
		self.ToolBar.update()

		ScrollBind(canvas_self=self, canvas_widget=self.fig_canvas_xy, y_scroll=True, x_scroll=True,
				   hbar=self.hbar, vbar=self.vbar)

	# expand canvas_frame when canvas changes its size
	def OnConfigure_XY(self, width, height):
		# when all widgets are in canvas
		self.fig_canvas_xy.itemconfigure(self.canvas_frame, width=width + 20, height=height + 20)
		# update scrollregion after starting 'mainloop'
		self.fig_canvas_xy.configure(scrollregion=self.fig_canvas_xy.bbox(tk.ALL))
		self.fig_canvas_xy.yview_moveto(1)
		self.fig_canvas_xy.xview_moveto(0)

	def Draw(self, width, height):
		self.OnConfigure_XY(width=width, height=height)
		self.TkAgg.draw()

	# shortcut of delete state
	def delete_state(self, automatic):
		self.ToolBar.delete_state(automatic)


class FigureXY(Figure):
	rgb_Black = ((0. / 255.), (0. / 255.), (0. / 255.))
	rgb_White = ((255. / 255.), (255. / 255.), (255. / 255.))

	def __init__(self, save_draw=3, **kwargs):
		super(FigureXY, self).__init__(tight_layout=True, **kwargs)
		self.save_draw = save_draw

		self.tex_draw = 1

		self.latex_math = []
		self.latex_line = []
		self.rgb_color = []

		self.singing_math = []
		self.singing_line = []
		self.singing_color = []

		self.size_w = [100]
		self.size_h = 10
		self.max_w = max(self.size_w)
		self.max_h = float(self.size_h)

		# Set subplot
		self.Axes = self.add_subplot(1, 1, 1)
		self.Text = self.Axes.text(0, 1, '')

	def DrawLaTex(self, LaTexT, axe_x=0, color=rgb_Black):
		"""

		:param LaTexT: input LaTeX or text of each line
		:param axe_x: set the vertical position of text pending on axe x
		:param color: set color for text
		:return: set function Draw at the end of lines you input
		"""
		if self.save_draw >= self.tex_draw:
			self.latex_math.append(LaTexT)
			self.latex_line.append(axe_x)
			self.rgb_color.append(color)

		# Texting directly
		self.Text = self.Axes.text(x=axe_x,
								   y=0.5 - self.tex_draw,
								   s=LaTexT,
								   color=color)

		Renderer = self.canvas.get_renderer(cleared=True)
		bb = self.Text.get_window_extent(renderer=Renderer)
		self.size_w.append(int(bb.width) + (axe_x * 10) + 80)
		self.size_h += (float(bb.height) * 2)

		self.max_w = max(self.size_w)
		self.max_h = float(self.size_h)
		self.size_w.clear()
		self.size_w.append(self.max_w)

		# Configure the coordination of subplot
		self.Axes.set_ylim((-self.tex_draw, 0))
		self.Axes.set_xlim((0, (self.max_w + 20) / 10))
		# self.Axes._set_title_offset_trans('Master HIGH 2020/2021')
		self.Axes.axis('off')
		self.Axes.set_xticklabels("", visible=False)
		self.Axes.set_yticklabels("", visible=False)

		self.tex_draw += 1

		# self.tight_layout()

		return bb
		# del Renderer, bb

	def InputTkAggXY(self, TkAgg):
		"""

		:param TkAgg: set the ScrollableTkAggXY before call Draw from the FigureXY
		:return:
		"""
		self.TkAggXY = TkAgg

	def Draw(self):
		self.tight_layout()
		self.TkAggXY.Draw(width=self.max_w, height=self.max_h)

	def Clear(self, size_xy=None):
		self.clear()

		self.tex_draw = 1

		for lil in range(self.save_draw):
			self.singing_math.append(self.latex_math[lil])
			self.singing_line.append(self.latex_line[lil])
			self.singing_color.append(self.rgb_color[lil])

		self.latex_math.clear()
		self.latex_line.clear()
		self.rgb_color.clear()

		self.size_w.clear()
		self.size_w.append(100)
		self.size_h = 10

		# Set subplot
		self.Axes = self.add_subplot(1, 1, 1)

		for lil in range(self.save_draw):
			if size_xy is None:
				self.DrawLaTex(self.singing_math[lil], self.singing_line[lil], self.singing_color[lil])
			else:
				original_percent_axe = (self.singing_line[lil] * 100) / size_xy[0]
				new_percent_axe = (original_percent_axe * size_xy[1]) / 100
				self.DrawLaTex(self.singing_math[lil], new_percent_axe, self.singing_color[lil])

		self.Draw()


class SmallNumbers(object):
	def __init__(self, total_of_numbers, place_of_script='sub'):
		"""
		:param total_of_numbers: input integer or string numbers to get list of string numbers
		:param place_of_script: sub or super, default is sub
		"""
		try:
			self.total_nbrs = int(eval(total_of_numbers))
		except TypeError:
			self.total_nbrs = int(total_of_numbers)

		self.place_of_script = str(place_of_script).lower()

		if self.place_of_script == 'sub':
			self.work_list = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
			self.generated_list = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']

		elif self.place_of_script == 'super':
			self.work_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
			self.generated_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

		if self.total_nbrs >= 10:
			start = 10
			end = 100
			for cmb in range(2, len(str(self.total_nbrs)) + 1):
				self.ListOfCombinations(is_upper_then=start, is_under_then=end, combinations=cmb)
				start *= 10
				end *= 10

	def __call__(self, call_number, *args, **kwargs):
		return self.generated_list[call_number]

	def ListOfCombinations(self, is_upper_then, is_under_then, combinations):
		multi_work_list = eval(str('self.work_list,') * combinations)
		nbr = 0
		for subset in itertools.product(*multi_work_list):
			if is_upper_then <= nbr < is_under_then:
				self.generated_list.append(''.join(subset))
				if self.total_nbrs == nbr:
					break
			nbr += 1


class ScrollBind(object):
	def __init__(self, canvas_self, canvas_widget, y_scroll, x_scroll, vbar=None, hbar=None):
		self.canvas_self, self.canvas_widget = canvas_self, canvas_widget
		self.y_scroll, self.x_scroll = y_scroll, x_scroll
		self.scroll_inch = 3

		if self.y_scroll:
			self.canvas_self.bind_all("<MouseWheel>", self.MouseWheelHandler)
			self.vbar = vbar
		if self.x_scroll:
			self.canvas_self.bind_all("<Shift-MouseWheel>", self.ShiftMouseWheelHandler)
			self.hbar = hbar
		self.canvas_self.bind_all("<Button>", self.TouchPadHandler)
		self.canvas_self.bind('<Enter>', self.BoundToScrolling)
		self.canvas_self.bind('<Leave>', self.UnboundToScrolling)

	def BoundToScrolling(self, event):
		if self.y_scroll:
			self.canvas_self.bind_all("<MouseWheel>", self.MouseWheelHandler)
		if self.x_scroll:
			self.canvas_self.bind_all("<Shift-MouseWheel>", self.ShiftMouseWheelHandler)
		self.canvas_self.bind_all("<Button>", self.TouchPadHandler)

	def UnboundToScrolling(self, event):
		if self.y_scroll:
			self.canvas_self.unbind_all("<MouseWheel>")
		if self.x_scroll:
			self.canvas_self.unbind_all("<Shift-MouseWheel>")
		self.canvas_self.unbind_all("<Button>")

	# windows mouse wheel scrolling vertical
	def MouseWheelHandler(self, event):
		x, y = self.vbar.get()
		if x == 0.0 and y == 1.0:
			return
		self.canvas_widget.yview_scroll(int(-self.scroll_inch * (event.delta / 120)), "units")

	# windows shift mouse wheel scrolling horizontal
	def ShiftMouseWheelHandler(self, event):
		x, y = self.hbar.get()
		if x == 0.0 and y == 1.0:
			return
		self.canvas_widget.xview_scroll(int(self.scroll_inch * (event.delta / 120)), "units")

	# linux touchpad scrolling horizontal
	def TouchPadHandler(self, event):
		x, y = self.hbar.get()
		if x == 0.0 and y == 1.0:
			return

		if event.num == 6:
			self.canvas_widget.xview_scroll(-self.scroll_inch, "units")

		elif event.num == 7:
			self.canvas_widget.xview_scroll(self.scroll_inch, "units")


class NoTeBooK(Notebook):
	def __init__(self, master, classes, cls_name, **kw):
		super(NoTeBooK, self).__init__(master=master, **kw)

		self.NtBk_tab = 0
		self.TotalTabs = len(classes)

		self.Classes = []
		for nb in range(self.TotalTabs):
			cls = classes[nb](master=self)
			self.Classes.append(cls)
			self.add(cls, text=cls_name[nb])

		self.grid(row=0, column=0, sticky=tk.NSEW)
		self.bind('<Button-1>', self.IdentifyTab)

	def Identify(self, event):
		return self.tk.call(self._w, "identify", "tab", event.x, event.y)

	def IdentifyTab(self, event):
		try:
			self.NtBk_tab = int(self.Identify(event))
		except Exception:
			pass

	def Keyboard(self, keyword):
		for cls in range(self.TotalTabs):
			if self.NtBk_tab == cls:
				self.Classes[cls].Keyboard(keyword)

	def Apply(self, font, size_xy, clear):
		for cls in range(self.TotalTabs):
			self.Classes[cls].Apply(font, size_xy, clear)


class CLASS_MODEL(ttk.Frame):
	def __init__(self, master):
		super(CLASS_MODEL, self).__init__(master=master)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		classes = []
		cls_name = []

		self.NtBk = NoTeBooK(master=self, classes=classes, cls_name=cls_name)

	def Keyboard(self, keyword):
		self.NtBk.Keyboard(keyword)

	def Apply(self, font, size_xy, clear):
		self.NtBk.Apply(font, size_xy, clear)