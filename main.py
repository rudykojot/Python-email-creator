import os
import tkinter as tk
from tkinter import scrolledtext,messagebox
from face_settings import face_setup


class CustomInputDialog(tk.Toplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.title("Input")
        self.geometry("400x200")

        self.configure(bg="#7ABAFF")
        self.prompt_label = tk.Label(self, text=prompt,bg="#7ABAFF", font=("Open Sans", 18, "bold"), fg="White")
        self.prompt_label.pack()
        self.text_input = scrolledtext.ScrolledText(self, width=40, height=5,font=("Open Sans", 10))
        self.text_input.pack()
        self.ok_button = tk.Button(self, text="Enter", command=self.on_ok,
                                   pady=5, bg="#FFD343", font=("Open Sans", 18), fg="white")
        self.ok_button.pack()

    def on_ok(self):

        self.result = self.text_input.get("1.0", tk.END).strip()
        self.destroy()


class HTMLGeneratorApp(tk.Tk):

    script_dir = os.path.dirname(os.path.realpath(__file__))

    output_folder = os.path.join(script_dir, "output")
    image_path = os.path.join(script_dir, "images", "pythonlogo.png","icon.ico")
    template_path = os.path.join(script_dir, "templates", "email_template.html")

    def __init__(self):
        super().__init__()
        self.title("Python Email Creator")
        self.iconbitmap(r"images\icon.ico")

        self.output_folder = "output"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        self.html_content = ""

        self.app_logo = tk.PhotoImage(
            file=r"images\pythonlogo.png")
        self.resized_logo = self.app_logo.subsample(5, 5)

        self.configure(background="#7ABAFF")

        self.table_data = {
            "table_1": {
                "html":
                    """
                       <tr>
                        <td class="" valign="top"
                        align="left">
                        
                        <table role="presentation"
                        style="border-bottom: 1px solid #AEAEAE; min-width: 100%; "
                        class="slot-styling"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 3px; padding-bottom: 3px; "
                        class="slot-styling camarker-inner">
                        
                        <table
                        role="presentation"
                        class="stylingblock-content-wrapper"
                        style="min-width: 100%; "
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td class="stylingblock-content-margin-cell"
                        style="padding: 4px 0px; ">
                        
                        <table
                        role="presentation"
                        style="background-color: #676767; min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding: 3px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <font
                        color="#ffffff">
                        
                        <span
                        style="font-size: 20px;"><b>
                        puttedtext
                        </b></span>
                        
                        </font>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                    """,
                "text": "puttedtext",
            },
            "table_2": {
                "html":
                    """
                        <table
                        role="presentation"
                        style="min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 10px; padding-bottom: 10px; padding-right: 10px; padding-left: 10px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <table
                        style="width: 100%;"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td>
                        
                        <table
                        style="width: 100%;"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td class="responsive-td"
                        style="width: 100%;"
                        valign="top">
                        
                        <table
                        role="presentation"
                        style="min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 10px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <div
                        style="text-align: justify;">
                        puttedtext
                        </div>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                    """,
                "text": "puttedtext",

            },
            "table_3": {
                "html":
                    """
                        <tr>
                        <td class="" valign="top"
                        align="left">
                        
                        <table role="presentation"
                        style="border-bottom: 1px solid #AEAEAE; min-width: 100%; "
                        class="slot-styling"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 3px; padding-bottom: 3px; "
                        class="slot-styling camarker-inner">
                        
                        <table
                        role="presentation"
                        class="stylingblock-content-wrapper"
                        style="min-width: 100%; "
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td class="stylingblock-content-margin-cell"
                        style="padding: 4px 0px; ">
                        
                        <table
                        role="presentation"
                        style="background-color: #7ABAFF; min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding: 7px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <span
                        style="color:#ffffff;"><span
                        style="background-color:#7ABAFF;">
                        <b> puttedtext </b>
                        </span></span>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                    """,
                "text": "puttedtext",

            },
            "table_4": {
                "html":
                    """
                        <table role="presentation"
                        style="background-color: #F4F4F4; min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 10px; padding-bottom: 10px; padding-right: 10px; padding-left: 15px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        puttedtext
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                    """,
                "text": "puttedtext",
            },
            "table_5": {
                "html":
                    """
                        <table
                        role="presentation"
                        style="background-color: #F4F4F4; min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 3px; padding-bottom: 3px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <table
                        role="presentation"
                        style="width: 100%;"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td>
                        
                        <table
                        role="presentation"
                        style="width: 100%;"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td class="responsive-td"
                        style="width: 50%; padding-right: 3px; padding-left: 20px;"
                        valign="top">
                        
                        <table
                        role="presentation"
                        style="min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <p
                        dir="ltr">
                        
                        <b>
                        text1
                        </b>
                        
                        </p>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        <td class="responsive-td"
                        style="width: 50%; padding-left: 3px;"
                        valign="top">
                        
                        <table
                        role="presentation"
                        style="min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <p data-stringify-type="quote"
                        type="cite">
                        text2
                        <br>
                        
                        <br>
                        
                        <b><span
                        style="color:#7ABAFF;"></span><br>
                        
                        <span
                        style="color:#7ABAFF;"></span></b>
                        
                        </p>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
    
                    """,
                "text": "text1",
                "text2": "text2"

            },
            "label": {
                "html":
                    """
                        <table
                        role="presentation"
                        class="stylingblock-content-wrapper"
                        style="min-width: 100%; "
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td class="stylingblock-content-margin-cell"
                        style="padding: 4px 0px 0px; ">
                        
                        <table
                        role="presentation"
                        style="background-color: #666666; min-width: 100%; "
                        class="stylingblock-content-wrapper"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding: 0px; "
                        class="stylingblock-content-wrapper camarker-inner">
                        
                        <!--[if mso]><table style="width:560px" cellpadding="0" cellspacing="0"><tr><td style="width:180px" valign="top"><![endif]-->
                        
                        <table
                        class="es-left"
                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left"
                        cellspacing="0"
                        cellpadding="0"
                        align="left">
                        
                        <tbody>
                        
                        <tr
                        style="border-collapse:collapse">
                        
                        <td class="es-m-p0r es-m-p20b"
                        style="padding:15;Margin:0;width:180px"
                        valign="top"
                        align="center">
                        
                        <table
                        role="presentation"
                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr
                        style="border-collapse:collapse">
                        
                        <td style="padding:0;Margin:0;font-size:0px"
                        class=""
                        align="left">
                        
                        <img alt=""
                        class="adapt-img"
                        src= "https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png"
                        style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"
                        shrinktofit="true"
                        width="120">
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        <!--[if mso]></td><td style="width:20px"></td><td style="width:360px" valign="top"><![endif]-->
                        
                        <table
                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"
                        cellspacing="0"
                        cellpadding="0"
                        align="right">
                        
                        <tbody>
                        
                        <tr
                        style="border-collapse:collapse">
                        
                        <td style="padding:0;Margin:0;width:360px"
                        align="left">
                        
                        <table
                        role="presentation"
                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr
                        style="border-collapse:collapse">
                        
                        <td style="padding:0;Margin:0"
                        class=""
                        align="left">
                        
                        <p
                        style="Margin:15;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;line-height:18px;color:#CCCCCC">
                        
                        <a href="testemail@email.com"
                        style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'open sans', 'helvetica neue', helvetica, arial, sans-serif;font-size:12px;text-decoration:none;color:#CCCCCC;line-height:18px"
                        target="_blank">testemail@testemailr.com</a><br>
                        
                        <br> 
                        Test company name;  Test address 22; 8999 Test location<br><br>
                        Test location (country),&nbsp;Test 124242 B<br>
                        Managing Directors:
                        John Doe,&nbsp;Joanna Doe,&nbsp;John Wick<br><br>
                        We respect your right to privacy
                        - click <b><a href="https://www.testadress.com"
                        style="text-decoration:none;color:#7ABAFF;">here</a></b> to view our policy
                        
                        </p>
                        
                        <p>
                        
                        </p>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        <tr>
                        
                        <td role="contentinfo"
                        aria-label="footer" class=""
                        valign="top" align="left">
                        
                        <table role="presentation"
                        style="min-width: 100%; "
                        class="slot-styling"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0">
                        
                        <tbody>
                        
                        <tr>
                        
                        <td style="padding-top: 20px; "
                        class="slot-styling camarker-inner">
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        </td>
                        
                        </tr>
                        
                        <tr>
                        
                        <td valign="top">
                        
                        </td>
                        
                        </tr>
                        
                        </tbody>
                        
                        </table>
                        
                        <!-- start:processor:append -->
                        
                        <!-- start:processor:body:append -->
                        
                        </div><!-- end:processor:body:append -->
                        
                        <!-- end:processor:append -->
                        
                        </div>
                    
                    """,
            },

        }

        self.face_setup()

        self.app_logo_label = tk.Label(self, image=self.resized_logo,bg="#7ABAFF")
        self.app_logo_label.grid(row=0, column=0, columnspan=2, padx=150, pady=20, sticky="W")

        self.app_name_label = tk.Label(self, text="Python Email Creator", font=("Open Sans", 30, "bold"), fg="white", bg="#7ABAFF")
        self.app_name_label.grid(row=0, column=1, columnspan=2, padx=100, pady=5,sticky="W")

        self.table_name_label = tk.Label(self, text="Table Name:",font=("Open Sans", 14, "bold"), fg="white", bg="#7ABAFF")
        self.table_name_label.grid(row=1, column=0, padx=5, pady=5)

        self.table_name_entry = tk.Entry(self, font=("Open Sans", 10))
        self.table_name_entry.grid(row=2, column=0, padx=5, pady=5, sticky="N")

        self.text_label = tk.Label(self, text="Text:",font=("Open Sans", 14, "bold"), fg="white", bg="#7ABAFF")
        self.text_label.grid(row=3, column=0, padx=5, pady=5, sticky="S")

        self.text_entry = tk.Text(self, height=15, width=20,font=("Open Sans", 10))
        self.text_entry.grid(row=4,column=0, padx=15, pady=5, sticky="N", )

        self.generate_button = tk.Button(self, text="Generate HTML", command=self.generate_html,
                                         font=("Open Sans", 14, "bold"),fg="white", bg="#FFD343")
        self.generate_button.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=30,font=("Open Sans", 10))
        self.text_area.grid(row=2, column=1, rowspan=50, columnspan=1, padx=15, pady=15)

        self.guide_label = tk.Label(self, text="Guide: \n\n"
                                               "table_1 = Dark Gray bar \n\n"
                                               "table_2 = White text area \n\n"
                                               "table_3 = Blue bar \n\n"
                                               "table_4 = Light Gray text area \n\n"
                                               "table_5 = Triggers 2 column Tab input \n\n"
                                               "label = Label with company contact info \n\n"
                                               "finish = creates html file",
                                    font=("Open Sans", 12, "bold"), fg="white", bg="#7ABAFF",justify="left")
        self.guide_label.grid(row=4, column=2, padx=5, pady=15)

    def face_setup(self):
        self.html_content = face_setup()

    def generate_html(self):
        table_name = self.table_name_entry.get().strip()
        text_input = self.text_entry.get("1.0", tk.END).strip()

        if table_name.lower() == "finish":
            self.create_html_file()
            messagebox.showinfo("SUCCESS", "email template created!")
            return

        if table_name in self.table_data:
            if table_name == "table_5":
                text_input_dialog = CustomInputDialog(self, "Enter text for Subject")
                self.wait_window(text_input_dialog)
                text1_input = text_input_dialog.result
                text_input_dialog = CustomInputDialog(self, "Enter text for Content")
                self.wait_window(text_input_dialog)
                text2_input = text_input_dialog.result
                html_content = self.table_data[table_name]["html"].replace("text1", text1_input).replace("text2", text2_input)
            else:
                html_content = self.table_data[table_name]["html"].replace("puttedtext", text_input)

            self.html_content += html_content + "\n"
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.html_content)
            self.text_entry.delete("1.0", tk.END)
        else:
            messagebox.showinfo("Invalid Table Name", "The table name you entered is invalid. Please try again.")

    def create_html_file(self):
        file_path = os.path.join(self.output_folder, "email_template.html")
        with open(file_path, "w") as html_file:
            html_file.write(self.html_content)

        self.text_area.insert(tk.END, f"\nHTML file generated at {file_path}.\n")

    def get_text(self):

        text_content = self.text_entry.get("1.0", tk.END)
        return text_content


if __name__ == "__main__":
    app = HTMLGeneratorApp()
    app.mainloop()
