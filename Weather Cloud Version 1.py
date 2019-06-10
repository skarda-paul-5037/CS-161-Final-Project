'''
Using tkinter create an API and return the weather.

Searching by zipcode to get the weather data and return it
in degrees fahrenheit.

Goals:
-Add images that change with differing weather patterns.
(added goal to use a website vs local for images)
-change default tkinter icon in upper left of window.
-Keep the code as simple as possible(using what I learned
over time and eventually stopped fighting against).

By Paul Skarda
'''


import requests
from tkinter import *
import io
from PIL import ImageTk, Image
from urllib.request import urlopen
root=Tk()
root.title("Weather Cloud Version 1.0")
root.resizable(0,0)
root.wm_attributes('-topmost',1)
root.geometry("375x150")
#main area display
info = StringVar()
weather = Message(root, textvariable = info, width = 200) 	
info.set("What's your weather?")			
weather.grid(row=1, column=1)
image_address = 'http://openweathermap.org/img/w/13n.png'
image_open = urlopen(image_address)
image_file = io.BytesIO(image_open.read())
image_png = Image.open(image_file)
image_tk = ImageTk.PhotoImage(image_png.convert("RGB"))
label_img = Label(root,image=image_tk)
label_img.grid(row=1, column=2)


#function that gets weather
def getWeather():
	'''
        Main function of program.

        API key usage with json to get info from web.
        Images and unique method(unique to me) of using
        open weathers images and changing files with a
        str(url).
        '''
	api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=e15ad4da31d4c24a066df5f98fda33ad&units=imperial&zip='
	country_code = ',us'
	zip_code = e.get()
	url = api_address + zip_code + country_code
	json_data = requests.get(url).json()
	if 'message' in json_data:
		info.set('Invalid zip code.')
	else:
		city = json_data['name']
		description = json_data['weather'][0]['description'] 
		icon = json_data['weather'][0]['icon']
		temperature = str(json_data['main']['temp']) + u'\u00b0' + " F"
		info.set(city + "\n" + description + "\n" + temperature)
		#Imported images location and calling
		image_main = 'http://openweathermap.org/img/w/'
		image_address = image_main + str(icon) + '.png'
		image_open = urlopen(image_address)
		image_file = io.BytesIO(image_open.read())
		image_png = Image.open(image_file)
		image_tk2 = ImageTk.PhotoImage(image_png.convert("RGB")) 
		label_img.configure(image=image_tk2)	
		label_img.image = image_tk2	
label=Label(root,text='Enter your zip code:  ')
label.grid(row=3, column=1, sticky='E')
e=Entry(root)
e.grid(row=3, column=2)
sub = Button(root,text='Get Weather', command = getWeather)
sub.grid(row=4, column=2)
root.iconbitmap('cloud.ico')
root.mainloop()
