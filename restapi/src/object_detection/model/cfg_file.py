from pydantic import BaseModel


class CfgFile(BaseModel):
	path: str
	dir: str
