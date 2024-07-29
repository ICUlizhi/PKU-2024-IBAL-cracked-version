from openai import OpenAI
import json

# api_key是你的key,在https://platform.deepseek.com/usage 注册,氪个一块够了
client = OpenAI(api_key="sk-988eb73686e24998a62dd62cdfdc19ac", base_url="https://api.deepseek.com")

# 对于最下面的main('a.txt', n, 'sample1.json' , prompt1)
# a.txt是文本
# sample1/2.json是参考的回答样本
# prompt1/2是提示,修改要求的话改这里文字和sample.json里相应位置的文字就行
# n是分割的段数,可调,每段一个词

#程序运行时长1min左右

def split_file(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    length = len(content)
    chunk_size = length // n
    chunks = [content[i:i + chunk_size] for i in range(0, length, chunk_size)]
    if len(chunks) > n:
        chunks[-2] += chunks[-1]
        chunks.pop()
    return chunks

def get_gpt_responses(chunks, sample, prompt0):
    responses = []
    for chunk in chunks:
        prompt = chunk + prompt0 
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": sample["system"]},
                {"role": "user", "content": sample["user"]},
                {"role": "assistant", "content": sample["assistant"]},
                {"role": "user", "content": prompt}
            ],
            stream=False,
            temperature=1.0
        )
        responses.append(response.choices[0].message.content.strip())
    return responses

def main(file_path, n, sample_path, prompt0):
    with open(sample_path, 'r', encoding='utf-8') as sample_file:
        sample = json.load(sample_file)
    chunks = split_file(file_path, n)
    responses = get_gpt_responses(chunks, sample, prompt0)
    for i, response in enumerate(responses):
        print(response)

prompt1 = "\n\n Find a new word in the text above and return its English definition in the format 'xxx : xxx' ,Please choose nouns, adjectives, adverbs, or verbs"
prompt2 = "\n\n Find a word in the text above which is rare but esay to guess by the text, and return your brief guess in the format 'xxx : xxx' ,Please choose nouns, adjectives, adverbs, or verbs"
main('a.txt', 12, 'sample1.json' , prompt1)
print("---------------") 
main('a.txt', 20, 'sample2.json' , prompt2) 
