
from gtts import gTTS
import sqlite3
import os
from moviepy.editor import *

 
def mp3(mytext,  name):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    name2 ="333\\"+ str(name) + ".mp3"
    print(name2)
    myobj.save(name2)

    

def update(id, stat):

    try:
        conn = sqlite3.connect('texttomp3.db')
        cursor = conn.cursor()
        sql = "Update data set data3 = ? where id = ?"
        data = (stat, id)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)



def singlevideo():
    
    conn = sqlite3.connect('texttomp3.db')
    cursor = conn.cursor()
    
    query = "select * FROM data where data3 not like '0'"
    cursor.execute(query)
   
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    for row in records:
        mp3 ="333\\"+ str(row[0]) + ".mp3"
        mp4 ="333\\"+ str(row[0]) + ".mp4"
        audio_clip = AudioFileClip(mp3)
        image_clip =[]
        image_clip.append ( ImageClip(row[1]).set_duration(audio_clip.duration))
        
        video_clip = concatenate_videoclips(image_clip)
    
        video_clip.set_audio(audio_clip)
        video_clip.duration = audio_clip.duration
    
        video_clip.audio = audio_clip
    
        video_clip.write_videofile(mp4 ,  fps=1, codec="mpeg4" )


def totalvideo():
      

    image_clip =[]
    #image_clip.append ( ImageClip("pic\\2.jpg").set_duration(audio_clip.duration/2))
    #image_clip.append ( ImageClip("pic\\3.jpg").set_duration(audio_clip.duration/2))



    obj = os.scandir("333\\")
    jpg =[]

    for entry in obj:
        if entry.is_file():
            if entry.name.lower().endswith('.mp4') :
                #print(entry.name)
                jpg.append(VideoFileClip("333\\" + entry.name))
               

    
    video_clip = concatenate_videoclips(jpg , method='compose')
    
   
    
    video_clip.fx( vfx.speedx, 1.35).write_videofile("333\\final.mp4" ,  fps=1, codec="mpeg4")




    

try:
   
    conn = sqlite3.connect('texttomp3.db')
    cursor = conn.cursor()
    
    query = "select * FROM data where data3 like '0'"
    cursor.execute(query)
   
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    for row in records:
        #print(row[2])
        mp3(row[2],row[0])
        namemp3 ="333\\"+ str(row[0]) + ".mp3"
        update(row[0],namemp3)

    cursor.close()    
    #singlevideo()
    totalvideo()
    


except sqlite3.Error as error:
    print(error)    
