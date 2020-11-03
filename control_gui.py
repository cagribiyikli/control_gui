from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, END


def url_control():
    url = str(girilenDeger.get())
    found_exceptions = []
    if " " in url:
        found_exceptions.append("FHU-6")
    if url.startswith("."):
        found_exceptions.append("FHU-0")
    if url.startswith("-"):
        found_exceptions.append("FHU-1")
    if url.startswith("?"):
        found_exceptions.append("FHU-2")
    if url.startswith(" "):
        found_exceptions.append("FHU-3")
    if url.endswith(" "):
        found_exceptions.append("FHU-4")
    if url.startswith("//"):
        found_exceptions.append("FHU-5")
    if len(found_exceptions) > 0:
        messagebox.showerror("Dikkat!", "Format hatasi URL")
    else:
        messagebox.showinfo("Tebrikler", "URL'de Hata Bulunamadi")
    finish.set(url)
    return found_exceptions


def domain_control():
    domain = str(girilenDeger.get())

    found_exception = []
    if not domain.islower():
        found_exception.append("FHA-1")
    if ".." in domain:
        found_exception.append("FHA-2")
    if domain.endswith("."):
        found_exception.append("FHA-3")
    if domain.startswith("."):
        found_exception.append("FHA-4")
    if ":" in domain:
        found_exception.append("FHA-5")
    if domain.count(".") == 0:
        found_exception.append("FHA-6")
    if " " in domain:
        found_exception.append("FHA-7")
    if "," in domain:
        found_exception.append("FHA-8")
    if "/" in domain:
        found_exception.append("FHA-9")
    if "?" in domain:
        found_exception.append("FHA-10")
    if len(found_exception) > 0:
        messagebox.showerror("Dikkat!", "Format hatasi Domain")
    else:
        messagebox.showinfo("Tebrikler", "Domain'de Hata Bulunamadi")
    finish.set(domain)
    return found_exception


def charachter_control():
    ip = str(girilenDeger.get())
    exceptions = []
    ip_charackter = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    for charackter in ip:
        if charackter in ip_charackter:
            continue
        else:
            exceptions.append("FHI-1")
            break
    return exceptions


def ip_control():
    ip = str(girilenDeger.get())
    exceptions = charachter_control()
    if ".." in ip:
        exceptions.append("FHI-2")
    if ip.endswith("."):
        exceptions.append("FHI-3")
    if ip.startswith("."):
        exceptions.append("FHI-4")
    if ":" in ip:
        exceptions.append("FHI-5")
    if ip.count(".") != 3:
        exceptions.append("FHI-6")
    if " " in ip:
        exceptions.append("FHİ-7")
    if "," in ip:
        exceptions.append("FHI-8")
    if "/" in ip:
        exceptions.append("FHI-9")
    if "?" in ip:
        exceptions.append("FHI-10")  # FHI-10 dict eklemedim bilinmeyen hata görebilmek
    if len(exceptions) == 0:
        blocks = ip.split(".")
        for block in blocks:
            block_as_int = int(block)
            if 0 > block_as_int or block_as_int > 255:
                exceptions.append("FHI-0")
    if len(exceptions) > 0:
        messagebox.showerror("Dikkat!", "Format hatasi IP")
    else:
        messagebox.showinfo("Tebrikler", "IP'de Hata Bulunamadi")

    finish.set(ip)
    return exceptions


def sxt_control():
    url = str(girilenDeger.get())

    if chr(2) in url:
        a = url.replace(chr(2), "-")
        finish.set(a)
        messagebox.showerror("Duzeltme Uygulandı", "Adreste SXT tespit edildi.")
    else:
        finish.set(url)
        messagebox.showerror("Tebrikler", "Düzeltilecek Birşey yok.")


def dict_of_ip():
    dict = {
        "FHI-0": "ip bloklari 0-255 arasinda olmaldir.",
        "FHI-1": "ip bloklari harf alamaz .",
        "FHI-2": "ip (..) gelemez.",
        "FHI-3": "ip (.) ile bitemez.",
        "FHI-4": "ip (.) ile baslayamaz.",
        "FHI-5": "ip (:) olamaz.",
        "FHI-6": "ip yanyana olmamak uzere 3 adet (.) olmalidir.",
        "FHI-7": "ip bosluk olamaz.",
        "FHI-8": "ip (,) olamaz.",
        "FHI-9": "ip (/) olamaz.",
        "FHI-11": "ip adresi 4 bloktan olusur!!"
    }
    result = []
    dict_exceptions = ip_control()
    for excep in dict_exceptions:
        if excep in dict.keys():
            result.append(dict.get(excep))
        else:
            result.append("Bilinmeyen hata!")
    if len(result) > 0:
        exception.set(result)
    return result


