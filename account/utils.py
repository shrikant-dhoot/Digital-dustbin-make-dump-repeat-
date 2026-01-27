import random

bucket_jokes = [
    
     "😂 Dream zinda hai, bas motivation ICU mein hai.",
     
    "🤡 Dream ka plan clear hai: aaj nahi… kal bhi nahi.",
    
    "😴 Zinda hai, par effort airplane mode pe hai.",
    
    "📱😂 Dream ne WhatsApp status laga rakha hai: Busy.",
    
    "🏋️🤡 Is dream ka confidence high hai, kaam zero.",
    
    "🎬😆 Dream keh raha hai: ‘Bas ek Netflix episode ke baad start’.",
    
    "🔋😴 Dream chal raha hai, battery 2% pe hai.",
    
    "🤝🤡 Dream active hai, par owner inactive hai.",
    
    "🗓️😂 Kal se pakka start karenge — dream still believes.",
    
    "🧠😵 Dream hai, direction nahi.",
    
    "😆 Is dream ko chhodne ka mood nahi… aaj.",
    
    "🤡 Dream abhi bucket mein hai, dustbin door hai (abhi).",
    
    "🥲 Progress slow hai, excuses fast.",
    
    "😴 Dream bol raha hai: ‘Abhi mood nahi bana’.",
    
    "📦😂 Ye dream gym membership jaisa hai — hai, use nahi hota.",
    
    "🕒🤡 Dream late nahi hai… bas slow chal raha hai.",
    
    "🤷‍♂️😂 Dream keh raha hai: ‘Pressure mat de bhai’.",
    "🔥😴 Spark hai, aag baad mein.",
    
    "📝🤡 Dream ka syllabus ready hai, padhna pending.",
    
    "😅 Dream zinda hai… bas reality se door hai."
    
    "Dream zinda hai… bas system hang hai",
    
    
]


dustbin_jokes = [
    
    "💀 Dream ko dustbin mein daala… kyunki use bhi pata tha mujhse nahi hone wala.",

"😂 Ye dream itna late ho gaya ki khud hi resign de diya.",

  "📅🤡 Dream bol raha tha ‘kal se pakka’… calendar ne bhi give up kar diya.",

"🤡 Is dream ka confidence zyada tha, aukaat kam.",

"🗑️😂 Dream ko dustbin bheja kyunki usne bhi mujhe seriously nahi liya.",

"🪦😴 RIP Dream — zinda rehne ka koi solid reason nahi mila.",

"🤝💀 Dream ne bola: ‘Bhai tu rehne de, main ja raha hoon’.",

"💡😵 Is dream ka future bright tha… bas bulb lagana bhool gaye.",

"📩😂 Dream ko itna ignore kiya ki ab wo spam folder mein chala gaya.",

"🤱😴 “Ye dream motivation ke bina paida ho gaya tha.",

"🤡 Dream tha… bas galat insaan ke paas aa gaya.",

"😵‍💫 Dream ko dustbin bheja, kyunki main khud confused tha.",

"📺💀 Is dream ka downfall Netflix series jaisa tha — slow but sure.",

"😴🤦 Dream ne try kiya survive karne ka, par owner lazy nikla.",

"📦😂 Ye dream ‘optional’ ban gaya tha life mein.",

"🪦🤡 Dream expired. Last words: ‘Tu nahi badlega’.",

"🏃💨 Is dream ka struggle dekh ke motivation bhi bhaag gaya.",

"🗑️🤡 Dream ke saath thodi si self-respect bhi dustbin chali gayi.",

"🥲💭 Ye dream zyada hi umeed rakh baitha tha.",

"🤝😴 “Dream aur main — dono ne ek-dusre se expectations kam kar di.",

"🤡 Dream nahi tha, misunderstanding thi.",

"💀 Is dream ka bhi patience khatam ho gaya.",

"🖥️😂 Dream tha, par system compatible nahi tha.",

"❌💭 Dream uninstall kar diya.",

"📝🤡 Ye dream bas form bharne ke liye bana tha.",
   
    
]


def get_random_jokes(category):
    if category == "bucket":
       return random.choice(bucket_jokes)
    else:
        return random.choice(dustbin_jokes)    