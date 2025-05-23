from typer import Typer, Option
from rich.console import Console
from typing_extensions import Annotated


app = Typer()

class Alphabet:
    def __init__(self, categorie: str = "deutsch"):
        self.categorie = categorie
        self.alphabet = {
            'A': {'deutsch': 'Anton', 'nato': 'Alpha'}, 
            'B': {'deutsch': 'Berta', 'nato': 'Bravo'}, 
            'C': {'deutsch': 'Cäsar', 'nato': 'Charlie'}, 
            'D': {'deutsch': 'Dora', 'nato': 'Delta'}, 
            'E': {'deutsch': 'Emil', 'nato': 'Echo'}, 
            'F': {'deutsch': 'Friedrich', 'nato': 'Foxtrot'}, 
            'G': {'deutsch': 'Gustav', 'nato': 'Golf'}, 
            'H': {'deutsch': 'Heinrich', 'nato': 'Hotel'}, 
            'I': {'deutsch': 'Ida', 'nato': 'India'}, 
            'J': {'deutsch': 'Julius', 'nato': 'Juliett'}, 
            'K': {'deutsch': 'Kaufmann', 'nato': 'Kilo'}, 
            'L': {'deutsch': 'Ludwig', 'nato': 'Lima'}, 
            'M': {'deutsch': 'Martha', 'nato': 'Mike'}, 
            'N': {'deutsch': 'Nordpol', 'nato': 'November'}, 
            'O': {'deutsch': 'Otto', 'nato': 'Oscar'}, 
            'P': {'deutsch': 'Paula', 'nato': 'Papa'}, 
            'Q': {'deutsch': 'Quelle', 'nato': 'Quebec'}, 
            'R': {'deutsch': 'Richard', 'nato': 'Romeo'}, 
            'S': {'deutsch': 'Samuel', 'nato': 'Sierra'}, 
            'T': {'deutsch': 'Theodor', 'nato': 'Tango'}, 
            'U': {'deutsch': 'Ulrich', 'nato': 'Uniform'}, 
            'V': {'deutsch': 'Viktor', 'nato': 'Victor'}, 
            'W': {'deutsch': 'Wilhelm', 'nato': 'Whiskey'}, 
            'X': {'deutsch': 'Xanthippe', 'nato': 'X-Ray'}, 
            'Y': {'deutsch': 'Ypsilon', 'nato': 'Yankee'}, 
            'Z': {'deutsch': 'Zacharias', 'nato': 'Zulu'}, 
            'Ä': {'deutsch': 'Ärger', 'nato': 'Ärger'}, 
            'Ö': {'deutsch': 'Ökonom', 'nato': 'Ökonom'}, 
            'Ü': {'deutsch': 'Übermut', 'nato': 'Übermut'}
        }

    def spell(self, text: str) -> str:
        result = ""
        for character in text:
            if character.upper() in self.alphabet:
                result += f"[red]{character.upper()}[/red]{self.alphabet[character.upper()][self.categorie][1:]}"
            elif character != " ":
                result += f"[red]{character.upper()}[/red]"
            else:
                result += character

            result += "\n"
        return result

@app.command()
def spell_out(text: str, 
              categorie: Annotated[
                  str, 
                  Option(help="Es stehen das Deutsche und das Nato Alphabet zur Verfügung")
              ] = "deutsch",
              in_newline: Annotated[
                  bool,
                  Option(help="Alles in einer neuen Zeile?")
              ] = False) -> None:
    """
    Nimmt ein beliebigen Text entgegen und gibt ihn buchstabiert zurück.
    
    Args:\n
    text - Den zu buchstabierenden Text \n
    categorie - entweder nato oder deutsch \n
    end - das Endzeichen der Ausgabe. Wird "" übergeben, erscheint die Ausgabe in der gleichen Zeile. \n

    Ausgabe: \n
    Buchstabierend auf die Standardausgabe
    """
    console = Console()
    alpha = Alphabet(categorie)
    result = alpha.spell(text)
    
    if in_newline:
        console.print(result)
    else:
        console.print(result.replace("\n", ""))


if __name__ == '__main__':
    app()

