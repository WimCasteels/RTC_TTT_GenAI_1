import cohere

API_key  = "fsUZa6Yd0VzMfgHG5PecZbpFnDFDp57iYpfQ5ZnK"

co = cohere.Client(API_key)

def chatbot_response(prompt):
    '''This function takes as input a prompt, then sends the prompt to the cohere API and and returns the LLM response '''
    response = co.chat(message=prompt)
    return response.text