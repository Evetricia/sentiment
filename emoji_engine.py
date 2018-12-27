import emoji_data_python
import numpy as np

class Engine:
    def __init__(self):
        useful_emoji = ["😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊","😋","😎","😍","😘","😗","😙","😚","🙂","🤗","🤔","😐","😑","😶","🙄","😏","😣","😥","😮","🤐","😯","😪","😫","😴","😌","😛","😜","😝","🤤","😒","😓","😔","😕","🙃","🤑","😲","🙁","😖","😞","😟","😤","😢","😭","😦","😧","😨","😩","😬","😰","😱","😳","😵","😡","😠","😷","🤒","🤕","🤢","🤧","😇","🤠","🤡","🤥","🤓","😈","👿","👹","💀","👻","👽","🤖","💩","💪","👈","👉","👆","🖕","👇","🤞","🖖","🤘","🖐","✋","👌","👍","👎","✊","👊","🤛","🤜","🤚","👋","👏","👐","🙌","🙏","🤝","💅","👂","👃","🔥","❤","☺","☹","☝","✌","✍"]
        lib_emoji_name_pairs = []
        for each in emoji_data_python.emoji_data:
            if each.char in useful_emoji:
                lib_emoji_name_pairs.append([each.name, each.char])
        
        #==================================================#
        # define sentiment scores of emojis
        #==================================================#        
        es = np.zeros(len(lib_emoji_name_pairs))
    
        es[0 :10] = [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 1]
        es[10:20] = [-0.8, 0.8, 0, 0, 0, 0, 0, -0.1, 0.2, -0.3]
        es[20:30] = [0.3, -0.1, -0.9, 0.3, 0.7, 0.8, 0.6, 0.7, 0.8, 0.5]
        es[30:40] = [0.7, 0.7, 0.5, 0.3, 0.7, 0.6, 0.3, 0.8, 0.7, 0.4]
        es[40:50] = [0, -0.1, -0.2, -0.2, -0.5, -0.1, -0.1, 0.8, 0.8, 0.8]
        es[50:60] = [0.8, 0.4, 0.5, 0.4, -0.4, -0.3, -0.6, -0.4, -0.1, -0.2]
        es[60:70] = [-0.2, -0.1, -0.1, -0.2, -0.3, -0.3, 0, -0.1, -0.2, -0.2]
        es[70:80] = [-0.1, -0.1, -0.3, -0.2, -0.1, -0.1, 0, -0.1, 0, -0.2]
        es[80:90] = [-0.2, 0.2, 0, 0, 0.7, 0, -0.2, 0.2, -0.1, 0]
        es[90:100] = [0, -0.2, 0, 0.6, 0.3, 0, 0.1, 0.1, 0.7, 0.1]
        es[100:109] = [0.2, 0.2, -0.2, 0.7, 0.4, -0.1, -0.1, 0.2, 0.2]
        
        for i in range(len(lib_emoji_name_pairs)):
            lib_emoji_name_pairs[i].append(es[i])
        
        self.emoji_lib = lib_emoji_name_pairs


    def print_emoji_lib(self):
        return self.emoji_lib


    def extract_emoji_info(self, str):
        occured_emojis_info = []
        emojis = emoji_data_python.get_emoji_regex().findall(str)
        for emoji in emojis:
            for [name, icon_char, score] in self.emoji_lib:
                if emoji == icon_char:
                    occured_emojis_info.append([name, score])

        return occured_emojis_info  


    
















