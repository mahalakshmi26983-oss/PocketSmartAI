import os
import httpx
import asyncio


PROVIDERS = {
    "openai": {
        "api_key": "OPENAI_API_KEY",
        "url": "https://api.openai.com/v1/chat/completions",
        "model": "gpt-4o-mini",
    },
    "groq": {
        "api_key": "GROQ_API_KEY",
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "model": "llama-3.3-70b-versatile",
    },
    "mistral": {
        "api_key": "MISTRAL_API_KEY",
        "url": "https://api.mistral.ai/v1/chat/completions",
        "model": "mistral-large-latest",
    },
    "deepseek": {
        "api_key": "DEEPSEEK_API_KEY",
        "url": "https://api.deepseek.com/chat/completions",
        "model": "deepseek-chat",
    },
    "xai": {
        "api_key": "XAI_API_KEY",
        "url": "https://api.x.ai/v1/chat/completions",
        "model": "grok-4",
    },
}


async def chat_with_provider(provider: str, message: str):

    if provider not in PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    config = PROVIDERS[provider]

    api_key = os.getenv(config["api_key"])

    if not api_key:
        raise ValueError(
            f"{config['api_key']} is missing in .env"
        )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": config["model"],
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
    }

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            config["url"],
            headers=headers,
            json=payload
        )

    if response.status_code != 200:
        raise Exception(
            f"{provider} API error: {response.text}"
        )

    data = response.json()

    return {
        "provider": provider,
        "model": config["model"],
        "response": data["choices"][0]["message"]["content"]
    }