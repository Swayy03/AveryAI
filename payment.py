from Sam_Investments1 import *
from postgresDatabase import MyDatabase
from sms import cur_obj

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Payment_Input_Dialogue:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("640x480")
        self.root.title("Payment Options")
        self.root.resizable(False, False)
        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.pack(fill="both", expand=True)

        #functions
        def startup():
            self.conn_obj = psycopg2.connect(user=MyDatabase.username, password=MyDatabase.pwd,
                                             host=MyDatabase.hostname,
                                             database='SamInvestments')
            self.cur_object = self.conn_obj.cursor()
            try:
                # Execute the SQL query
                self.cur_object.execute(
                    'CREATE TABLE IF NOT EXISTS tenantinfo(tenant_id SERIAL PRIMARY KEY, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255), house_no VARCHAR(5));')
                self.cur_object.execute(
                    'CREATE TABLE IF NOT EXISTS payments(pay_id SERIAL PRIMARY KEY, pay_reason VARCHAR(455) NOT NULL, pay_amount INTEGER, pay_date TIMESTAMP);')
                self.conn_obj.commit()
                print("Table created successfully or already exists.")

            except Exception as e:
                print(f"Error: {e}")
                self.conn_obj.rollback()  # Rollback in case of error

            finally:
                # Close the cursor and connection to clean up
                self.conn_obj.close()
                self.cur_object.close()
                pass


        def pay_button_clicked():
            print(self.pay_reason_entry.get())
            print(self.pay_amount_entry.get())
            startup()
            try:
                conn_obj = psycopg2.connect(user=MyDatabase.username, password=MyDatabase.pwd, host=MyDatabase.hostname,
                                            database="SamInvestments")
                cur_obj = conn_obj.cursor()
                cur_obj.execute(f"INSERT INTO payments(pay_reason, pay_amount) VALUES('{self.pay_reason_entry.get()}',{self.pay_amount_entry.get()})")
                conn_obj.commit()
                conn_obj.close()
            except (Exception, psycopg2.DatabaseError) as err:
                print(err)

            self.root.quit()
            self.root.destroy()
        def pay_option_selected(event):
            print("Worked")

        conn_obj2 = psycopg2.connect(user=MyDatabase.username, password=MyDatabase.pwd,
                                         host=MyDatabase.hostname,
                                         database='SamInvestments')
        cur_object2 = conn_obj2.cursor()
        try:
            # Execute the SQL query
            cur_object2.execute(
                'CREATE TABLE IF NOT EXISTS tenantinfo(tenant_id SERIAL PRIMARY KEY, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255), house_no VARCHAR(5));')
            cur_object2.execute(
                'CREATE TABLE IF NOT EXISTS payments(pay_id SERIAL PRIMARY KEY, pay_reason VARCHAR(455) NOT NULL, pay_amount INTEGER, pay_date TIMESTAMP);')
            conn_obj2.commit()
            print("Table created successfully or already exists.")

        except Exception as e:
            print(f"Error: {e}")
            conn_obj2.rollback()  # Rollback in case of error

        finally:
            # Close the cursor and connection to clean up
            pass
            #self.conn_obj2.close()
            #self.cur_object2.close()

        self.pay_label = ctk.CTkLabel(self.mainframe, text="Payment", font=('Roboto',20))
        self.pay_label.pack(padx=10, pady=10)

        self.pay_reason_entry = ctk.CTkEntry(self.mainframe, placeholder_text="Enter reason for payment", height=30, width=300)
        self.pay_reason_entry.pack(padx=10, pady=10)

        self.pay_amount_entry = ctk.CTkEntry(self.mainframe, placeholder_text="Enter Amount", height=30,width=300)
        self.pay_amount_entry.pack(padx=10, pady=10)

        self.select_pay_option = ctk.CTkComboBox(self.mainframe, values=['Send Money', 'Buy Goods and services','Paybill', 'Pochi la Biashara'])
        self.select_pay_option.pack(padx=10, pady=10)
        self.select_pay_option.bind("<<ComboboxSelected>>", pay_option_selected)

        self.pay_number = ctk.CTkEntry(self.mainframe, placeholder_text="Enter payment number", height=30, width=300)
        self.pay_number.pack(padx=10, pady=10)

        self.pay_button = ctk.CTkButton(self.mainframe, text="Pay",command=pay_button_clicked)
        self.pay_button.pack(padx=10, pady=10)

        self.root.mainloop()

