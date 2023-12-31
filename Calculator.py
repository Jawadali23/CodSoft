from tkinter import *

root=Tk()
root.title('Simple Calculator')
root.resizable(0,0)
root.geometry('289x289')
root.config(bg='#3f3f4e')


text_result=Text(root,height=2,width=15,font=('verdana',24),bd=4,relief=SUNKEN)
text_result.grid(columnspan=5)
text_result.config(bg='#3f3f4e',fg='white')

calculation =""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def remove_last():
    global calculation
    calculation=calculation[:-1]
    update_display()

def update_display():
    text_result.delete(1.0,'end')
    text_result.insert(1.0,calculation)

def evaluation_calculation():
    global calculation
    
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,'Error')

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,'end')

    
btn7= Button(root,width=4,text='7',bg='#040406',fg='white',command=lambda:add_to_calculation('7'))
btn7.grid(row=1,column=0)
btn7.config(font=('Vardana',14))

btn8= Button(root,width=4,text='8',bg='#040406',fg='white',command=lambda:add_to_calculation('8'))
btn8.grid(row=1,column=1)
btn8.config(font=('Vardana',15))

btn9= Button(root,width=4,text='9',bg='#040406',fg='white',command=lambda:add_to_calculation('9'))
btn9.grid(row=1,column=2)
btn9.config(font=('Vardana',15))

btn4_button= Button(root,width=4,text='4',bg='#040406',fg='white',command=lambda:add_to_calculation('4'))
btn4_button.grid(row=2,column=0)
btn4_button.config(font=('Vardana',15))

btn5_button= Button(root,width=4,text='5',bg='#040406',fg='white',command=lambda:add_to_calculation('5'))
btn5_button.grid(row=2,column=1)
btn5_button.config(font=('Vardana',15))

btn6_button= Button(root,width=4,text='6',bg='#040406',fg='white',command=lambda:add_to_calculation('6'))
btn6_button.grid(row=2,column=2)
btn6_button.config(font=('Vardana',15))

btn1_button= Button(root,width=4,text='1',bg='#040406',fg='white',command=lambda:add_to_calculation('1'))
btn1_button.grid(row=3,column=0)
btn1_button.config(font=('Vardana',15))

btn2_button= Button(root,width=4,text='2',bg='#040406',fg='white',command=lambda:add_to_calculation('2'))
btn2_button.grid(row=3,column=1)
btn2_button.config(font=('Vardana',15))

btn3_button= Button(root,width=4,text='3',bg='#040406',fg='white',command=lambda:add_to_calculation('3'))
btn3_button.grid(row=3,column=2)
btn3_button.config(font=('Vardana',15))

add_button= Button(root,width=5,text='+',bg='#9897a9',fg='black',command=lambda:add_to_calculation('+'))
add_button.grid(row=1,column=3)
add_button.config(font=('Arial',15))

sub_button= Button(root,width=5,text='-',bg='#9897a9',fg='black',command=lambda:add_to_calculation('-'))
sub_button.grid(row=2,column=3)
sub_button.config(font=('Arial',15))

mul_button= Button(root,width=5,text='*',bg='#9897a9',fg='black',command=lambda:add_to_calculation('*'))
mul_button.grid(row=3,column=3)
mul_button.config(font=('Arial',15))

div_button= Button(root,width=5,text='/',bg='#9897a9',fg='black',command=lambda:add_to_calculation('/'))
div_button.grid(row=4,column=3)
div_button.config(font=('Vardana',15))

open_button= Button(root,width=4,text='(',bg='#040406',fg='white',command=lambda:add_to_calculation('('))
open_button.grid(row=4,column=0)
open_button.config(font=('Vardana',15))

zero_button= Button(root,width=4,text='0',bg='#040406',fg='white',command=lambda:add_to_calculation('0'))
zero_button.grid(row=4,column=1)
zero_button.config(font=('Vardana',15))

close_button= Button(root,width=4,text=')',bg='#040406',fg='white',command=lambda:add_to_calculation(')'))
close_button.grid(row=4,column=2)
close_button.config(font=('Vardana',15))

clear_button= Button(root,width=7,text='C',bg='#322d31',fg='white',command=clear_field)
clear_button.grid(row=5,column=0,columnspan=2)
clear_button.config(font=('Vardana',15))

equal_button= Button(root,width=6,text='=',bg='#1338be',fg='white',command=evaluation_calculation)
equal_button.grid(row=5,column=3)
equal_button.config(font=('Vardana',16))

previous_item=Button(root,width=4,text="←",bg='#bc5448',fg='white',command=remove_last)
previous_item.grid(row=5,column=2)
previous_item.config(font=('verdana',16))
root.mainloop()