from zhipuai import ZhipuAI
 
client = ZhipuAI(api_key="f91eddc3a4af12a20b384dce80b14141.JEsuNrIh1Ea0Dw1O") # 填写您自己的APIKey
while True:
    prompt = input("user:")
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user","content": prompt}
        ],
    )
    answer = response.choices[0].message.content
    print("ZhipuAI:",answer)
#请给出最多两个概率最高的可能，以及相应的解决方法