def dict_of_domains():
    dicts = {
        "FHA-1": "Alan adinda buyuk harf olamaz.",
        "FHA-2": "Alan adinda (..) gelemez.",
        "FHA-3": "Alan adi (.) ile bitemez.",
        "FHA-4": "Alan adi (.) ile baslayamaz.",
        "FHA-5": "Alan adinda (:) olamaz.",
        "FHA-6": "Alan adinda en az (.) olmalidir.",
        "FHA-7": "Alan adinda bosluk olamaz.",
        "FHA-8": "Alan adinda (,) olamaz.",
        "FHA-9": "Alan adinda (/) olamaz."
    }
    result = []
    exceptions = ip_control()
    for excep in exceptions:
        if excep in dicts.keys():
            result.append(dicts.get(excep))
    if len(result) > 0:
        exception.set(result)
    return result


def dict_of_find_exceptions():
    dict_of_url = {
        "FHU-0": "Url . ile baslayamaz.",
        "FHU-1": "Url - ile baslayamaz.",
        "FHU-3": "Url basinda bosluk olamaz.",
        "FHU-2": "Url ? ile baslayamaz.",
        "FHU-4": "Url sonunda bosluk olamaz.",
        "FHU-5": "Url // ile baslayamaz.",
        "FHU-6": "Url icinde bosluk var.Fiziksel evrağı kontrol ediniz----"}
    list_of_exceptions = []
    exceptions = url_control()
    for excep in exceptions:
        if excep in dict_of_url.keys():
            list_of_exceptions.append(dict_of_url.get(excep))
    if len(list_of_exceptions) > 0:
        exception.set(list_of_exceptions)
    return list_of_exceptions


def clear_labels():
    girilenDeger.delete(0, END)
    finish.set("")
    exception.set("")


rootWindow = Tk()  # Ana pencere
rootWindow.title("--HoşGeldiniz--")
rootWindow.geometry('1200x650+0+0')

# girilen
girilenDeger = Entry(rootWindow)  # girilen icin girilecek alan
girilenDeger.place(x=180, y=0, width=400, height=30)
labelGirilen = Label(rootWindow, text='Kontrol Edilecek Adres', font=("Verdana", 10, "bold"))  # girilen icin label
labelGirilen.place(x=0, y=5)

# çikilan
finish = StringVar()  # cikilan icin alan
finishValue = Entry(rootWindow, textvariable=finish)
finishValue.place(x=765, y=0, width=360, height=30)
finishLabel = Label(rootWindow, text='Dönüştürülen Adres', font=("Verdana", 10, "bold"))  # cikan icin label
finishLabel.place(x=1130, y=5)

# hatalar
exception = StringVar()
exceptionValue = Entry(rootWindow, textvariable=exception)
exceptionValue.place(x=150, y=500, width=1100, height=150)
exceptionLabel = Label(rootWindow, text="Bulunan Hatalar", font=("Verdana", 10, "bold"))
exceptionLabel.place(x=0, y=550)

# butonlar
convertButton = Button(rootWindow, text='SXT KONTROL', command=sxt_control, fg="Green", font=("Verdana", 10, "bold"),
                       height=1, width=13)
convertButton.place(x=600, y=0)
exceptionButton = Button(rootWindow, text='URL KONTROL', command=dict_of_find_exceptions, fg="Green",
                         font=("Verdana", 10, "bold"), height=1, width=13)
exceptionButton.place(x=600, y=100)
domainButton = Button(rootWindow, text='DOMAIN KONTROL', command=dict_of_domains, fg="Green",
                      font=("Verdana", 10, "bold"), height=1, width=13)
domainButton.place(x=600, y=200)
IpButton = Button(rootWindow, text="IP KONTROL", command=dict_of_ip, fg="Green", font=("Verdana", 10, "bold"), height=1,
                  width=13)
IpButton.place(x=600, y=300)
clearButton = Button(rootWindow, text='TEMİZLE', command=clear_labels, fg="red", font=("Verdana", 10, "bold"), height=1,
                     width=13)
clearButton.place(x=600, y=400)

rootWindow.mainloop()
