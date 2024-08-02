#========================== App builder : Farzad Kermani ================================
#***************** IMPORTS ************** 
import tkinter as tk

#***************** CLASS FOR CALCULATOR ***********
#***************** از کلاس تی کی ارث بری میکند ************
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('320x480')
        self.resizable(0,0)
        self.result=tk.Entry(self,font=('Arial',36),bg='orange')
        self.result.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipadx=10,ipady=5,sticky=tk.W+tk.E)
        self.result.config(justify=tk.LEFT)
        self.grid_columnconfigure(0,weight=1)
        self.add_menus()

        button_frame=tk.Frame(self)
        button_frame.grid(row=1,column=0,columnspan=4,padx=10,pady=10)
#****************ساختن دکمه ها ****************************        
        self.Create_button('CE',button_frame,0,0,self.Clear)
        self.Create_button('C',button_frame,0,1,self.Clear)
        self.Create_button('<--',button_frame,0,2,self.backspace)
        self.Create_button('/',button_frame,0,3, lambda:self.add_operation('/'))
        self.Create_button('7',button_frame,1,0, lambda:self.add_number(7))
        self.Create_button('8',button_frame,1,1, lambda:self.add_number(8))
        self.Create_button('9',button_frame,1,2, lambda:self.add_number(9))
        self.Create_button('*',button_frame,1,3, lambda:self.add_operation('*'))
        self.Create_button('4',button_frame,2,0, lambda:self.add_number(4))
        self.Create_button('5',button_frame,2,1, lambda:self.add_number(5))
        self.Create_button('6',button_frame,2,2, lambda:self.add_number(6))
        self.Create_button('-',button_frame,2,3, lambda:self.add_operation('-'))
        self.Create_button('1',button_frame,3,0, lambda:self.add_number(1))
        self.Create_button('2',button_frame,3,1, lambda:self.add_number(2))
        self.Create_button('3',button_frame,3,2, lambda:self.add_number(3))
        self.Create_button('+',button_frame,3,3, lambda:self.add_operation('+'))
        self.Create_button('+/-',button_frame,4,0, lambda:self.add_number('-'))
        self.Create_button('0',button_frame,4,1, lambda:self.add_number(0))
        self.Create_button('.',button_frame,4,2, lambda:self.add_number('.'))
        self.Create_button('=',button_frame,4,3,self.Calculate)
#********************* تابع برای ساختن دکمه ****************
    def Create_button(self,text,frame,row,column,command,bg='silver'):
        button=tk.Button(frame,text=text,command=command,font=('Arial',18),width=3,height=1)
        button.config(bg=bg)
        button.grid(row=row,column=column,padx=10,pady=10)
#*********************** تابع برای دکمه های اعداد *********
    def add_number(self,number):
        current=self.result.get()
        current+=str(number)
        self.result.delete(0,tk.END)
        self.result.insert(0,current)
#*********************** تابع برای دکمه های عملگرهای محاسباتی ********
    def add_operation(self,operator):
        current=self.result.get()
        current+=operator
        self.result.delete(0,tk.END)
        self.result.insert(0,current)
#**********************تابع برای دکمه مساوی ونمایش نتیجه محاسبه ***************
    def Calculate(self):
        current=self.result.get()
        self.result.delete(0,tk.END)
        self.result.insert(0,eval(current)) # یک متد برای تبدیل رشته به نوع قبلی eval
#***************تابع برای پاک کردن ****************
    def Clear(self):
        self.result.delete(0,tk.END)
#******************** تابع برای پاک کردن آخرین مقدار وارد شده **************
    def backspace(self):
        current=self.result.get()[:-1]
        self.result.delete(0,tk.END)
        self.result.insert(0,current)


    def add_menus(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # ایجاد منو color با زیرمنوها
        color_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Color", menu=color_menu)
        color_menu.add_command(label="Gold", command=self.change_window_color_gold)
        color_menu.add_command(label="Green", command=self.change_window_color_green)
        color_menu.add_command(label="Red", command=self.change_window_color_red)
        color_menu.add_command(label="Blue", command=self.change_window_color_blue)

        # ایجاد منو about
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="Manufacturer", command=self.show_about_message)

    def change_window_color_gold(self):
        self.configure(background='gold')

    def change_window_color_green(self):
        self.configure(background='green')

    def change_window_color_red(self):
        self.configure(background='red')

    def change_window_color_blue(self):
        self.configure(background='blue')

    def show_about_message(self):
        popup = tk.Toplevel(self)
        popup.title("About")
        label = tk.Label(popup, text="App builder : Farzad Kermani")
        label.pack(pady=10, padx=10)
       

if __name__=='__main__':

    Calculator=Calculator()
    Calculator.mainloop()
    



                