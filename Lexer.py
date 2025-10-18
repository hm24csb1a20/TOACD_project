from token import Token,TokenType
from typing import Any

class Lexer:
    def __init__(self, source: str) -> None:
        """
        source the string version of our source code
        """
        self.source = source

        self.position: int = -1
        self.read_position: int = 0
        self.line_no: int = 1

        self.current_char: str | None = None

        self.__read_char()


    def __read_char(self) -> None:
        
        if self.read_position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    # handling all the edge cases we might see in our code 
    def __skip_whitespace(self) -> None:
        
        while self.current_char in [' ', '\t', '\n', '\r']:
            
            if self.current_char == '\n':
                self.line_no += 1
            
            self.__read_char()
    def __is_digit(self, ch: str) -> bool:
    
        return '0' <= ch and ch <= '9'

    def __is_letter(self, ch: str) -> bool:
        return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_'

    # creating the token at the pointer 
    def __new_token(self, tt: TokenType, literal: Any) -> Token:
        
        return Token(type=tt, literal=literal, line_no=self.line_no, position=self.position)
    

    def __read_number(self) -> Token:
        
        start_pos: int = self.position
        dot_count: int = 0

        output: str = ""
        while self.__is_digit(self.current_char) or self.current_char == '.':
            if self.current_char == '.':
                # for decimal
                dot_count += 1
            
            if dot_count > 1:
                print(f"not a vaid decimal at  position {self.position}")
                return self.__new_token(TokenType.ILLEGAL, self.source[start_pos:self.position])
            
            output += self.source[self.position]
            self.__read_char()
            # if no is at the end of the fiel
            if self.current_char is None:
                break

        if dot_count == 0:
            return self.__new_token(TokenType.INT, int(output))
        else:
            return self.__new_token(TokenType.FLOAT, float(output))
        
    def __read_identifier(self) -> str:
        position = self.position
        while self.current_char is not None and (self.__is_letter(self.current_char) or self.current_char.isalnum()):
            self.__read_char()
        
        return self.source[position:self.position]
    

    # our main moving the pointer we are refrencing
    def next_token(self) -> list[Token]:
        tok: Token = None

        
        self.__skip_whitespace()

        # Skip line comments starting with //
        if self.current_char == '/' and self.__peek_char() == '/':
            while self.current_char is not None and self.current_char != '\n':
                self.__read_char()
            self.__skip_whitespace()
            return self.next_token()

        match self.current_char:
            case '+':
                tok = self.__new_token(TokenType.PLUS, self.current_char)
            case '-':
                # Handle ->
                if self.__peek_char() == '>':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.ARROW, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.MINUS, self.current_char)
            case '*':
                tok = self.__new_token(TokenType.ASTERISK, self.current_char)
            case '/':
                tok = self.__new_token(TokenType.SLASH, self.current_char)
            case '^':
                tok = self.__new_token(TokenType.POW, self.current_char)
            case '%':
                tok = self.__new_token(TokenType.MODULUS, self.current_char)
            case '<':
                # Handle <=
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.LT_EQ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.LT, self.current_char)
            case '>':
                # Handle >=
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.GT_EQ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.GT, self.current_char)
            case '=':
                # Handle ==
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.EQ_EQ, ch + self.current_char)
                else:
                    tok = self.__new_token(TokenType.EQ, self.current_char)
            case '!':
                
                if self.__peek_char() == '=':
                    ch = self.current_char
                    self.__read_char()
                    tok = self.__new_token(TokenType.NOT_EQ, ch + self.current_char)
                else:
                    
                    tok = self.__new_token(TokenType.ILLEGAL, self.current_char)
            case ':':
                tok = self.__new_token(TokenType.COLON, self.current_char)
            case ';':
                tok = self.__new_token(TokenType.SEMICOLON, self.current_char)
            case ',':
                tok = self.__new_token(TokenType.COMMA, self.current_char)
            case '"':
                tok = self.__new_token(TokenType.STRING, self.__read_string())
            case '(':
                tok = self.__new_token(TokenType.LPAREN, self.current_char)
            case ')':
                tok = self.__new_token(TokenType.RPAREN, self.current_char)
            case '{':
                tok = self.__new_token(TokenType.LBRACE, self.current_char)
            case '}':
                tok = self.__new_token(TokenType.RBRACE, self.current_char)
            case None:
                tok = self.__new_token(TokenType.EOF, "")
            case _:
                # if self.__is_letter(self.current_char):
                #     literal: str = self.__read_identifier()
                #     tt: TokenType = lookup_ident(literal)
                #     tok = self.__new_token(tt=tt, literal=literal)
                #     return tok
                if self.__is_digit(self.current_char):
                    tok = self.__read_number()
                    return tok
                else:
                    tok = self.__new_token(TokenType.ILLEGAL, self.current_char)

        self.__read_char()
        return tok