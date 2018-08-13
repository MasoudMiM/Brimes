import numpy as np
import Tkinter as tk

def DispRela():
    TimePeriod = float(TP.get())    
    WaterDepth = float(WD.get())
    
    L = 1.0;
    l = L+1.0;
    while np.abs(L-l)>0.01:
        L=l
        l=9.81/2.0/np.pi*TimePeriod**2*np.tanh(2.0*np.pi*WaterDepth/L)
        
    WL = l
    d = WL/10.0
    z = d
    R2 = WL/20.0
    Kd = 0.0937*WL
    R0 = Kd*np.exp(2*np.pi*z/WL)
    Rd = Kd
    Offset = R2/2.0
    R2p = 1.5*R2
    WPL = np.sqrt(Rd**2-R2**2)
    
    labelresult = tk.Label(root, text="Wavelength = %g m" %WL).grid(row=7,columnspan=2, sticky=tk.W)
    draflabel = tk.Label(root, text="Draft and depth below (d & z) = %g m" %d).grid(row=8,columnspan=2, sticky=tk.W)
    sternlabel = tk.Label(root, text="Stern radius (R_2) = %g m" %R2).grid(row=9,columnspan=2, sticky=tk.W)
    designparam = tk.Label(root, text="Design parameter (K_D) = %g m" %Kd).grid(row=10,columnspan=2, sticky=tk.W)
    paunchradiuslabel = tk.Label(root,text="Paunch radius (R_0) = %g m" %R0).grid(row=11,columnspan=2, sticky=tk.W)
    paunchradiusSWLlabel = tk.Label(root,text="Paunch radius at SWL (R_d) = %g m" %Rd).grid(row=12,columnspan=2, sticky=tk.W)
    offsetlabel = tk.Label(root,text="Offset distance (OO') = %g m" %Offset).grid(row=13,columnspan=2, sticky=tk.W)
    paucnhRmodifiedlabel = tk.Label(root, text="Modified paunch radius (R'_2) = %g m" %R2p).grid(row=14,columnspan=2, sticky=tk.W)
    WPLengthlabel = tk.Label(root, text="Water plane length (L_D) = %g m" %WPL).grid(row=15,columnspan=2, sticky=tk.W)
    return
    
root = tk.Tk()
root.title("Salter Duck Design")
root.geometry("1100x300")

photo = tk.PhotoImage(file="PodDesign.png")
label = tk.Label(root, image = photo).grid(rowspan=25,column=3)
#root.configure(background='grey')

# variables
TP = tk.StringVar()
WD = tk.StringVar()

#------- Time Period
label_TP=tk.Label(root, text="Time Period: ").grid(row=0) 
label_TP_unit = tk.Label(root, text="(s)").grid(row=0,column=2, sticky=tk.E)
TimePeriod=tk.Entry(root, textvariable=TP).grid(row=0,column=1, sticky=tk.E)
        
#------- Water Depth
label_WD=tk.Label(root, text="Water Depth: ").grid(row=1)
label_WD_unit = tk.Label(root, text="(m)").grid(row=1,column=2, sticky=tk.E)
WaterDepth=tk.Entry(root, textvariable=WD).grid(row=1,column=1, sticky=tk.E)

# Button
button1=tk.Button(root,text="Calculate", command=DispRela).grid(row=4,column=0)


root.mainloop()


