def traffic_light(color: str) -> str:
    match color:
        case "Red":
            return "Stop"

        case "Yellow":
            return "Ready"

        case "Green":
            return "Go"

        case _:
            return "Invalid"
