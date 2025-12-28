# Exercise 19: Agentic Workflows with Tools
# Before creating agentic workflows, let's practice tool integration and decision making

from typing import List, Dict, Any, Optional, Callable
import json

# TODO: Create a class called 'Tool'
# - __init__: name, description, function, parameters_schema
# - execute: runs the tool function with parameters
# - get_schema: returns tool definition for LLM

# TODO: Create a class called 'ToolRegistry'
# - register_tool: adds tool to registry
# - get_available_tools: returns all tool schemas
# - execute_tool: finds and executes tool by name

# TODO: Create a class called 'Agent'
# - __init__: takes tool registry and system prompt
# - think: analyzes user query and decides what tools to use
# - plan: creates execution plan based on available tools
# - execute_plan: runs tools in sequence and combines results

# TODO: Create sample tools
# - calculator: performs mathematical operations
# - search: simulates information search
# - formatter: formats text in different styles

# TODO: Create a function called 'solve_with_agent'
# Parameters: query (str), agent (Agent)
# Uses agent to solve the query using available tools
# Returns final answer

class Tool:
    """Represents a tool that can be used by an agent"""

    def __init__(self, name: str, description: str, function: Callable, parameters_schema: Dict[str, Any]):
        self.name = name
        self.description = description
        self.function = function
        self.parameters_schema = parameters_schema

    def execute(self, parameters: Dict[str, Any]) -> Any:
        """Execute the tool with given parameters"""
        try:
            return self.function(**parameters)
        except Exception as e:
            return f"Tool execution error: {e}"

    def get_schema(self) -> Dict[str, Any]:
        """Return tool schema for LLM"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters_schema
        }

class ToolRegistry:
    """Registry of available tools"""

    def __init__(self):
        self.tools = {}

    def register_tool(self, tool: Tool):
        """Register a tool in the registry"""
        self.tools[tool.name] = tool

    def get_available_tools(self) -> List[Dict[str, Any]]:
        """Get schemas of all available tools"""
        return [tool.get_schema() for tool in self.tools.values()]

    def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> Any:
        """Execute a tool by name"""
        if tool_name not in self.tools:
            return f"Tool '{tool_name}' not found"

        tool = self.tools[tool_name]
        return tool.execute(parameters)

class Agent:
    """AI agent that can use tools to solve problems"""

    def __init__(self, tool_registry: ToolRegistry, system_prompt: str = "You are a helpful assistant with access to various tools."):
        self.tool_registry = tool_registry
        self.system_prompt = system_prompt
        self.conversation_history = []

    def think(self, query: str) -> Dict[str, Any]:
        """Analyze query and determine what tools to use"""
        query_lower = query.lower()

        plan = {
            "tools_needed": [],
            "reasoning": "",
            "execution_order": []
        }

        # Simple rule-based planning
        if any(word in query_lower for word in ['calculate', 'compute', 'math', 'sum', 'multiply']):
            plan["tools_needed"].append("calculator")
            plan["reasoning"] = "Mathematical calculation required"
            plan["execution_order"].append("calculator")

        if any(word in query_lower for word in ['search', 'find', 'lookup', 'information']):
            plan["tools_needed"].append("search")
            plan["reasoning"] = "Information search required"
            plan["execution_order"].append("search")

        if any(word in query_lower for word in ['format', 'style', 'display']):
            plan["tools_needed"].append("formatter")
            plan["reasoning"] = "Text formatting required"
            plan["execution_order"].append("formatter")

        if not plan["tools_needed"]:
            plan["reasoning"] = "No specific tools needed, can answer directly"

        return plan

    def plan(self, query: str) -> Dict[str, Any]:
        """Create detailed execution plan"""
        analysis = self.think(query)

        plan_details = {
            "query": query,
            "analysis": analysis,
            "steps": []
        }

        for tool_name in analysis["execution_order"]:
            tool_schema = None
            for tool in self.tool_registry.get_available_tools():
                if tool["name"] == tool_name:
                    tool_schema = tool
                    break

            if tool_schema:
                # Extract parameters needed from query (simplified)
                parameters = self._extract_parameters(query, tool_schema)

                plan_details["steps"].append({
                    "tool": tool_name,
                    "parameters": parameters,
                    "description": f"Execute {tool_name} with parameters: {parameters}"
                })

        return plan_details

    def _extract_parameters(self, query: str, tool_schema: Dict[str, Any]) -> Dict[str, Any]:
        """Extract tool parameters from query (simplified implementation)"""
        params = {}

        if tool_schema["name"] == "calculator":
            # Simple parameter extraction for calculator
            if "sum" in query or "+" in query:
                params["operation"] = "add"
                params["a"] = 10  # Simplified
                params["b"] = 20
            elif "multiply" in query or "*" in query:
                params["operation"] = "multiply"
                params["a"] = 5
                params["b"] = 4

        elif tool_schema["name"] == "search":
            params["query"] = query.split()[-1]  # Last word as search term

        elif tool_schema["name"] == "formatter":
            params["text"] = "Sample text"
            params["style"] = "uppercase"

        return params

    def execute_plan(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the plan and return results"""
        results = {
            "query": plan["query"],
            "tool_results": [],
            "final_answer": ""
        }

        for step in plan["steps"]:
            tool_name = step["tool"]
            parameters = step["parameters"]

            result = self.tool_registry.execute_tool(tool_name, parameters)
            results["tool_results"].append({
                "tool": tool_name,
                "parameters": parameters,
                "result": result
            })

        # Combine results into final answer
        if results["tool_results"]:
            results["final_answer"] = self._synthesize_answer(results["tool_results"])
        else:
            results["final_answer"] = "I can answer this directly without tools."

        return results

    def _synthesize_answer(self, tool_results: List[Dict[str, Any]]) -> str:
        """Synthesize tool results into a coherent answer"""
        if not tool_results:
            return "No tools were used."

        answer_parts = []
        for result in tool_results:
            tool_name = result["tool"]
            tool_result = result["result"]

            if tool_name == "calculator":
                answer_parts.append(f"Calculation result: {tool_result}")
            elif tool_name == "search":
                answer_parts.append(f"Search result: {tool_result}")
            elif tool_name == "formatter":
                answer_parts.append(f"Formatted text: {tool_result}")

        return " ".join(answer_parts)

