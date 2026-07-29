from pydantic import BaseModel, Field, ValidationError

class TraineeProfile(BaseModel):
    name: str
    years_experience: float = Field(ge= 0)
    current_role: str
    target_role: str = "AI Engineer"
    skills: list[str]


#valid JSON payload
data = '{"name": "Rachell", "years_experience" : 0, "current_role": "student", "target_role": "AI Engineer & Data Scientist", "skills": ["database", "java"]}'
try:
    print("\nAll data is filled with the right constraint")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)

#valid JSON payload (where target role is optional)
data = '{"name": "Rachell", "years_experience" : 0, "current_role": "student", "skills": ["database", "java"]}'
try:
    print("\nTarget role not existed")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)

#Invalid JSON payload (name not existed)
data = '{"years_experience" : 0, "current_role": "student", "skills": ["database", "java"]}'
try:
    print("\nName field not existed")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)

#Invalid JSON payload (years of experience outside of the constraint)
data = '{"name": "Rachell", "years_experience" : -1, "current_role": "student", "skills": ["database", "java"]}'
try:
    print("\nYears of experience less than 0")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)
    
#Invalid JSON payload (current role not existed)
data = '{"name": "Rachell", "years_experience" : 0, "skills": ["database", "java"]}'
try:
    print("\nCurrent role field not existed")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)

#Invalid JSON payload (skills not existed)
data = '{"name": "Rachell", "years_experience" : 0, "current_role": "student"}'
try:
    print("\nSkills field not existed")
    tp = TraineeProfile.model_validate_json(data)
except ValidationError as e:
    print(e)