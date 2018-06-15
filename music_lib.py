from libpytunes import Library
import pandas as pd
import datetime
import matplotlib.pyplot as plt

l = Library("C:\Python34\music_Library.xml")

new_list = []
counter=0

new_list = [song.__dict__ for id, song in l.songs.items() if song and song.kind]


df = pd.DataFrame(new_list)
##print(df.head())
#writer = pd.ExcelWriter('c:\\Users\\cdonohu\\Documents\\python\\music_output_test.xlsx', engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Sheet1')
#writer.save()

df['genre'].plot()
plt.show()






