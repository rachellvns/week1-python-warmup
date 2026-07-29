from pydantic import BaseModel, Field, ValidationError

# SEO Audit has 3 pillars: 
# technical, on-page, off-page

# 1st pillar
class TechnicalSEO(BaseModel):
    page_speed: float = Field(gt=0)
    broken_links: int = Field(default=0, ge=0)
    mobile_friendly: bool
    crawled_pages: int = Field(default=0, ge=0)

# 2nd pillar
class OffPageSEO(BaseModel):
    backlinks : int = Field(default=0, ge=0)
    referring_domains: int = Field(default=0, ge=0)
    brand_mentions: int = Field(default=0, ge=0)

good_data = '{"backlinks": 5, "referring_domains": 2}'
tec = OffPageSEO.model_validate_json(good_data)
print(tec)

default_data = '{''}'
tec = OffPageSEO.model_validate_json(default_data)
print(tec)

try:
    bad_data = '{"backlinks": 3, "referring_domains": 2, "brand_mentions": "False"}'
    tec = OffPageSEO.model_validate_json(bad_data)
    print(tec)
except ValidationError as e:
    print("Rejected, contain incompatible field!")