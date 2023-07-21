import os
import openai

openai.organization = "org-4JqLNzk5F86VGcrPxDKwcFZl"
openai.api_key_path = "/home/cupsponge/projects/keys/openai.key"
#print( openai.Model.list() )

MODEL = "gpt-3.5-turbo"

class ChatBot:
    def __init__( self, context="You are a helpful assistant." ):
        self.context = context
        self.messages = [{"role": "system", "content": context}]

    def QueryChatBot( self, userMsg ):
        self.messages.append( {"role": "user", "content": userMsg } )
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=self.messages
        )

        aiMsg = response["choices"][0]["message"]
        self.messages.append( aiMsg )
        return response

    def ResetChat( self ):
        self.messages = [{"role": "system", "content": self.context}]

    def SetPrompt( self, prompt ):
        self.prompt = prompt

    def SetContext( self, context ):
        self.context = context


    
print( "Chat with Chat GPT~" )
chatBot = ChatBot( "You are a pirate" )
promptMsg = "What would you like to ask chatGPT? Type 'Reset' to reset the conversation, or 'Quit' to quit the program.\n"
userMsg = input( promptMsg )

while( userMsg != "Quit" ):
    if( userMsg == "Reset" ):
        chatBot.ResetChat()
    else:
        response = chatBot.QueryChatBot( userMsg )
        aiMsg = response["choices"][0]["message"]
        print( "\n" + aiMsg["content"] )
        print( "(Total tokens: " + str( response["usage"]["total_tokens"] ) + ")\n" )

    userMsg = input( promptMsg )

print( "Goodbye!" )