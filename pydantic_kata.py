from pydantic import BaseModel, Field, ValidationError

# SEO Audit has 3 pillars: 
# technical, on-page, off-page
    
# 1st pillar
class TechnicalSEO(BaseModel):
    page_speed: float = Field(gt=0)
    broken_links: int = Field(default=0, ge=0)
    mobile_friendly: bool
    crawled_pages: int = Field(default=0, ge=0)

good_data = '{"page_speed": 5.3, "broken_links": 2, "mobile_friendly": "True", "crawled_pages": 7}'
tec = TechnicalSEO.model_validate_json(good_data)
print(tec)

bad_data = '{"broken_links": 3, "mobile_friendly": "False", "crawled_pages": 8}'
try:
    tec = TechnicalSEO.model_validate_json(bad_data)
    print(tec)
except ValidationError as e:
    print("Rejected, missing required field!")