from random  import randint ,choice
from customtkinter import *
class Encode():
    
    def __generate_key(self) -> str:
        __key=""
        while True:
            for i in range(0,4):
              __key+=str(randint(0,9))
            if int(__key[0])*int(__key[3])-int(__key[1])*int(__key[2] 
            )!= 0:
                break
        return __key
    def __text_to_int(self,txt):
        __int_list=[]
        k=0
        v=int(len(txt)/2)
        for i in range(0,v):
            __int_list.append(
                [ord(j) for j in txt[k:k+2]]
            )
            k+=2
        if len(txt)%2==1:
            __int_list.append([ord(txt[len(txt)-1]),0])
        return __int_list
    def convert_cyper_list(self,int_list,key):
        __cyper_int_list=[]
        for i in int_list:
            __cyper_int_list.append(
                [
                    i[0]*key[0]+i[1]*key[2],
                    i[0]*key[1]+i[1]*key[3]
                                    ]
            )
        return __cyper_int_list
    def gen_key_int(self,key):
        pass
    def cypertext(self):
        str_=""
        for i in self.__cypher_list_:
            for j in i:
                str_+=chr(j)
        return (self.key,str_)
    def __init__(self,text):
        self.key=[ int(i) for i in self.__generate_key()]
        self.__cypher_list_=self.convert_cyper_list(self.__text_to_int(text),self.key)
        Encode.k=self.__cypher_list_
class Decode:
    def __init__(self,key,cyphertext) -> None:
        self.key=[int(i) for i in key]
        self.cyphertext=cyphertext
        self.cypher_int=self.convert_cyphertext_to_cypher_int()
    def convert_cyphertext_to_cypher_int(self):
        cypher_list=[]
        for i in self.cyphertext:
            cypher_list.append(ord(i))
        return cypher_list
    def cyphertexTONormal(self):
        normal_text=''
        ascii_value=[]
        rem=self.key[0]*self.key[3]-self.key[1]*self.key[2]
        decode_key= [self.key[3]/rem,
                     -(self.key[1]/rem),
                     -(self.key[2]/rem),
                     self.key[0]/rem
                     ]
        for i in range(0,len(self.cypher_int),2):
            ascii_value.extend(
                [
                    self.cypher_int[i]*decode_key[0]+self.cypher_int[i+1]*decode_key[2],
                    self.cypher_int[i]*decode_key[1]+self.cypher_int[i+1]*decode_key[3]
                                    ]
            )
        for i in ascii_value:
            normal_text+=chr(round(i))
        return normal_text
from customtkinter import *

