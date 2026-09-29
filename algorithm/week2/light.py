def traffic_light(color: str) -> str:
    if color == "Red":
        return "Stop"
    elif color == "Yellow":
        return "Ready"
    elif color == "Green":
        return "Go"
    else:
        return "Invalid"
