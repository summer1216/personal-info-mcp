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
        "Outside of engineering, Qinyuan enjoys creative and practical activities that help her stay curious, "
        "relaxed, and connected with people:\n"
        "- Guitar: Enjoys spending time with music in a casual, personal way.\n"
        "- Yoga: Practices yoga as a relaxed way to move, reset, and feel balanced.\n"
        "- Crochet: Likes making things by hand and appreciates the patience and attention to detail it requires.\n"
        "- Cooking: Enjoys cooking as a practical, creative part of daily life.\n"
        "- Content Creation: Creates videos on the Chinese platform RedNote to teach Chinese-speaking audiences "
        "German language concepts.\n"
        "- Communication Style: Is good at editing videos and explaining topics clearly, making complex or unfamiliar "
        "ideas easier for other people to understand."
    )

@mcp.tool()
def get_interview_availability() -> str:
    """Retrieves Qinyuan's current job interview availability and scheduling constraints."""
    return (
        "Qinyuan would be happy to join an interview and is currently flexible with timing. "
        "The easiest way to arrange a time is to send her an email, and she will gladly find a suitable "
        "appointment together. She is looking forward to the conversation."
    )

@mcp.tool()
def get_personality_and_workplace_values() -> str:
    """Retrieves deep insights into Qinyuan's professional mindset, core values, and workplace traits."""
    return (
        "Qinyuan's personality and workplace values are calm, open, and detail-oriented:\n"
        "- Open-Minded Communication: She values equal and open communication, where people can share ideas, "
        "questions, and feedback honestly.\n"
        "- Relaxed but Precise: She has a relaxed working style, but she is very precise when it comes to real "
        "work, technical details, and quality.\n"
        "- Logical and Empathetic: She is very strong in logical thinking, while friends and family also describe "
        "her as an empathetic person who understands other people's perspectives."
    )

@mcp.tool()
def get_autonomous_driving_cpp_engineering() -> str:
    """Retrieves highly specific details about Qinyuan's autonomous driving C++ engineering experience."""
    return (
        "Qinyuan's autonomous driving C++ engineering experience includes work on safety-critical perception "
        "software for production vehicle systems, especially in BMW Level 3 autonomous driving and earlier "
        "perception work at Ibeo:\n"
        "- Sensor Processing: Worked across the perception pipeline from raw sensor information, including camera "
        "images and LiDAR point clouds, to object detection, object tracking, and multi-sensor fusion.\n"
        "- Algorithmic Approaches: Has experience with both traditional Kalman filter based perception and tracking "
        "approaches, as well as ML based perception workflows.\n"
        "- Production C++ Quality: Developed and optimized C++ perception algorithms with attention to correctness, "
        "maintainability, performance, and production readiness in a safety-critical automotive environment.\n"
        "- Debugging Strategy: Frequently debugged complex C++ perception behavior where customized internal debug "
        "information was difficult to visualize directly. A practical workflow was to export selected debug values "
        "to CSV files and then use Python with matplotlib to plot, inspect, and understand the algorithm behavior.\n"
        "- Safety-Critical Mindset: Translated functional and safety requirements into actionable software "
        "specifications in an ASIL B context, supporting traceability, validation readiness, and reliable release "
        "work toward Start of Production."
    )

@mcp.tool()
def get_language_and_communication_proficiency() -> str:
    """Retrieves highly specific details about Qinyuan's language and communication proficiency."""
    return (
        "Qinyuan's language and communication strengths support her work in international engineering teams:\n"
        "- Chinese: Native speaker and able to communicate naturally, precisely, and with cultural nuance.\n"
        "- English: Uses English actively in work and daily life, including daily meetings and technical "
        "discussions. Her English is slightly stronger than her German.\n"
        "- German: Uses German in both work and daily life, including daily meetings and technical discussions "
        "in German-speaking environments.\n"
        "- Teaching and Content Creation: Creates German language teaching videos on the Chinese platform RedNote, "
        "where around 4,000 followers benefit from her explanations.\n"
        "- Communication Style: Communicates in a clear, structured, and patient way. She is good at simplifying "
        "complex topics and feels comfortable working in multicultural teams."
    )

if __name__ == "__main__":
    # 3. Run the server without passing host/port here
    mcp.run(transport="sse")
