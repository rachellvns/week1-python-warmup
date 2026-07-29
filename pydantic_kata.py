from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator

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

#3rd pillar
class OnPageSEO(BaseModel):
    title: str = Field(min_length=15, max_length=60)
    meta_description: str = Field(default="", max_length=160)
    search_intent: str = Field(default="", max_length=30)
    keywords: list[str] = Field(default=[])
    
class SEOAudit(BaseModel):
    website: str = Field(frozen=True)
    technical: TechnicalSEO | None = None
    off_page: OffPageSEO | None = None
    on_page: OnPageSEO | None = None
    
    @model_validator(mode="after")
    def validate_one_pillar_filled(self):
        if not any ([self.technical, self.off_page, self.on_page]):
            raise ValueError()
        return self

good_data = """
    {       
        "website": "https://kavio.tech/", 
        "on_page": 
        {
            "title": "KAVIO - AI products & agentic services", 
            "meta_description": "KAVIO is an AI agency for companies world wide. Products you can buy and agents we build for you - from answer-engine visibility to full agentic automation.", 
            "search_intent": "commercial", 
            "keywords":["GEO", "AEO", "Agent Experience"]
        }
    }
    """
aud = SEOAudit.model_validate_json(good_data)
print(aud)

try:
    bad_data = '{"website": "https://google.com/"}'
    aud = SEOAudit.model_validate_json(bad_data)
    print(aud)
except ValidationError as e:
    print("\nRejected, you should choose at least 1 pillar")