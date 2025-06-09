from strands import Agent
from strands.tools.mcp import MCPClient
from strands_tools import http_request
from mcp import stdio_client, StdioServerParametrs

#Define naming focused system prompt:
NAMING_SYSTEM_PROMPT = """
You are an assitant that helps to name open source projects.

