import openai

# 设置OpenAI API密钥
openai.api_key = '***'

# 定义ChatGPT的交互函数
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # ChatGPT模型的名称
        prompt=prompt,
        temperature=0.7,  # 控制输出的创造性和多样性，值越低越保守，值越高越创造性
        max_tokens=1000,  # 生成的最大标记数
        n=1,  # 生成的回复数
        stop=None,  # 可以是一个字符串或字符串列表，用于指定生成文本的终止标记
        timeout=15,  # API请求的超时时间（以秒为单位）
    )

    # 获取模型生成的回复
    reply = response.choices[0].text.strip()
    return reply

# 测试ChatGPT交互
prompt = "你好！"
while True:
    user_input = input("用户：")
    prompt += user_input + "\n"
    reply = chat_with_gpt(prompt)
    prompt += reply + "\n"
    print("ChatGPT：", reply)

