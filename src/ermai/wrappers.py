from openai import OpenAI as OAI
import anthropic
from google import genai

class OpenAI:
	def __init__(self, api_key=None, instruction="You are a helpful AI assistant.", model="gpt-4o-mini", maxtokens=1000, temperature=0.7):
		self.client = OAI(api_key=api_key)
		self.instruction = instruction
		self.model = model
		self.mt = maxtokens
		self.temp = temperature
		self.messages = [{"role": "system", "content": self.instruction}]
	def prompt(self, query):
		self.messages.append({"role": "user", "content": str(query)})
		response = self.client.chat.completions.create(
			model="gpt-4o",  # Specify the model you want to use
			messages=self.messages,
			max_tokens=self.mt,
			temperature=self.temp
		)
		answer = str(response.output_text)
		self.messages.append({"role": "assistant", "content": answer})
		return answer

class Anthropic:
	def __init__(self, api_key=None, instruction="You are a helpful AI assistant.", model="claude-3-5-haiku", maxtokens=1000, temperature=0.7):
		self.client = anthropic.Anthropic(api_key=api_key)
		self.instruction = instruction
		self.messages = []
		self.mt = maxtokens
		self.temp = temperature
		self.model = model
	def prompt(self, query):
		self.messages.append({"role": "user", "content": str(query)})
		response = self.client.messages.create(
			model=self.model,
			max_tokens=self.mt,
			temperature=self.temp,
			system=self.instruction,
			messages=self.messages
		)
		answer = response.content
		self.messages.append({"role": "assistant", "content": answer})
		return answer

class GoogleAI:
	def __init__(self, api_key=None, model="gemini-3.5-flash", instruction="You are a helpful AI assistant.", maxtokens=1000, temperature=0.7):
		self.instruction = instruction
		self.model = model
		self.mt = maxtokens
		self.temp = temperature
		self.client = genai.Client(api_key=api_key)
		self.messages = [{"role": "system", "content": self.instruction}]
	def prompt(self, query):
		self.messages.append({"role": "user", "content": str(query)})
		response = client.models.generate_content(
			model=self.model,
			contents=self.messages
			maxtokens=self.mt
			temperature=self.temp
		)
		answer = response.text
		self.messages.append({"role": "model", "content": answer})
		return answer
