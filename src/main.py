from textnode import TextNode

def main(): 
    textnode1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    textnode2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode1 == textnode2)
    
main()