class gui(Encode,Decode):
    def show_frame(self, frame):
        frame.tkraise()

    def __init__(self):
        self.root = CTk()
        self.root.resizable(False, False)
        self.root.geometry("900x700")
        self.root.title("Encode Decode")
        self.root.iconbitmap("maghs_icon.ico")
        self.home_page = CTkFrame(self.root)
        self.home_page.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.encode_page = CTkFrame(self.root)
        self.encode_page.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.decode_page= CTkFrame(self.root)
        self.decode_page.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.encode_button = CTkButton(
            master=self.home_page,
            text="Encode Text",
            font=("Arial", 30),
            width=300,
            height=50,
            command=lambda: self.encode(self.encode_page)
        )
        self.encode_button.pack(anchor="center", pady=(280, 20))

        self.decode_button = CTkButton(
            master=self.home_page,
            text="Decode Text",
            font=("Arial", 30),
            width=300,
            height=50,
            command=lambda :self.decode(self.decode_page)
        )
        self.decode_button.pack(anchor="center")

        self.show_frame(self.home_page)  # Show home_page initially

    def decode(self,frame):
        def decode_page_():
            def copy_decoded_text():
                self.root.clipboard_clear()
                self.root.clipboard_append(self.decoded_text.get("1.0","end-1c"))
            text=self.decoded_text.get("1.0","end-1c")
            key=self.key_.get().replace(" ","")
            decode_page.destroy()
            Decode.__init__(self,key,text)
            self.show_frame(frame)
            self.copy_decode = CTkButton(self.decode_page, text="copy", width=30, height=10,command=copy_decoded_text)
            self.copy_decode.pack(anchor="e", pady=(50, 0))
            self.decoded_text = CTkTextbox(
                self.decode_page,
                width=800,
                height=600,
                font=("Arial", 18)
            )
            self.decoded_text.pack(anchor="center")
            self.decoded_text.insert("1.0",Decode.cyphertexTONormal(self))
        decode_page=CTkFrame(self.root)
        decode_page.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_frame(decode_page)
        self.decode_text_page = CTkFrame(decode_page, width=850, height=400)
        self.decode_text_page.pack(anchor="center", pady=20)
        self.decode_text_page.pack_propagate(False)
        CTkLabel(master=self.decode_text_page, text="Enter Encrypted Text", font=("Arial", 18)).pack(anchor="w", padx=5)
        self.decoded_text = CTkTextbox(
            self.decode_text_page,
            width=850,
            height=390,
            font=("Arial", 18)
        )
        self.decoded_text.pack(anchor="center", pady=(0, 20))
        self.key_frame_ = CTkFrame(
            decode_page, width=850, height=100
        )
        self.key_frame_.pack(anchor="center")
        self.key_frame_.pack_propagate(False)
        CTkLabel(master=self.key_frame_, text="Enter Key", font=("Arial", 18)).pack(anchor="w", padx=5)
        self.key_ = CTkEntry(
            self.key_frame_,
            width=850,
            height=50,
            font=("Arial", 18)
        )
        self.key_.pack(anchor="center")
        self.decode__=CTkButton(decode_page,text="Decode",width=200,height=50,font=("Arial",20),command=decode_page_)
        self.decode__.pack(anchor="center",pady=(30,0))
    def encode(self, frame):
        self.show_frame(frame)
        def encoded_page():
            def copy_text():
                self.root.clipboard_clear()
                self.root.clipboard_append(self.encoded_text.get("1.0","end-1c"))
                self.copy.configure(text="copied!")
            def copy_key():
                self.root.clipboard_clear()
                self.root.clipboard_append(self.key.get("1.0","end-1c"))
                self.copy_key.configure(text="copied!")
            Encode.__init__(self,self.text_for_encode.get("1.0","end-1c"))
            a=Encode.cypertext(self)
            self.text_for_encode.destroy()
            self.encode.destroy()
            self.encode_text_page=CTkFrame(self.encode_page,width=850,height=400)
            self.encode_text_page.pack(anchor="center",pady=20)
            self.encode_text_page.pack_propagate(False)
            self.copy=CTkButton(self.encode_text_page,text="copy",width=30,height=10,command=copy_text)
            self.copy.pack(anchor="e")
            CTkLabel(master=self.encode_text_page,text="Encrypted Text",font=("Arial",18)).pack(anchor="w",padx=5)
            self.encoded_text=CTkTextbox(
                self.encode_text_page,
                width=850,
                height=390,
                font=("Arial",18)
            )
            self.encoded_text.pack(anchor="center",pady=(0,20))
            self.key_frame=CTkFrame(
                self.encode_page,width=850,height=100
            )
            self.key_frame.pack(anchor="center")
            self.key_frame.pack_propagate(False)
            self.copy_key=CTkButton(self.key_frame,text="copy",width=30,height=10,command=copy_key)
            self.copy_key.pack(anchor="e")
            CTkLabel(master=self.key_frame,text="Key",font=("Arial",18)).pack(anchor="w",padx=5)
            self.key=CTkTextbox(
                self.key_frame,
                width=850,
                height=50,
                font=("Arial",18)
            )
            self.key.pack(anchor="center")
            self.encoded_text.insert("1.0",a[1])
            self.key.insert("1.0",a[0])
            self.encoded_text.configure(state="disabled")
            self.key.configure(state="disabled")
        self.text_for_encode = CTkTextbox(
            master=self.encode_page,
            width=850,
            height=500,
            font=("Arial",20),
        )
        self.text_for_encode.pack(anchor="center", pady=20)
        self.encode=CTkButton(self.encode_page,text="Encode",width=200,height=50,font=("Arial",20),command=encoded_page)
        self.encode.pack(anchor="center")
    def main(self):
        self.root.mainloop()
if __name__ == "__main__":
    r = gui()
    r.main()