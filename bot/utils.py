import random
import tiktoken

def roll_dice(sides):
    return random.randint(1, sides)

def split_string(str, max_length=1800):
    '''Takes a string and splits it into a list where each item in the list is no more than 1800 characters and ends on a sentence boundary'''

    # Find all occurrences of the ``` characters
    code_indices = []
    start_index = str.find("```")
    while start_index != -1:
        end_index = str.find("```", start_index + 3)
        if end_index != -1:
            code_indices.append((start_index, end_index + 3))
            start_index = str.find("```", end_index + 3)
        else:
            break

    substrings = []
    start = 0
    for code_start, code_end in code_indices:
        if start < code_start:
            # Add substring before the code block
            substring = str[start:code_start]
            if len(substring) > max_length:
                # Check if substring exceeds maximum length
                continue
            substrings.append(substring)
        # Add code block as a single substring
        substrings.append(str[code_start:code_end])
        start = code_end
    if start < len(str):
        # Add the rest of the string as a substring
        substring = str[start:]
        if len(substring) <= max_length:
            substrings.append(substring)

    # Split each substring into smaller chunks based on sentence boundaries
    final_substrings = []
    for substring in substrings:
        if len(substring) > max_length:
            while len(substring) > max_length:
                last_boundary_index = substring[:max_length].rfind(".")
                if last_boundary_index == -1:
                    last_boundary_index = substring[:max_length].rfind("?")
                    if last_boundary_index == -1:
                        last_boundary_index = substring[:max_length].rfind("!")
                        if last_boundary_index == -1:
                            last_boundary_index = max_length
                        else:
                            last_boundary_index += 1
                    else:
                        last_boundary_index += 1
                else:
                    last_boundary_index += 1
                final_substrings.append(substring[:last_boundary_index])
                substring = substring[last_boundary_index:]
            final_substrings.append(substring)
        else:
            final_substrings.append(substring)

    return final_substrings

def num_tokens_from_messages(messages, model="gpt-3.5-turbo"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
        See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")