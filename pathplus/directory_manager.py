from pathlib import Path
import os


class DirectoryManager:
    
    def __init__(self,path : str | Path):

        
        
        self._path = Path(path)
    
    
  

    def tree(self) -> dict[str, list[str]]:
        """
        Generates a dictionary representing the directory tree.
        
        Returns:
            dict[str, list[str]]: A dictionary where the keys are absolute directory 
                                paths (as strings) and values are lists of file 
                                names contained within those directories.
        """
        data = {}
            
        for root, dirs, files in os.walk(self._path.absolute()):
            if files:  # Only include directories that actually contain files
                # Converting root (path) to str to strictly match your type hint
                data[str(root)] = files
                
        return data



  

    def total_size(self) -> str | None:
        """
        Calculates and returns the total size of the directory and all its contents
        formatted in Bytes, MB, or GB.
        
        Returns:
            str | None: The formatted total size, or None if the path is not a directory.
        """
        if not self._path.is_dir():
            return None

        # 1. Calculate the actual total size of all files inside the directory
        total_bytes = 0
        for root, _, files in os.walk(self._path.absolute()):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Use os.path.getsize to get the size of each file
                    total_bytes += os.path.getsize(file_path)
                except OSError:
                    # Handle cases where a file might have been deleted or is inaccessible
                    continue

        # 2. Format the size dynamically
        if total_bytes < 1_000_000:
            return f"{total_bytes} Bytes"
        elif total_bytes < 1_000_000_000:
            # Rounding to 2 decimal places makes the string look much cleaner
            return f"{total_bytes / 1_000_000:.2f} MB"
        else:
            return f"{total_bytes / 1_000_000_000:.2f} GB"
        
        
        
        
