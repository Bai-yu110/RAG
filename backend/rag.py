from backend.llm import get_llm_response
from main import search_knowledge

def ask(prompt):
    docs = search_knowledge(prompt, top_k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    full_prompt = f"""
参考知识库内容：
{context}
用户问题：{prompt}
请严格依据知识库内容回答，不要编造信息。
"""
    return get_llm_response(full_prompt)