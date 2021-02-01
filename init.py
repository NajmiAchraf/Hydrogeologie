import tkinter as tk
from sympy import sympify, latex
from sympy.parsing.sympy_parser import parse_expr
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Pmw.Pmw_2_0_1.lib.PmwBalloon import Balloon


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


class ToolbarController(NavigationToolbar2Tk):
    def __init__(self, canvas_, parent_):
        self.toolitems = (
            (None, None, None, None),
            ('Delete', 'Clear the paper work', 'delete', 'delete_history'),
            (None, None, None, None),
            ('Save', 'Save the paper work', 'filesave', 'save_figure'),
            (None, None, None, None)
        )
        NavigationToolbar2Tk.__init__(self, canvas_, parent_)

    def delete_history(self):
        self.canvas.figure.Clear()
        self.canvas.draw()


class ScrollableTkAggXY(tk.Canvas):
    def __init__(self, figure, master, **kw):
        # --- create canvas with scrollbar ---
        super(ScrollableTkAggXY, self).__init__(master, **kw)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        figure.InputTkAggXY(self)

        self.fig_canvas_xy = tk.Canvas(self)
        self.fig_canvas_xy.grid(row=1, column=0, sticky=tk.NSEW)
        self.fig_canvas_xy.rowconfigure(0, weight=1)
        self.fig_canvas_xy.columnconfigure(0, weight=1)

        self.fig_wrapper_xy = tk.Frame(self.fig_canvas_xy)
        self.fig_wrapper_xy.grid(row=0, column=0, sticky=tk.NSEW)
        self.fig_wrapper_xy.rowconfigure(0, weight=1)
        self.fig_wrapper_xy.columnconfigure(0, weight=1)

        self.TkAgg = FigureCanvasTkAgg(figure, master=self.fig_wrapper_xy)
        self.AggWidget = self.TkAgg.get_tk_widget()
        self.AggWidget.grid(row=0, column=0, sticky=tk.NSEW)

        self.vbar = AutoScrollbar(self, orient=tk.VERTICAL, command=self.fig_canvas_xy.yview)
        self.vbar.grid(row=1, column=1, sticky=tk.NS)

        self.hbar = AutoScrollbar(self, orient=tk.HORIZONTAL, command=self.fig_canvas_xy.xview)
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
        self.fig_canvas_xy.itemconfigure(self.canvas_frame, width=width + 21, height=height + 20)
        # update scrollregion after starting 'mainloop'
        self.fig_canvas_xy.configure(scrollregion=self.fig_canvas_xy.bbox(tk.ALL))
        self.fig_canvas_xy.yview_moveto(1)
        self.fig_canvas_xy.xview_moveto(0)

    def Draw(self, width, height):
        self.OnConfigure_XY(width=width, height=height)
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
        """

        :param character: input LaTeX or text of each line
        :return: set function Draw at the end of lines you input
        """

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
        self.size_w.append(int(bb.width))
        self.size_h += (float(bb.height) * 2)

        self.width = max(self.size_w)
        self.height = float(self.size_h)

        del Renderer
        del bb

        # try:
        #     self.tight_layout()
        # except Exception:
        #     pass

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
        singing_prog = self.latex_math[0]
        singing_mode = self.latex_math[1]
        self.latex_math.clear()
        self.size_w.clear()
        self.size_w.append(10)
        self.size_h = 10
        self.DrawLaTex(singing_prog)
        self.DrawLaTex(singing_mode)
        self.Draw()
        del singing_prog
        del singing_mode


class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError("cannot use pack with this widget")

    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")


class ScrollBind(object):
    def __init__(self, canvas_self, canvas_widget, y_scroll, x_scroll, vbar=None, hbar=None):
        self.canvas_self, self.canvas_widget = canvas_self, canvas_widget
        self.y_scroll, self.x_scroll = y_scroll, x_scroll
        self.scroll_inch = 5

        if self.y_scroll:
            self.canvas_self.bind_all("<MouseWheel>", self.MouseWheelHandler)
            self.vbar = vbar
        if self.x_scroll:
            self.canvas_self.bind_all("<Shift-MouseWheel>", self.ShiftMouseWheelHandler)
            self.hbar = hbar
        self.canvas_self.bind_all("<Button>", self.TouchPadHandler)
        self.canvas_self.bind('<Enter>', self.BoundToScroling)
        self.canvas_self.bind('<Leave>', self.UnboundToScroling)

    def BoundToScroling(self, event):
        if self.y_scroll:
            self.canvas_self.bind_all("<MouseWheel>", self.MouseWheelHandler)
        if self.x_scroll:
            self.canvas_self.bind_all("<Shift-MouseWheel>", self.ShiftMouseWheelHandler)
        self.canvas_self.bind_all("<Button>", self.TouchPadHandler)

    def UnboundToScroling(self, event):
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
