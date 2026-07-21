from pathlib import Path
from hashlib import sha256
from hashlib import sha512
from hashlib import md5
from datetime import datetime


class FileManager:
    _ALGORITHMS = {

        "sha256": sha256,

        "sha512": sha512,

        "md5": md5,

        }
        
    def __init__(self, path : str | Path):
        
    
    
    
        self._path = Path(path)
        
    
    
  
    def get_path(self) -> Path:
        
        return self._path
    
  
    def set_path(self,target_path:str) -> None:
        
        self._path = Path(target_path)
    
    
    def hash(
       self,
       algorithm: str ="md5",
       file: Path | None = None 
    ) -> str:
        """

        The method to get a file's hash read with the indicated algorithm.
        
        Params
        ------
        algorithm: str, default="md5",
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
            if file is not None:
                current_path = Path(file)

            else:
                current_path = self._path
        except KeyError as exc:

            raise ValueError(f"Unsupported hash algorithm: {algorithm}") from exc

        return hash_function(current_path.read_bytes()).hexdigest()
    
    
    
    
    
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

            "created_time": datetime.fromtimestamp(stat.st_ctime).strftime("%d/%m/%Y"),

            "extension": self._path.suffix,
            

        }
        
        return infos

    
    
    def compare(self,other : Path) -> bool:
        
        """
        
        Compares two file hash values.
        
        """
        
        if self.hash() == self.hash(file=other):
            
            return True
        
        return False
    
   
    def verify(self,hash_value:str) -> bool:
        """
        
        Checks the file hash value.
        
        hash_value (str) : MD5  
        
        """
        if self.hash() == hash_value:
            return True
        
        return False
    
    
    def size(self) -> str:
        """
        
        Returns the file size.
        
        """
        
        
        if self._path.stat().st_size < 1000000:
            return f"{(self._path.stat().st_size)} Bytes"
            
        return f"{(self._path.stat().st_size / 1000000)} MB"