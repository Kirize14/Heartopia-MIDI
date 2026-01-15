import time
from pynput.keyboard import Key, Controller

# Initialize the keyboard controller
keyboard = Controller()

def play_piano(sequence, bpm):
    """
    sequence: List of lists (chords) or single strings (notes)
    bpm: Beats per minute (tempo)
    """
    # Calculate the delay between notes in seconds
    delay = 60 / bpm
    
    print(f"Starting in 3 seconds... Switch to your piano window!")
    time.sleep(3)
    
    for block in sequence:
        # Check if the block is empty (a rest)
        if block is None or block == "":
            print("Resting...")
            time.sleep(delay)
            continue
            
        # If it's a chord (list)
        if isinstance(block, list):
            for key in block:
                keyboard.press(key)
            time.sleep(0.1) 
            for key in block:
                keyboard.release(key)
        
        # If it's a single note
        else:
            keyboard.press(block)
            time.sleep(0.1)
            keyboard.release(block)
        
        # Wait for the next beat (minus the 0.1s hold time)
        time.sleep(max(0, delay - 0.1))


# --- CONFIGURATION ---
# Your requested sequence: ['q','o','j'] together, then 'a'
my_song = [
    #ถ้าเธอรักใครคนหนึ่ง
    'b','n','e',['w', 'o'],'q','n',None,None,
    #เธอเองจะรู้หรือเปล่า
    'b','n','e',['w', '/'],'e','b',None,None,
    #ว่ารักของเธอชั่วคราวหรือรักของเธอยาวนานกว่านั้น
    'b','n','q',['w', '.'],'q','n','q',['w','p'],'q','n','q',['w',','],'q','e',None,None,

    #ถ้าเธอพบใครคนหนึ่ง 
    'b','n','e',['w', 'o'],'q','n',None,None,
    #ที่เธอให้ความสำคัญ
    'b','n','e',['w', '/'],'e','b',None,None,
    #เมื่อเธอสบตาคู่นั้นเธอรู้สึกอย่างไร
    'b','n','q',['w', '.'],'e','w','q',['w','p'],'q','n',None,['q',','],'/','p','z',None,


    #รักหนึ่งอาจเกิดด้วยใครลิขิตหรือมันอาจเกิดด้วยตาต้องใจ
    #ด ล ซ ล ด ร ม ซ      ด ล ซ ล ด ร ม ซ
    'q','n','b',['n','.'],'q','w','e',['b','/'],'q','n','b',['n','['],'q','w','e',['b','p'],

    #หรือมันอาจเกิดด้วยเหตุผลใด ใครเล่าเลยใครจะเลยล่วงรู้
    #ด   ล ซ ล  ด  ร  ม ร   ม ซ  ม  ร  ด ร ด ม
    'q','n','b',['n','.'],'q','w','e',['w','/'],'e','t','e',['w','['],'q','w','q',['e','p'],None,None,
    #อาจเกิดเพราะใครกำหนดหรือใครขีดกฎเกณฑ์ไว้ให้เจอ
    #ซ ล ม ร ด ซ ด ล ซ ล ด ร ม ซ
    'b',['n','.'],'e','w','q',['b','/'],'q','n' ,'b' ,['n','['] ,'q' ,'w' ,'e',['b','p'],
    #ให้เราต้องพบกันอยู่เสมอ ทุกครั้งไป
    #ด ล ซ ม ร ล ด ร ม ร ด
    'q','n','b',['e','o'],'w','n','q',['w','p'],None,None,'e',['w',','],None,'q'
]

# Set your tempo (e.g., 120 BPM)
play_piano(my_song, bpm=160)
