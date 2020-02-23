import requests
'''for i in range(1000,2501):
    if i%7==0 and i%5!=0:
        print(i,end=",")''' 
'''a = requests.get("https://www.google.com/search?ei=vVs-XozYL7rH3LUPu_i5aA&q=ISO-8859-1&oq=ISO-8859-1&gs_l=psy-ab.3..0i131i67j0l9.3280.4838..5650...0.2..0.169.769.3j4......0....1j2..gws-wiz.....6..0i71j0i131j0i67j0i362i308i154i357.wWcwkw-9s4A&ved=0ahUKEwjMqvKasMHnAhW6I7cAHTt8Dg0Q4dUDCAo&uact=5")      
print(slice(a.text[0:1001])
print(a.encoding)s
for i in range (0,3):
    #a = requests.get(input('get url'))
    #print(a.url)
    #print(a.status_code)
    #print(a.elapsed)'''
a = requests.get('https://www.imdb.com/title/tt1187043/')
print(a.text[0:100])