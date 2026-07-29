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

class OnPageSEO(BaseModel):
    title: str = Field(min_length=15, max_length=60)
    meta_description: str = Field(default="", max_length=160)
    search_intent: str = Field(default="", max_length=30)
    keywords: list[str] = Field(default=[])
    
good_data = '{"title": "How to cure cancer", "meta_description": "A guide to cure the deadliest desease on earth", "search_intent": "informational", "keywords":["cancer", "disease"]}'
on = OnPageSEO.model_validate_json(good_data)
print(on)

bad_data = '{"meta_description": "A guide to cure the deadliest desease on earth", "search_intent": "informational", "keywords":["cancer", "disease"]}'
try:
    on = OnPageSEO.model_validate_json(bad_data)
    print(on)
except ValidationError as e:
    print("Rejected, missing required field!")