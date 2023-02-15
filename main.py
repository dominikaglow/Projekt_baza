import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from enum import Enum


class Tab_Typ(Enum):
    MOVIE = 1
    ACTOR = 2
    LINK = 3


class Window:
    def __init__(self, master):
        super().__init__()

        # defining files names
        self.FILEMOVIE = 'movie.json'
        self.FILEACTOR = 'actor.json'
        self.FILELINK = 'link.json'

        self.master = master
        self.photo_m = tk.PhotoImage(file='tape_16.png')
        self.photo_a = tk.PhotoImage(file='actor_16.png')
        self.photo_add = tk.PhotoImage(file='add.png')
        self.photo_update = tk.PhotoImage(file='update.png')
        self.photo_delete = tk.PhotoImage(file='delete.png')
        self.photo_clear = tk.PhotoImage(file='clear.png')
        self.photo_exit = tk.PhotoImage(file='exit.png')
        self.photo_delete_a = tk.PhotoImage(file='delete_a.png')
        self.photo_add_a = tk.PhotoImage(file='add_a.png')
        # lists movies, actor, link
        self.my_data_list_m = []
        self.my_data_list_ma = []
        self.my_data_list_lnk = []
        # id movie
        self.idV = tk.StringVar()
        # id actor
        self.idVa = tk.StringVar()

        # notebooks
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=0, column=0, columnspan=5, sticky='nsew')

        # create frames
        self.movie_frame = ttk.Frame(self.notebook)
        self.actor_frame = ttk.Frame(self.notebook)

        self.movie_frame.pack(fill='both', expand=True)
        self.actor_frame.pack(fill='both', expand=True)

        # add frames to notebook
        self.notebook.add(self.movie_frame, text='MOVIES', image=self.photo_m, compound=tk.LEFT)
        self.notebook.add(self.actor_frame, text='ACTORS', image=self.photo_a, compound=tk.LEFT)
        # switch_tab is called when the a tab is changed
        self.notebook.bind('<<NotebookTabChanged>>', self.switch_tab)

        self.add_movie_control(self.movie_frame)
        self.add_actor_control(self.actor_frame)

        self.frame_btn = tk.Frame(self.master)
        self.frame_btn.grid(row=1, column=0, sticky='nsew')
        for i in range(5):
            self.frame_btn.columnconfigure(i, weight=1)

        self.frame_btn.rowconfigure(0, weight=1)

        self.btnAdd = tk.Button(self.frame_btn, image=self.photo_add, borderwidth=0, padx=20, pady=10, command=self.add_entry)
        self.btnAdd.grid(row=1, column=0, padx=20, pady=10)

        self.btnUpdate = tk.Button(self.frame_btn, image=self.photo_update, borderwidth=0, padx=20, pady=10, command=self.update_entry)
        self.btnUpdate.grid(row=1, column=1, padx=20, pady=10)

        self.btnDelete = tk.Button(self.frame_btn, image=self.photo_delete, borderwidth=0, padx=20, pady=10, command=self.delete_entry)
        self.btnDelete.grid(row=1, column=2, padx=20, pady=10)

        self.btnClear = tk.Button(self.frame_btn, image=self.photo_clear, borderwidth=0, padx=18, pady=10, command=self.cancel)
        self.btnClear.grid(row=1, column=3, padx=20, pady=10)

        self.btnExit = tk.Button(self.frame_btn, image=self.photo_exit, borderwidth=0, padx=20, pady=10, command=self.quit)
        self.btnExit.grid(row=1, column=4, padx=20, pady=10)

        # load data for first page
        self.load_json_from_file(Tab_Typ.MOVIE)
        self.load_trv_with_json(Tab_Typ.MOVIE, self.trv)

        moja = self.generate_next_id(Tab_Typ.MOVIE)
        self.idV.set(moja)

    def add_movie_control(self, m_frame):
        self.frame_content = tk.Frame(m_frame)

        self.frame_content.grid(row=0, column=0, rowspan=5, columnspan=5)
        label_0 = tk.Label(self.frame_content, anchor="w", width=24, height=1, relief="ridge",
                           text="Id").grid(row=0, column=0, sticky=tk.W + tk.E)

        label_1 = tk.Label(self.frame_content, anchor="w", width=24, height=1,
                           relief="ridge", text="Title").grid(row=1, column=0, sticky=tk.W + tk.E)

        label_2 = tk.Label(self.frame_content, anchor="w", width=24, height=1,
                           relief="ridge", text="Director").grid(row=2, column=0, sticky=tk.W + tk.E)

        label_3 = tk.Label(self.frame_content, anchor="w", width=24, height=1,
                           relief="ridge", text="Length(min)").grid(row=3, column=0, sticky=tk.W + tk.E)

        label_4 = tk.Label(self.frame_content, anchor="w", width=24, height=1,
                           relief="ridge", text="Type").grid(row=4, column=0, sticky=tk.W + tk.E)

        label_5 = tk.Label(self.frame_content, anchor="w", width=24, height=1,
                           relief="ridge", text="Year of production").grid(row=5, column=0, sticky=tk.W + tk.E)

        moja = self.generate_next_id(Tab_Typ.MOVIE)
        self.idV.set(moja)
        self.ident = tk.Label(self.frame_content, anchor="w", height=1, textvariable=self.idV)
        self.ident.grid(row=0, column=1, sticky=tk.W)

        self.nzw = tk.Entry(self.frame_content, width=30, borderwidth=2, fg="black")
        self.nzw.grid(row=1, column=1, columnspan=4, sticky=tk.W)

        self.rez = tk.Entry(self.frame_content, width=30, borderwidth=2, fg="black")
        self.rez.grid(row=2, column=1, columnspan=4, sticky=tk.W)

        vcmd = (self.master.register(self.callback))
        self.dl = tk.Entry(self.frame_content, width=30, borderwidth=2, fg="black", validate='all',
                           validatecommand=(vcmd, '%P'))
        self.dl.grid(row=3, column=1, columnspan=4, sticky=tk.W)

        self.rdz = tk.Entry(self.frame_content, width=30, borderwidth=2, fg="black")
        self.rdz.grid(row=4, column=1, columnspan=4, sticky=tk.W)

        self.r = tk.Entry(self.frame_content, width=30, borderwidth=2, fg="black", validate='all',
                          validatecommand=(vcmd, '%P'))
        self.r.grid(row=5, column=1, columnspan=4, sticky=tk.W)

        self.frame_treeview = ttk.Frame(self.frame_content)
        self.frame_treeview.grid(row=6, column=0, columnspan=5)

        self.trv = ttk.Treeview(self.frame_treeview, columns=(1, 2, 3, 4, 5, 6), show="headings", selectmode=tk.BROWSE,
                                style="Custom2.Treeview")
        self.trv.grid(row=0, column=0, rowspan=2, columnspan=5)
        verscrlbar = ttk.Scrollbar(self.frame_treeview, orient="vertical", command=self.trv.yview)
        verscrlbar.grid(row=0, column=5, sticky=tk.NS)
        self.trv.configure(xscrollcommand=verscrlbar.set)

        self.trv.heading(1, text="Id", anchor="center")
        self.trv.heading(2, text="Title", anchor="center")
        self.trv.heading(3, text="Director", anchor="center")
        self.trv.heading(4, text="Length", anchor="center")
        self.trv.heading(5, text="Type", anchor="center")
        self.trv.heading(6, text="Year", anchor="center")

        self.trv.column("#1", anchor=tk.CENTER, width=80, stretch=True)
        self.trv.column("#2", anchor="w", width=180, stretch=False)
        self.trv.column("#3", anchor="w", width=180, stretch=False)
        self.trv.column("#4", anchor=tk.CENTER, width=180, stretch=False)
        self.trv.column("#5", anchor=tk.CENTER, width=180, stretch=False)
        self.trv.column("#6", anchor=tk.CENTER, width=80, stretch=False)

        # nieparzyste - niebieski kolor, parzyste - bialy
        self.trv.tag_configure('oddrow', background="white")
        self.trv.tag_configure('evenrow', background="lightblue")
        self.trv.bind("<ButtonRelease>", lambda event: self.MouseButtonUpCallBack(event, "movietree"))

    def add_actor_control(self, aframe):
        self.frame_contenta = tk.Frame(aframe)
        self.frame_contenta.grid(row=0, column=0, rowspan=5, columnspan=5)

        label_0 = tk.Label(self.frame_contenta, anchor="w", width=28, height=1,
                           relief="ridge", text="Id").grid(row=0, column=0, sticky=tk.W + tk.E)

        label_1 = tk.Label(self.frame_contenta, anchor="w", width=28, height=1,
                           relief="ridge", text="Name").grid(row=1, column=0, sticky=tk.W + tk.E)

        label_2 = tk.Label(self.frame_contenta, anchor="w", width=28, height=1,
                           relief="ridge", text="Surname").grid(row=2, column=0, sticky=tk.W + tk.E)

        label_3 = tk.Label(self.frame_contenta, anchor="w", width=28, height=1,
                           relief="ridge", text="Date of birth (YYYY/MM/DD)").grid(row=3, column=0, sticky=tk.W + tk.E)

        moja = self.generate_next_id(Tab_Typ.ACTOR)
        self.idVa.set(moja)
        self.identa = tk.Label(self.frame_contenta, anchor="w", height=1, textvariable=self.idVa)
        self.identa.grid(row=0, column=1, sticky=tk.W)

        self.nam = tk.Entry(self.frame_contenta, width=30, borderwidth=2, fg="black")
        self.nam.grid(row=1, column=1, columnspan=4, sticky=tk.W)

        self.surn = tk.Entry(self.frame_contenta, width=30, borderwidth=2, fg="black")
        self.surn.grid(row=2, column=1, columnspan=4, sticky=tk.W)

        self.dob = tk.Entry(self.frame_contenta, width=30, borderwidth=2, fg="black")
        self.dob.grid(row=3, column=1, columnspan=4, sticky=tk.W)

        self.frame_treeviewa = ttk.Frame(self.frame_contenta)
        self.frame_treeviewa.grid(row=6, column=0, columnspan=5)

        self.trva = ttk.Treeview(self.frame_treeviewa, columns=(1, 2, 3, 4), show="headings", height="3",
                                 selectmode=tk.BROWSE, style="Custom2.Treeview")
        self.trva.grid(row=0, column=0, rowspan=2, columnspan=4)
        verscrlbara = ttk.Scrollbar(self.frame_treeviewa, orient="vertical", command=self.trva.yview)
        verscrlbara.grid(row=0, column=5, sticky=tk.N + tk.S)
        self.trva.configure(xscrollcommand=verscrlbara.set)

        self.trva.heading(1, text="Id", anchor="center")
        self.trva.heading(2, text="Name", anchor="center")
        self.trva.heading(3, text="Surname", anchor="center")
        self.trva.heading(4, text="DOB", anchor="center")

        self.trva.column("#1", anchor="w", width=80, stretch=True)
        self.trva.column("#2", anchor="w", width=180, stretch=False)
        self.trva.column("#3", anchor="w", width=180, stretch=False)
        self.trva.column("#4", anchor="w", width=180, stretch=False)

        self.trva.tag_configure('oddrow', background="white")
        self.trva.tag_configure('evenrow', background="lightblue")
        self.trva.bind("<ButtonRelease>", lambda event: self.MouseButtonUpCallBack(event, "actortree"))

        self.frame_movies = tk.LabelFrame(self.frame_contenta, text="Movies", width=10, font=("bold", 14))
        self.frame_movies.grid(row=7, column=0, columnspan=5, sticky=tk.W)

        self.trvm = ttk.Treeview(self.frame_movies, columns=(1, 2, 3, 4), show="headings", height="3", selectmode=tk.BROWSE,
                                 style="Custom2.Treeview")
        self.trvm.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.frame_movies_add = tk.Frame(self.frame_movies)
        self.frame_movies_add.grid(row=0, column=4, padx=10, pady=10, sticky=tk.W)
        self.m_combo = ttk.Combobox(self.frame_movies_add, values=list(self.my_data_list_m))
        self.m_combo.grid(row=0, column=1, columnspan=2)
        self.Btn_ma = tk.Button(self.frame_movies_add, image=self.photo_add_a, borderwidth=0, padx=18, pady=10, command=self.add_link)
        self.Btn_ma.grid(row=0, column=3)
        self.Btn_md = tk.Button(self.frame_movies_add, image=self.photo_delete_a, borderwidth=0, padx=18, pady=10, command=self.delete_link)
        self.Btn_md.grid(row=1, column=0)
        self.Btn_ma["state"] = tk.DISABLED
        self.Btn_md["state"] = tk.DISABLED

        self.trvm.heading(1, text="Movie Name", anchor="center")
        self.trvm.heading(2, text="Director", anchor="center")
        self.trvm.heading(3, text="Actor_id", anchor="center")
        self.trvm.heading(4, text="Movie_id", anchor="center")

        self.trvm.column("#1", anchor="w", width=180, stretch=True)
        self.trvm.column("#2", anchor="w", width=180, stretch=False)
        # width=0 means that the column is "hidden"
        self.trvm.column("#3", anchor="w", width=0, stretch=False)
        self.trvm.column("#4", anchor="w", width=0, stretch=False)

    def check_if_link_exist(self, id_a, id_m):
        ret = False
        for lnk in self.my_data_list_lnk:
            if lnk["id_actor"] == id_a:
                if lnk["id_movie"] == id_m:
                    ret = True
                    break
        return ret

    def add_link(self):
        list = []
        # which film is selected
        ind = self.m_combo.current()
        if ind > -1:
            id_a = self.idVa.get()
            id_m = self.my_data_list_m[ind]["id"]
            # if the link exists show messagebox
            if self.check_if_link_exist(id_a,id_m) == True:
                messagebox.showinfo("showinfo", self.my_data_list_m[ind]["title"] + " has been already added for this actor!")
                return
            list.append(self.idVa.get())
            itm = self.my_data_list_m[ind]
            list.append(itm["id"])
            self.process_request("_INSERT_", list, Tab_Typ.LINK)
        return

    def delete_link(self):
        selected_item = self.trvm.focus()
        # details - holds data of selected row
        details = self.trvm.item(selected_item)
        # actor_id and movie_id are "hidden"
        actor_id = details.get("values")[2]
        movie_id = details.get("values")[3]
        self.delete_item_from_lnk(actor_id, movie_id)
        self.save_json_to_file(Tab_Typ.LINK)
        self.display_movies_for_actor()

    def delete_item_from_lnk(self, id_a, id_m):
        for lnk in self.my_data_list_lnk:
            if lnk["id_actor"] == str(id_a):
                if lnk["id_movie"] == str(id_m):
                    self.my_data_list_lnk.remove(lnk)

    # checking if entry is a number if yes return true, if not return false
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    # creating list that holds movie title and director(data that appear ina  combobox)
    def get_movies_from_list(self, list):
        lst = []
        for dic_itm in list:
            lst.append(dic_itm["title"] + "-" + dic_itm["director"])
        return lst

    def switch_tab(self, *args):
        # 0 - zakladka movies
        # 1 - zakladka actors
        ind = self.notebook.index(self.notebook.select())
        if ind == 1:
            # loading movies in actor tab to have a list of all current movies in combobox
            self.load_json_from_file(Tab_Typ.MOVIE)
            self.load_json_from_file(Tab_Typ.ACTOR)
            self.load_json_from_file(Tab_Typ.LINK)

            moja_a = self.generate_next_id(Tab_Typ.ACTOR)
            self.idVa.set(moja_a)
            # trva refers to actors
            self.load_trv_with_json(Tab_Typ.ACTOR, self.trva)
            self.m_combo.configure(values=self.get_movies_from_list(self.my_data_list_m))

    # command_type - add, delete, ...
    # list - list of parameters that will be used
    # type - actor/movie/link
    def process_request(self, command_type, list, type):
        if type == Tab_Typ.MOVIE:
            tree = self.trv
        elif type == Tab_Typ.ACTOR:
            tree = self.trva

        if command_type == "_UPDATE_":
            row = self.find_row_in_my_data_list(list[0], type)
            if type == Tab_Typ.MOVIE:
                if row >= 0:
                    dict = {"id": list[0], "title": list[1], "director": list[2],
                        "length": list[3], "type": list[4], "year": list[5]}
                    self.my_data_list_m[row] = dict
            elif type == Tab_Typ.ACTOR:
                if row >= 0:
                    dict = {"id": list[0], "name": list[1], "surname": list[2],
                            "dob": list[3]}
                    self.my_data_list_ma[row] = dict

        elif command_type == "_INSERT_":
            if type == Tab_Typ.MOVIE:
                dict = {"id": list[0], "title": list[1], "director": list[2],
                        "length": list[3], "type": list[4], "year": list[5]}
                self.my_data_list_m.append(dict)
            elif type == Tab_Typ.ACTOR:
                self.remove_all_data_from_tree(self.trvm)
                dict = {"id": list[0], "name": list[1], "surname": list[2],
                    "dob": list[3]}
                self.my_data_list_ma.append(dict)
            elif type == Tab_Typ.LINK:
                dict = {"id_actor": list[0], "id_movie": list[1]}
                self.my_data_list_lnk.append(dict)

        elif command_type == "_DELETE_":
            row = self.find_row_in_my_data_list(list[0], type)
            if row >= 0:
                if type == Tab_Typ.MOVIE:
                    id_mov = list[0]
                    for lnk in self.my_data_list_lnk:
                        if lnk["id_movie"] == str(id_mov):
                            self.my_data_list_lnk.remove(lnk)
                    self.save_json_to_file(Tab_Typ.LINK)
                    del self.my_data_list_m[row]
                elif type == Tab_Typ.ACTOR:
                    id_ac = list[0]
                    for lnk in self.my_data_list_lnk:
                        if lnk["id_actor"] == id_ac:
                            self.my_data_list_lnk.remove(lnk)
                    self.save_json_to_file(Tab_Typ.LINK)
                    self.remove_all_data_from_tree(self.trvm)
                    del self.my_data_list_ma[row]

        self.save_json_to_file(type)
        if type == Tab_Typ.ACTOR or type == Tab_Typ.MOVIE:
            self.load_trv_with_json(type, tree)
        elif type == Tab_Typ.LINK:
            self.display_movies_for_actor()
        # clear entry
        self.clear_all_fields()

    def add_entry(self):
        list = []
        ind = self.notebook.index(self.notebook.select())
        if ind == 0:
            list.append(self.idV.get())
            list.append(self.nzw.get())
            list.append(self.rez.get())
            list.append(self.dl.get())
            list.append(self.rdz.get())
            list.append(self.r.get())
            type = Tab_Typ.MOVIE
        elif ind == 1:
            list.append(self.idVa.get())
            list.append(self.nam.get())
            list.append(self.surn.get())
            list.append(self.dob.get())
            type = Tab_Typ.ACTOR

        self.process_request("_INSERT_", list, type)
        return

    def update_entry(self):
        list = []
        ind = self.notebook.index(self.notebook.select())

        if ind == 0:
            list.append(self.idV.get())
            list.append(self.nzw.get())
            list.append(self.rez.get())
            list.append(self.dl.get())
            list.append(self.rdz.get())
            list.append(self.r.get())
            type = Tab_Typ.MOVIE
        elif ind == 1:
            list.append(self.idVa.get())
            list.append(self.nam.get())
            list.append(self.surn.get())
            list.append(self.dob.get())
            type = Tab_Typ.ACTOR
        self.process_request("_UPDATE_", list, type)
        return

    def delete_entry(self):
        list = []
        ind = self.notebook.index(self.notebook.select())
        if ind == 0:
            type = Tab_Typ.MOVIE
            list.append(self.idV.get())
        elif ind == 1:
            type = Tab_Typ.ACTOR
            list.append(self.idVa.get())

        self.process_request("_DELETE_", list, type)
        return

    # removing data from entry
    def clear_all_fields(self):
        ind = self.notebook.index(self.notebook.select())
        if ind == 0:
            self.nzw.delete(0, tk.END)
            self.rez.delete(0, tk.END)
            self.dl.delete(0, tk.END)
            self.rdz.delete(0, tk.END)
            self.r.delete(0, tk.END)
            self.nzw.focus_set()
            self.idV.set(self.generate_next_id(Tab_Typ.MOVIE))
        elif ind == 1:
            self.nam.delete(0, tk.END)
            self.surn.delete(0, tk.END)
            self.dob.delete(0, tk.END)
            self.nam.focus_set()
            self.idVa.set(self.generate_next_id(Tab_Typ.ACTOR))


    # cancel -> clear button
    def cancel(self):
        self.clear_all_fields()
        self.change_enabled_state('New')

    def quit(self):
        self.master.quit()
        return

    def generate_next_id(self, typ):
        ind = -1
        if typ == Tab_Typ.MOVIE:
            list = self.my_data_list_m
        elif typ == Tab_Typ.ACTOR:
            list = self.my_data_list_ma
        for rec in list:
            if int(rec["id"]) > ind:
                ind = int(rec["id"])
        ind = ind + 1
        ret = str(ind)
        return ret

    def load_json_from_file(self, which):
        if which == Tab_Typ.MOVIE:
            file = self.FILEMOVIE
        elif which == Tab_Typ.ACTOR:
            file = self.FILEACTOR
        elif which == Tab_Typ.LINK:
            file = self.FILELINK
        try:
            # The r throws an error if the file does not exist or opens an existing file
            file_handler = open(file, 'r')
        except IOError:
            file_handler = open(file, 'w+')

        try:
            if which == Tab_Typ.MOVIE:
                self.my_data_list_m = json.load(file_handler)
            elif which == Tab_Typ.ACTOR:
                self.my_data_list_ma = json.load(file_handler)
            elif which == Tab_Typ.LINK:
                self.my_data_list_lnk = json.load(file_handler)
        except:
            print('Database is empty or corrupted.')
            return
        file_handler.close

    def save_json_to_file(self, which):
        if which == Tab_Typ.MOVIE:
            file = self.FILEMOVIE
            list = self.my_data_list_m
        elif which == Tab_Typ.ACTOR:
            file = self.FILEACTOR
            list = self.my_data_list_ma
        elif which == Tab_Typ.LINK:
            file = self.FILELINK
            list = self.my_data_list_lnk
        try:
            file_handler = open(file, 'w')
        except IOError:
            file_handler = open(file, 'w+')
        json.dump(list, file_handler, indent=4)

        file_handler.close

    def find_row_in_my_data_list(self, find_id, which):
        row = 0
        found = False

        if which == Tab_Typ.MOVIE:
            list = self.my_data_list_m
        elif which == Tab_Typ.ACTOR:
            list = self.my_data_list_ma

        for rec in list:
            if rec["id"] == find_id:
                found = True
                break
            row += 1

        if (found == True):
            return (row)

        return (-1)

    def remove_all_data_from_tree(self, tree):
        for item in tree.get_children():
            tree.delete(item)

    def load_edit_field_with_row_data(self, _tuple, tab):
        if len(_tuple) == 0:
            return
        if tab == Tab_Typ.MOVIE:
            self.idV.set(_tuple[0])
            self.nzw.delete(0, tk.END)
            self.nzw.insert(0, _tuple[1])
            self.rez.delete(0, tk.END)
            self.rez.insert(0, _tuple[2])
            self.dl.delete(0, tk.END)
            self.dl.insert(0, _tuple[3])
            self.rdz.delete(0, tk.END)
            self.rdz.insert(0, _tuple[4])
            self.r.delete(0, tk.END)
            self.r.insert(0, _tuple[5])
        elif tab == Tab_Typ.ACTOR:
            self.idVa.set(_tuple[0])
            self.nam.delete(0, tk.END)
            self.nam.insert(0, _tuple[1])
            self.surn.delete(0, tk.END)
            self.surn.insert(0, _tuple[2])
            self.dob.delete(0, tk.END)
            self.dob.insert(0, _tuple[3])
        return

    def MouseButtonUpCallBack(self, event, name):
        if name == "movietree":
            tree = self.trv
            tab = Tab_Typ.MOVIE
        elif name == "actortree":
            tree = self.trva
            tab = Tab_Typ.ACTOR

        # data of selected row
        cursel = tree.selection()
        if cursel:
            currentRowIndex = tree.selection()[0]
            # lastTuple holds values for actor/movie with currentRowIndex
            lastTuple = (tree.item(currentRowIndex, 'values'))
            self.load_edit_field_with_row_data(lastTuple, tab)
            # change buttons status
            self.change_enabled_state('Edit')
            # if actortree -> display data that refers to connection between actors and movies
            if name == "actortree":
                self.display_movies_for_actor()

    def display_movies_for_actor(self):
        # list containing movie ids for actor with idVa
        lst = self.get_dict_for_actor(self.idVa.get())
        self.load_trv_for_actor(self.get_movies_for_actor(lst), self.idVa.get())

    def get_movies_for_actor(self, lst):
        # list containing all data about movies from lst
        m_list = []
        # searching for movies from list lst
        for dic in self.my_data_list_m:
            if dic["id"] in lst:
                m_list.append(dic)
        return m_list


    def get_dict_for_actor(self, id):
        list = []
        for d in self.my_data_list_lnk:
            if d["id_actor"] == id:
                list.append(d["id_movie"])
        return list



    def load_trv_with_json(self, which, tree):
        self.remove_all_data_from_tree(tree)

        count = 0  # row

        if which == Tab_Typ.MOVIE:
            for key in self.my_data_list_m:
                id = key["id"]
                title = key["title"]
                director = key["director"]
                length = key["length"]
                type_m = key["type"]
                year = key["year"]

                if count % 2 == 0:
                    self.trv.insert('', index='end', iid=count, text="",
                                    values=(id, title, director, length, type_m, year),
                                    tags=('evenrow',))
                else:
                    self.trv.insert('', index='end', iid=count, text="",
                                    values=(id, title, director, length, type_m, year),
                                    tags=('oddrow',))
                count += 1
        elif which == Tab_Typ.ACTOR:
            for key in self.my_data_list_ma:
                id = key["id"]
                name = key["name"]
                surname = key["surname"]
                dob = key["dob"]

                if count % 2 == 0:
                    self.trva.insert('', index='end', iid=count, text="", values=(id, name, surname, dob),
                                     tags=('evenrow',))
                else:
                    self.trva.insert('', index='end', iid=count, text="", values=(id, name, surname, dob),
                                     tags=('oddrow',))
                count += 1

    # filling the Movies table in the Actors tab
    def load_trv_for_actor(self, lst, id_a):
        self.remove_all_data_from_tree(self.trvm)
        count = 0  # row
        for key in lst:
            title = key["title"]
            director = key["director"]
            id_m = key["id"]
            if count % 2 == 0:
                self.trvm.insert('', index='end', iid=count, text="",
                                values=(title, director, id_a, id_m),
                                tags=('evenrow',))
            else:
                self.trvm.insert('', index='end', iid=count, text="",
                                values=(title, director, id_a, id_m),
                                tags=('oddrow',))
            count += 1


    def change_enabled_state(self, state):
        if state == 'Edit':
            self.btnUpdate["state"] = tk.NORMAL
            self.btnDelete["state"] = tk.NORMAL
            self.Btn_ma["state"] = tk.NORMAL
            self.Btn_md["state"] = tk.NORMAL
            self.btnAdd["state"] = tk.DISABLED
        elif state == 'Cancel':
            self.btnUpdate['state'] = tk.DISABLED
            self.btnDelete['state'] = tk.DISABLED
            self.btnAdd['state'] = tk.DISABLED
            self.Btn_ma["state"] = tk.DISABLED
            self.Btn_md["state"] = tk.DISABLED
        else:
            self.btnUpdate['state'] = tk.DISABLED
            self.btnDelete['state'] = tk.DISABLED
            self.btnAdd['state'] = tk.NORMAL
            self.Btn_ma["state"] = tk.DISABLED
            self.Btn_md["state"] = tk.DISABLED


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w = screen_width * 0.5
h = screen_height * 0.5
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)
photo = tk.PhotoImage(file='movie_32.png')
root.title("Movies Project")
root.wm_iconphoto(False, photo)
# color of the line you click on
root.config(bg="gray17")
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
window = Window(root)
style = ttk.Style()

style.configure("Custom2.Treeview", background="Greed", foreground="Purple", fieldbackground="pink")
style.map('Custom2.Treeview', background=[('selected', '#3c3737')], foreground=[('selected', 'white')])

root.mainloop()
