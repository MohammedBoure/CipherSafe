def convert_path(path: str) -> str:
    parts = path.split("\\")
    if len(parts) > 1:
        parts[0] = parts[0].replace("\\", "/")  
        return "/".join(parts)  
    return path

