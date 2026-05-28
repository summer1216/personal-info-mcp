import os
from mcp.server.fastmcp import FastMCP

# 1. Fetch the port and set it right at the top
port = int(os.environ.get("PORT", 8080))

# 2. Pass host and port directly into the FastMCP initialization
mcp = FastMCP("Qinyuan Portfolio Context Server", host="0.0.0.0", port=port)

@mcp.tool()
def get_hobbies_and_life_experience() -> str:
    """Retrieves Qinyuan's personal hobbies, life experiences, and interests outside of core engineering."""
    return (
        "Outside of designing data pipelines and cloud architectures, Qinyuan is highly active and well-rounded:\n"
        "1. Guitar: Passionate about acoustic fingerstyle guitar and music theory.\n"
        "2. Yoga: Practices regularly to maintain mental clarity, focus, and physical resilience.\n"
        "3. Open-Mindedness: Has lived and worked across diverse global/cultural settings, which naturally "
        "fuels an open-minded, non-rigid approach to technical problem-solving."
    )

@mcp.tool()
def get_interview_availability() -> str:
    """Retrieves Qinyuan's current job interview availability and scheduling constraints."""
    return (
        "Qinyuan is currently managing a part-time transition during parental leave and is highly flexible "
        "for video interviews. Preferred slots are Mondays through Thursdays between 09:00 and 15:00 CEST. "
        "However, exceptions can easily be accommodated outside these hours given a 24-hour heads-up."
    )

@mcp.tool()
def get_personality_and_workplace_values() -> str:
    """Retrieves deep insights into Qinyuan's professional mindset, core values, and workplace traits."""
    return (
        "Qinyuan approaches software engineering with a blend of intense curiosity and deep professional humility. "
        "Key workplace values include:\n"
        "- Radical Collaboration: Believes the best systems are built through clear, egoless team communication.\n"
        "- Relentless Troubleshooting: A self-driven builder who thrives on taking complex, ambiguous tasks "
        "(like building this custom MCP cloud environment) and seeing them safely through to production."
    )

if __name__ == "__main__":
    # 3. Run the server without passing host/port here
    mcp.run(transport="sse")
