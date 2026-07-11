from pathlib import Path
from hashlib import sha256
from hashlib import sha512
from hashlib import md5
from datetime import datetime
import os

class FileManager:
    
    def __init__(self, path : str | Path):
        
        self._ALGORITHMS = {

        "sha256": sha256,

        "sha512": sha512,

        "md5": md5,

        }
        
        
        self._path = Path(path)
        
     
    

    def exists(self) -> bool:
        """
        The method to check whether the file exists.
        It was created using with **pathlib.Path**
        
       
        Returns
        -------
            True if the file exists.
            False otherwise.
        """
        
        return self._path.exists()
    
    
    
    
    
    def hash(
       self,
       algorithm: str ="sha256"  
    ) -> str:
        """

        The method to get a file's hash read with the indicated algorithm.
        
        Params
        ------
        algorithm: str, default="sha256",
        Hash algorithm to use.
        
        Returns
        -------
        
        The hash value (str)
        
        Supported Algorithms
        ---------- 
        * sha512 
        * sha256
        * md5 
        
        Raises
        ------
        
        ValueError
        FileNotFoundError

        """
        

        try:

            hash_function = self._ALGORITHMS[algorithm]
            

        except KeyError as exc:

            raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc

        return hash_function(self._path.read_bytes()).hexdigest()
    
    
    
    
    
    def info(self) -> dict[str, str | Path | int | bytes]:
        """
        
        The method gets infos about the file.
        
        Returns
        -------
        
        Info about the file (dict)
        
        """
        infos = {}
        
        stat = self._path.stat()

        infos = {

            "name": self._path.name,

            "path": self._path.resolve(),

            "size": stat.st_size,

            "created_time": datetime.fromtimestamp(stat.st_birthtime).strftime("%d/%m/%Y"),

            "extension": self._path.suffix,
            
            "content": self._path.read_bytes()

        }
        
        return infos          

  
        
        
        