# Tool functions
def calculator(operation: str, a: float, b: float) -> float:
    """Simple calculator tool"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Division by zero"
    else:
        return "Unknown operation"

def search(query: str) -> str:
    """Simulated search tool"""
    mock_results = {
        "python": "Python is a programming language",
        "ai": "AI stands for Artificial Intelligence",
        "weather": "Today's weather is sunny"
    }
    return mock_results.get(query.lower(), f"No information found for: {query}")

def formatter(text: str, style: str) -> str:
    """Text formatting tool"""
    if style.lower() == "uppercase":
        return text.upper()
    elif style.lower() == "lowercase":
        return text.lower()
    elif style.lower() == "title":
        return text.title()
    else:
        return text

def create_sample_tools() -> ToolRegistry:
    """Create and register sample tools"""
    registry = ToolRegistry()

    # Calculator tool
    calc_tool = Tool(
        name="calculator",
        description="Perform mathematical calculations",
        function=calculator,
        parameters_schema={
            "type": "object",
            "properties": {
                "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["operation", "a", "b"]
        }
    )

    # Search tool
    search_tool = Tool(
        name="search",
        description="Search for information",
        function=search,
        parameters_schema={
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    )

    # Formatter tool
    format_tool = Tool(
        name="formatter",
        description="Format text in different styles",
        function=formatter,
        parameters_schema={
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "style": {"type": "string", "enum": ["uppercase", "lowercase", "title"]}
            },
            "required": ["text", "style"]
        }
    )

    registry.register_tool(calc_tool)
    registry.register_tool(search_tool)
    registry.register_tool(format_tool)

    return registry

def solve_with_agent(query: str, agent: Agent) -> str:
    """Solve a query using the agent and its tools"""
    plan = agent.plan(query)
    result = agent.execute_plan(plan)
    return result["final_answer"]

def main():
    """Demonstrate agentic workflows with tools"""
    try:
        print("=== Agentic Workflows Exercise ===\n")

        # Create tools and agent
        tool_registry = create_sample_tools()
        agent = Agent(tool_registry)

        print("Available tools:")
        for tool in tool_registry.get_available_tools():
            print(f"- {tool['name']}: {tool['description']}")
        print()

        # Test queries
        test_queries = [
            "What is 10 + 20?",
            "Tell me about Python",
            "Format 'hello world' in uppercase"
        ]

        for i, query in enumerate(test_queries, 1):
            print(f"{i}. Query: {query}")

            # Show planning
            plan = agent.plan(query)
            print(f"   Plan: {plan['analysis']['reasoning']}")
            if plan['steps']:
                print(f"   Tools to use: {[step['tool'] for step in plan['steps']]}")

            # Execute
            answer = solve_with_agent(query, agent)
            print(f"   Answer: {answer}\n")

        print("✅ Agentic workflow demonstration completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
