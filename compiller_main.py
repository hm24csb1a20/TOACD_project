from lexer import Lexer
import os

LEXER_DEBUG :bool= True



if __name__=='__main__':
    
    current = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current,"test.lime")
    with open("test.lime","r") as file :
        code :str = file.read()
        if(LEXER_DEBUG):
            debug_lex: Lexer = Lexer(source=code)
        while(debug_lex.current_char is not None):
            print(debug_lex.next_token())

    
    