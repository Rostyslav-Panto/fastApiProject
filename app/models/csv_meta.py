from sqlmodel import SQLModel, Field


class CSVMetaBase(SQLModel):
    name: str


class CSVMeta(CSVMetaBase, table=True):
    id: int = Field(default=None, primary_key=True)


class CSVMetaCreate(CSVMetaBase):
    pass
