
from nerfstudio.engine.trainer import TrainerConfig
from nerfstudio.plugins.types import MethodSpecification

MyMethod = MethodSpecification(
    config=TrainerConfig(
        method_name="MyMethod",
        description="My method description - explain what it does",
        method_author="Avishai & Nir",
        method_year="2023",
        pipeline=[
        ],
    ),
    description="My method description",
) 
        
        