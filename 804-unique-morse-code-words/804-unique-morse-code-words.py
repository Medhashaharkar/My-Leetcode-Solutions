class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....","i": "..","j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-","r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        
        result = []
        
        for w in words:
            temp_result = ""
            for i in w:
                temp_result = temp_result + morse[i]
            result.append(temp_result)
        
        return len(set(result))