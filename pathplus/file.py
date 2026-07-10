from pathlib import Path


class FileManager:
    
    def __init__(self, path : str | Path):
        
        self._path = Path(path)
    
    @property
    def exists(self) -> bool:
        """
        The method to check whether the file exists.
        It was created using with **pathlib.Path** 
        
        Returns
        -------
            True : The file is exists
            False : The File is **not** exists
        """
        
        return Path.exists(self._path)