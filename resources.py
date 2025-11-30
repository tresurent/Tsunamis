# resources.py
from dataclasses import dataclass
from typing import List

@dataclass
class Resource:
    name: str
    url: str
    category: str
    icon: str  # simple text icon name for now

def load_default_resources() -> List[Resource]:
    """Return a list of common XULA/CPSC resource links."""
    return [
        Resource(
            name="XULA Academic Calendar",
            url="https://www.xula.edu/academics/calendar",
            category="Academics",
            icon="calendar"
        ),
        Resource(
            name="Drop Deadline Calendar",
            url="https://www.xula.edu/registrar",
            category="Academics",
            icon="deadline"
        ),
        Resource(
            name="CRN Tools",
            url="https://selfservice.xula.edu",
            category="Courses",
            icon="tools"
        ),
        Resource(
            name="CPSC Tutoring Info",
            url="https://www.xula.edu/computer-science",
            category="Tutoring",
            icon="tutor"
        ),
    ]
