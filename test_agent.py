from src.agent import run_agent

result = run_agent("Find student S101.")

print("\nRESULT TYPE:")
print(type(result))

print("\nFINAL ANSWER:")
print(result["answer"])

print("\nTOOL TRACE:")
print(result["tool_trace"])