import os
import openai

openai.organization = "org-4JqLNzk5F86VGcrPxDKwcFZl"
openai.api_key = os.getenv("OPENAI_API_KEY")
#print( openai.Model.list() )

MODEL = "gpt-3.5-turbo"

print( "Chat with Chat GPT~" )

messages = [{"role": "system", "content": "You are a helpful assistant."}]
userMsg = input( "What would you like to ask chatGPT? Type 'Reset' to reset the conversation, or 'Quit' to quit the program.\n" )

while( userMsg != "Quit" ):
    if( userMsg == "Reset" ):
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.append( {"role": "user", "content": userMsg } )
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )

    aiMsg = response["choices"][0]["message"]
    print( "\n" + aiMsg["content"] )
    print( "(Total tokens: " + str( response["usage"]["total_tokens"] ) + ")" )
    messages.append( aiMsg )

    userMsg = input( "\nWhat would you like to ask chatGPT? Type 'Reset' to reset the conversation, or 'Quit' to quit the program.\n" )

print( "Goodbye!" )