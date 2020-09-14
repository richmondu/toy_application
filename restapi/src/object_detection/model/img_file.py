from pydantic import BaseModel


class ImgFile(BaseModel):
	path: str
	dir: str
