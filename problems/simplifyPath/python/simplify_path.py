class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        split_path = path.split("/")
        directories = []
        for directory in split_path:
            if directories and directory == "..":
                directories.pop(-1)
            elif directory in (".", "", ".."):
                continue
            else:
                directories.append(directory)

        return f"/{'/'.join(directories)}"


if __name__ == "__main__":
    s = "/../"
    print(Solution().simplifyPath(s))
