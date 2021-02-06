import tkinter as tk
from tkinter import messagebox
import actionsequence as ac


class as_window():

    def __init__(self, root_root):
        self.root_var = tk.Toplevel(root_root)
        self.root_var.iconbitmap(r'icon.ico')  # Dit werkt niet
        self.root_var.geometry("600x500")
        self.root_var.lift()
        # Create a consistent header everywhere
        self.header_frame = tk.Frame(self.root_var)
        self.header_frame.grid()

        header = tk.Label(self.header_frame,
                          text="TOPdesk API kit", font="impact")
        header.grid()

        self.frame = tk.Frame(self.root_var)
        self.frame.grid()

        self.root_var.title("ACtion Sequence builder")

        # Require actionsequence information
        self.acts_frame = tk.Frame(self.root_var)
        self.acts_frame.grid()

        self.ac_name = form_Entry(master=self.acts_frame, name="as_name", label="Name")
        self.ac_desc = form_Entry(master=self.acts_frame, name="as_desc", label="Description")
        self.ac_name = form_Entry(master=self.acts_frame, name="as_name", label="Structurename")

        # Create the Auth Frame
        self.auth_frame = tk.Frame(self.root_var)
        self.auth_frame.grid()

        # Create the TOPdesk username and password form
        self.v_usr = form_Entry(master=self.auth_frame, name="topdesk_user", label="Enter TOPdesk username")
        self.v_pw = form_Entry(master=self.auth_frame, name="app_pw", label="Enter Application password")
        self.v_url = form_Entry(master=self.auth_frame, name="topdesk_url", label="Enter TOPdesk URL")

        # Create the Auth Frame
        self.inc_frame = tk.Frame(self.root_var)
        self.inc_frame.grid()

        # Create the TOPdesk username and password form
        self.p_url = form_Entry(master=self.inc_frame, name="status", label="Enter status (firstLine)")
        self.p_caller = form_Entry(master=self.inc_frame, name="caller", label="Enter TOPdesk URL")

        self.button = tk.Button(self.auth_frame,
                            text="Create",
                            command=lambda: self.create_stuff())
        self.button.grid()

    def create_stuff(self):
        self.h_type = ac.nvpair(name="Content-Type", value="application/json")
        self.h_auth = ac.nvpair()
        self.h_auth.is_auth(user=self.v_usr.var, pw=self.v_pw.var)

        # step1.add_headers(h_type, h_auth)
        # step1.add_parameters(p_status, p_caller)
        # incidentcreator.add_steps(step1.build())
        # incidentcreator.add_variables(td_usr, td_pw, td_url)
        # print(json.dumps(incidentcreator.build(), indent=2))


class form_Entry:
    row_num = 0
    def __init__(self, master, name, label):
        self.use = tk.BooleanVar()
        self.use.set(True)

        self.label = tk.Label(master, text=label)
        self.entry = tk.Entry(master)
        self.check = tk.Checkbutton(master, var=self.use,
                                    onvalue=True, offvalue=False)

        self.label.grid(in_=master, row=form_Entry.row_num, column=0, pady=1)
        self.entry.grid(in_=master, row=form_Entry.row_num, column=1, pady=2)
        self.check.grid(in_=master, row=form_Entry.row_num, column=2, pady=1)

        form_Entry.row_num += 1

        self.name = name


    def compile(self):
        self.var = ac.nvpair(name=self.name, value=self.entry.get())


'''
incidentcreator = actionsequence(formatversion="2.6", exportdate=1568803440466,
                                 name="Create an incident (Registered Caller)",
                                 description="Amazing story",
                                 structurename="incident1")

td_usr = nvpair(name="topdesk_user",
                value="Enter the name of your API Operator account")
td_pw = nvpair(name="topdesk_applicationpassword",
               value="Enter the application password")
td_url = nvpair(name="topdesk_url",
                value="Enter your TOPdesk URL here")

step1 = step(name="step1", method="POST",
             url="${_variables.topdesk_url?no_esc}/tas/api/incidents",
             escape=True, condition="ONLY_WHEN_PREVIOUS_SUCCEEDED")

h_type = nvpair(name="Content-Type", value="application/json")
h_auth = nvpair()
h_auth.is_auth(user=td_usr, pw=td_pw)

p_status = parameter(name="status", value="firstLine")
p_caller = parameter(name="callerLookup")
p_caller.nest(name="email", value="${aanmelderemail}")

step1.add_headers(h_type, h_auth)
step1.add_parameters(p_status, p_caller)
incidentcreator.add_steps(step1.build())
incidentcreator.add_variables(td_usr, td_pw, td_url)
print(json.dumps(incidentcreator.build(), indent=2))
'''


class tophelp_window:
    '''
    Creates the TOPhelp screen and URL changer functionality. Requires a direct
     definition of the root/master window.
    '''

    def __init__(self, root_var):
        self.root_var = root_var
        self.root_var = root_var
        self.root_var.iconbitmap(r'icon.ico')  # Dit werkt niet
        self.root_var.geometry("150x150")
        self.root_var.lift()
        # Create a consistent header everywhere
        self.header_frame = tk.Frame(root_var)
        self.header_frame.pack()

        header = tk.Label(self.header_frame,
                          text="Link changer", font="impact")
        header.pack()

        self.frame = tk.Frame(root_var)
        self.frame.pack()

        self.root_var.title("TOPhelp link changer")

        changer = tk.Button(self.root_var,
                            text="Click to change url",
                            command=self._urlchanger)
        changer_explanation = tk.Message(self.root_var,
                                         text="Reads last clipboard entry and if TOPhelp URL, changes to MyTOPdesk")

        changer.pack()
        changer_explanation.pack()

    def _urlchanger(self):
        '''Change TOPhelp URL to My TOPdesk URL'''
        # First get the clipboard content
        # Gets a TOPhelp URL, such as https://tophelp.topdesk.com/tas/public/ssp/content/detail/knowledgeitem?unid=513caaea948e4b8a9e567c9ebbce60b4
        clipboard = self.root_var.clipboard_get()

        # check for it being a KI hotlink
        if "https://tophelp.topdesk.com/" in clipboard and len(clipboard) < 150:
            mytopdeskurl = clipboard.replace("https://tophelp.topdesk.com/", "https://my.topdesk.com/")
            self.root_var.clipboard_clear()
            self.root_var.clipboard_append(mytopdeskurl)
        else:
            messagebox.showerror(title="Not a (valid) TOPhelp URL", message="To make this work, the URL must at least contain https://tophelp.topdesk.com/ and be less than 150 chars long. Please try again.")
            self.root_var.lift()
